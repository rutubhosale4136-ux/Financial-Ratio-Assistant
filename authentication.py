"""Registration, login, and session management with PBKDF2 password hashing.

College Project: Financial Statement Ratio Analysis Assistant
This module handles:
1. PBKDF2 password hashing and salt generation (using Python standard library hashlib & secrets).
2. Input validation for name, email, and password.
3. User registration with duplicate email prevention.
4. User login and credential verification.
5. Streamlit session state management for logged-in users.
6. Streamlit UI for login and registration forms.
"""

import hashlib
import re
import secrets
import streamlit as st
import database

# Number of PBKDF2 iterations (industry standard, secure & fast)
HASH_ITERATIONS = 100_000


# ============================================================================
# Password Hashing & Verification (PBKDF2)
# ============================================================================

def hash_password(password: str, salt: str = None) -> tuple[str, str]:
    """Hash a password using PBKDF2-HMAC-SHA256 with a unique cryptographic salt.

    Plain-text passwords are never stored.

    Args:
        password: Plain-text password string.
        salt: Optional hex salt string. If None, a new 16-byte random salt is generated.

    Returns:
        tuple: (password_hash_hex, salt_hex)
    """
    if salt is None:
        salt = secrets.token_hex(16)

    derived = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt.encode("utf-8"),
        HASH_ITERATIONS,
    )
    return derived.hex(), salt


def verify_password(password: str, stored_hash: str, salt: str) -> bool:
    """Verify an entered password against the stored PBKDF2 hash.

    Uses constant-time comparison (secrets.compare_digest) to prevent timing attacks.
    """
    if not password or not stored_hash or not salt:
        return False
    computed_hash, _ = hash_password(password, salt)
    return secrets.compare_digest(stored_hash, computed_hash)


# ============================================================================
# Input Validation
# ============================================================================

def validate_email(email: str) -> tuple[bool, str]:
    """Validate email format."""
    email = (email or "").strip()
    if not email:
        return False, "Email address is required."
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(pattern, email):
        return False, "Please enter a valid email address (e.g. student@example.com)."
    return True, ""


def validate_registration_inputs(
    full_name: str,
    email: str,
    password: str,
    confirm_password: str,
) -> tuple[bool, str]:
    """Validate all user registration inputs."""
    name = (full_name or "").strip()
    if not name:
        return False, "Full name is required."
    if len(name) < 2:
        return False, "Full name must be at least 2 characters long."

    valid_email, email_msg = validate_email(email)
    if not valid_email:
        return False, email_msg

    if not password:
        return False, "Password is required."
    if len(password) < 6:
        return False, "Password must be at least 6 characters long."

    if password != confirm_password:
        return False, "Passwords do not match. Please re-enter confirm password."

    return True, ""


# ============================================================================
# User Registration and Authentication Logic
# ============================================================================

def register_user(
    full_name: str,
    email: str,
    password: str,
    confirm_password: str,
    db_path=None,
) -> tuple[bool, str]:
    """Register a new user account.

    Validates input, checks for duplicate email, hashes the password with a unique salt,
    and inserts the record into SQLite.

    Returns:
        tuple: (success_bool, message_str)
    """
    is_valid, error_msg = validate_registration_inputs(
        full_name, email, password, confirm_password
    )
    if not is_valid:
        return False, error_msg

    normalised_email = email.strip().lower()

    # Pre-check for duplicate email in database
    existing_user = database.get_user_by_email(normalised_email, db_path=db_path)
    if existing_user is not None:
        return False, "An account with this email already exists. Please log in."

    # Hash the password with a newly generated salt
    password_hash, password_salt = hash_password(password)

    try:
        database.create_user(
            full_name=full_name.strip(),
            email=normalised_email,
            password_hash=password_hash,
            password_salt=password_salt,
            db_path=db_path,
        )
        return True, "Registration successful! You can now log in with your credentials."
    except database.DatabaseError as e:
        return False, str(e)


def authenticate_user(
    email: str,
    password: str,
    db_path=None,
) -> tuple[bool, str, dict | None]:
    """Authenticate a user using their email and password.

    Returns:
        tuple: (success_bool, message_str, user_dict_or_None)
    """
    normalised_email = (email or "").strip().lower()
    if not normalised_email or not password:
        return False, "Email and password are required.", None

    user = database.get_user_by_email(normalised_email, db_path=db_path)
    if user is None:
        # Generic message avoids user enumeration
        return False, "Invalid email or password.", None

    if not verify_password(password, user["password_hash"], user["password_salt"]):
        return False, "Invalid email or password.", None

    # Return safe user dictionary without hash and salt
    safe_user = {
        "id": user["id"],
        "full_name": user["full_name"],
        "email": user["email"],
        "created_at": user.get("created_at"),
    }
    return True, "Login successful!", safe_user


# ============================================================================
# Session State Management
# ============================================================================

def init_session_state():
    """Ensure authentication keys exist in Streamlit session state."""
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    if "user" not in st.session_state:
        st.session_state["user"] = None


def is_authenticated() -> bool:
    """Check if a user is currently logged in."""
    init_session_state()
    return bool(st.session_state.get("logged_in") and st.session_state.get("user"))


def get_current_user() -> dict | None:
    """Get the currently logged-in user dictionary from session state."""
    init_session_state()
    return st.session_state.get("user")


def get_current_user_id() -> int | None:
    """Get the user ID of the currently logged-in user for database queries."""
    user = get_current_user()
    return user["id"] if user else None


def login_session(user_data: dict):
    """Store the authenticated user in Streamlit session state."""
    init_session_state()
    st.session_state["logged_in"] = True
    st.session_state["user"] = user_data


def logout():
    """Clear session state, logging the user out immediately."""
    st.session_state["logged_in"] = False
    st.session_state["user"] = None
    st.session_state.clear()
    st.rerun()


# ============================================================================
# Streamlit Authentication UI
# ============================================================================

def render_html(html_str: str):
    """Safely render raw HTML in Streamlit using st.markdown with zero-indented lines to prevent code blocks."""
    clean_html = "\n".join(line.strip() for line in html_str.splitlines() if line.strip())
    st.markdown(clean_html, unsafe_allow_html=True)


def render_auth_page():
    """Render the user registration and login interface with a modern fintech split-screen layout."""
    init_session_state()

    # Split-screen columns: Left (Visuals & Analytics Hero), Right (Auth Form Card)
    col_left, col_right = st.columns([1.2, 1], gap="large")

    # =========================================================================
    # LEFT SECTION — FINANCIAL VISUALS & HERO
    # =========================================================================
    with col_left:
        hero_html = """<div class="auth-hero-card" style="background: linear-gradient(135deg, #142B4A 0%, #173660 40%, #1A4479 70%, #205396 100%) !important; border-radius: 20px !important; padding: 34px 30px !important; color: #FFFFFF !important; box-shadow: 0 14px 36px rgba(20, 43, 74, 0.22) !important; border: 1px solid rgba(255, 255, 255, 0.16) !important; position: relative !important; overflow: hidden !important;">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
<span style="background: rgba(255, 255, 255, 0.12); border: 1px solid rgba(255, 255, 255, 0.2); padding: 4px 12px; border-radius: 20px; font-size: 0.75rem; font-weight: 700; color: #93C5FD; letter-spacing: 0.5px; text-transform: uppercase;">
🚀 Corporate Intelligence Platform
</span>
<span style="color: #CBD5E1; font-size: 0.8rem; font-weight: 600;">v1.0 &bull; Indian Rupee Workspace</span>
</div>
<h1 style="color: #FFFFFF !important; font-size: 2.1rem; font-weight: 800; line-height: 1.25; margin: 0 0 10px 0;">
Financial Statement<br/>
<span style="background: linear-gradient(90deg, #38BDF8, #818CF8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
Ratio Analysis
</span> Assistant
</h1>
<p style="color: #E2E8F0 !important; font-size: 1rem; line-height: 1.5; margin: 0 0 22px 0;">
Smarter Financial Decisions Through Intelligent Ratio Analysis.
</p>
<div style="position: relative; width: 100%; height: 260px; background: rgba(10, 25, 47, 0.65); border-radius: 16px; border: 1px solid rgba(255, 255, 255, 0.18); overflow: hidden; margin-bottom: 22px;">
<div style="position: absolute; top: -30px; right: -30px; width: 150px; height: 150px; background: radial-gradient(circle, rgba(19, 168, 158, 0.45) 0%, transparent 70%); border-radius: 50%;"></div>
<div style="position: absolute; bottom: -30px; left: 10px; width: 170px; height: 170px; background: radial-gradient(circle, rgba(40, 120, 208, 0.5) 0%, transparent 70%); border-radius: 50%;"></div>
<svg viewBox="0 0 500 240" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" preserveAspectRatio="none">
<defs>
<linearGradient id="areaGradient" x1="0" y1="0" x2="0" y2="1">
<stop offset="0%" stop-color="#13A89E" stop-opacity="0.5" />
<stop offset="50%" stop-color="#2878D0" stop-opacity="0.2" />
<stop offset="100%" stop-color="#142B4A" stop-opacity="0.0" />
</linearGradient>
<linearGradient id="lineGradient" x1="0" y1="0" x2="1" y2="0">
<stop offset="0%" stop-color="#13A89E" />
<stop offset="50%" stop-color="#38BDF8" />
<stop offset="100%" stop-color="#20A46B" />
</linearGradient>
<linearGradient id="goldGradient" x1="0" y1="0" x2="1" y2="1">
<stop offset="0%" stop-color="#FDE68A" />
<stop offset="50%" stop-color="#F59E0B" />
<stop offset="100%" stop-color="#B45309" />
</linearGradient>
</defs>
<line x1="20" y1="60" x2="480" y2="60" stroke="rgba(255,255,255,0.12)" stroke-dasharray="4,4" />
<line x1="20" y1="120" x2="480" y2="120" stroke="rgba(255,255,255,0.12)" stroke-dasharray="4,4" />
<line x1="20" y1="180" x2="480" y2="180" stroke="rgba(255,255,255,0.12)" stroke-dasharray="4,4" />
<polygon points="30,220 90,190 160,200 230,140 300,160 380,90 440,105 480,45 480,240 30,240" fill="url(#areaGradient)" />
<path d="M 30 220 Q 60 190 90 190 T 160 200 T 230 140 T 300 160 T 380 90 T 440 105 T 480 45" fill="none" stroke="url(#lineGradient)" stroke-width="4.5" stroke-linecap="round" />
<circle cx="90" cy="190" r="5" fill="#38BDF8" />
<circle cx="230" cy="140" r="5" fill="#38BDF8" />
<circle cx="380" cy="90" r="5" fill="#20A46B" />
<circle cx="480" cy="45" r="7" fill="#20A46B" />
<circle cx="480" cy="45" r="14" fill="none" stroke="#20A46B" stroke-width="2" opacity="0.6" />
<g class="anim-coin" transform="translate(65, 75)">
<circle cx="0" cy="0" r="22" fill="#F59E0B" />
<circle cx="0" cy="0" r="22" fill="url(#goldGradient)" />
<circle cx="0" cy="0" r="18" fill="none" stroke="#FEF3C7" stroke-width="1.8" opacity="0.9" />
<text x="0" y="7" font-size="20" font-weight="900" fill="#FFFFFF" text-anchor="middle" font-family="Arial, sans-serif">₹</text>
</g>
<g class="anim-coin" transform="translate(435, 185)">
<circle cx="0" cy="0" r="17" fill="#F59E0B" />
<circle cx="0" cy="0" r="17" fill="url(#goldGradient)" />
<circle cx="0" cy="0" r="14" fill="none" stroke="#FEF3C7" stroke-width="1.4" opacity="0.9" />
<text x="0" y="5" font-size="15" font-weight="900" fill="#FFFFFF" text-anchor="middle" font-family="Arial, sans-serif">₹</text>
</g>
</svg>
<div class="float-metric-card anim-float-1" style="position: absolute; top: 16px; right: 18px; background: rgba(20, 43, 74, 0.88); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.22); border-radius: 12px; padding: 10px 14px; box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);">
<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">
<span style="color: #94A3B8; font-size: 0.7rem; font-weight: 700; text-transform: uppercase;">Turnover</span>
<span style="background: rgba(32, 164, 107, 0.25); color: #4ADE80; padding: 2px 6px; border-radius: 4px; font-size: 0.7rem; font-weight: 700;">▲ +24.8%</span>
</div>
<div style="font-size: 1.15rem; font-weight: 800; color: #FFFFFF; margin-top: 3px;">
₹ 14.85 Cr
</div>
</div>
<div class="float-metric-card anim-float-2" style="position: absolute; bottom: 18px; left: 20px; background: rgba(20, 43, 74, 0.88); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.22); border-radius: 12px; padding: 10px 14px; box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);">
<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">
<span style="color: #94A3B8; font-size: 0.7rem; font-weight: 700; text-transform: uppercase;">Net Profit</span>
<span style="background: rgba(40, 120, 208, 0.25); color: #60A5FA; padding: 2px 6px; border-radius: 4px; font-size: 0.7rem; font-weight: 700;">▲ +18.2%</span>
</div>
<div style="font-size: 1.15rem; font-weight: 800; color: #FFFFFF; margin-top: 3px;">
₹ 2.75 Cr
</div>
</div>
<div class="float-metric-card anim-float-1" style="position: absolute; bottom: 18px; right: 18px; background: rgba(20, 43, 74, 0.88); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.22); border-radius: 12px; padding: 10px 14px; box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);">
<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">
<span style="color: #94A3B8; font-size: 0.7rem; font-weight: 700; text-transform: uppercase;">Health Score</span>
<span style="background: rgba(128, 100, 200, 0.25); color: #C084FC; padding: 2px 6px; border-radius: 4px; font-size: 0.7rem; font-weight: 700;">Strong</span>
</div>
<div style="font-size: 1.15rem; font-weight: 800; color: #FFFFFF; margin-top: 3px;">
94.2 <span style="font-size: 0.75rem; color: #94A3B8;">/ 100</span>
</div>
</div>
</div>
<div style="display: flex; flex-wrap: wrap; gap: 8px;">
<span style="background: rgba(255, 255, 255, 0.12); border: 1px solid rgba(255, 255, 255, 0.2); padding: 6px 14px; border-radius: 20px; font-size: 0.78rem; color: #FFFFFF; font-weight: 500;">
✓ 14 Deterministic Financial Ratios
</span>
<span style="background: rgba(255, 255, 255, 0.12); border: 1px solid rgba(255, 255, 255, 0.2); padding: 6px 14px; border-radius: 20px; font-size: 0.78rem; color: #FFFFFF; font-weight: 500;">
✓ Multi-Year Trends & Peer Radar
</span>
<span style="background: rgba(255, 255, 255, 0.12); border: 1px solid rgba(255, 255, 255, 0.2); padding: 6px 14px; border-radius: 20px; font-size: 0.78rem; color: #FFFFFF; font-weight: 500;">
✓ Executive PDF Reports (ReportLab)
</span>
<span style="background: rgba(255, 255, 255, 0.12); border: 1px solid rgba(255, 255, 255, 0.2); padding: 6px 14px; border-radius: 20px; font-size: 0.78rem; color: #FFFFFF; font-weight: 500;">
✓ PBKDF2 Password Security
</span>
</div>
</div>"""
        render_html(hero_html)

    # =========================================================================
    # RIGHT SECTION — AUTHENTICATION FORM CARD
    # =========================================================================
    with col_right:
        with st.container(border=True):
            tab_login, tab_register = st.tabs(["🔑 Sign In", "📝 Create Account"])

            # -----------------------------------------------------------------
            # TAB 1: LOGIN FORM
            # -----------------------------------------------------------------
            with tab_login:
                welcome_html = """<div style="margin-bottom: 16px;">
<h2 style="color: #142B4A; font-weight: 800; font-size: 1.65rem; margin: 0 0 4px 0;">Welcome Back 👋</h2>
<p style="color: #5A6E85; font-size: 0.92rem; margin: 0;">Enter your credentials to access your financial dashboard.</p>
</div>"""
                render_html(welcome_html)

                with st.form("login_form", clear_on_submit=False):
                    login_email = st.text_input(
                        "Email Address",
                        placeholder="student@example.com",
                        key="login_email_input",
                    )

                    show_pwd = st.checkbox("Show password", key="login_show_pwd")
                    login_password = st.text_input(
                        "Password",
                        type="default" if show_pwd else "password",
                        placeholder="Enter your password",
                        key="login_password_input",
                    )

                    col_rem, col_badge = st.columns([1.2, 1])
                    with col_rem:
                        remember_me = st.checkbox("Remember me", value=True, key="login_remember_me")
                    with col_badge:
                        render_html("<div style='text-align: right; color: #2878D0; font-size: 0.78rem; font-weight: 600; padding-top: 6px;'>🔒 Private SQLite</div>")

                    submitted_login = st.form_submit_button(
                        "Sign In to Workspace 🚀",
                        use_container_width=True,
                        type="primary",
                    )

                    if submitted_login:
                        success, message, user = authenticate_user(login_email, login_password)
                        if success:
                            login_session(user)
                            st.success(f"Welcome back, {user['full_name']}!")
                            st.rerun()
                        else:
                            st.error(f"❌ {message}")

                demo_html = """<div style="background-color: #F8FAFC; border: 1px dashed #CBD5E1; border-radius: 8px; padding: 10px 14px; margin-top: 18px; font-size: 0.8rem; color: #64748B;">
💡 <b>Demo Accounts:</b> <code>rutu522@gmail.com</code> &bull; <code>demo@student.edu</code><br/>
New user? Click the <b>Create Account</b> tab above.
</div>"""
                render_html(demo_html)

            # -----------------------------------------------------------------
            # TAB 2: REGISTRATION FORM
            # -----------------------------------------------------------------
            with tab_register:
                create_html = """<div style="margin-bottom: 16px;">
<h2 style="color: #142B4A; font-weight: 800; font-size: 1.65rem; margin: 0 0 4px 0;">Create Account ✨</h2>
<p style="color: #5A6E85; font-size: 0.92rem; margin: 0;">Get isolated, private access to company ratio analysis.</p>
</div>"""
                render_html(create_html)

                with st.form("register_form", clear_on_submit=False):
                    reg_name = st.text_input(
                        "Full Name",
                        placeholder="e.g. Ramesh Sharma",
                        key="reg_name_input",
                    )
                    reg_email = st.text_input(
                        "Email Address",
                        placeholder="student@example.com",
                        key="reg_email_input",
                    )
                    show_reg_pwd = st.checkbox("Show password", key="reg_show_pwd")
                    reg_password = st.text_input(
                        "Password",
                        type="default" if show_reg_pwd else "password",
                        placeholder="At least 6 characters",
                        help="Password will be securely hashed with PBKDF2-HMAC-SHA256 and salted.",
                        key="reg_password_input",
                    )
                    reg_confirm = st.text_input(
                        "Confirm Password",
                        type="default" if show_reg_pwd else "password",
                        placeholder="Re-enter password",
                        key="reg_confirm_input",
                    )
                    submitted_register = st.form_submit_button(
                        "Create My Account 🎯",
                        use_container_width=True,
                        type="primary",
                    )

                    if submitted_register:
                        success, message = register_user(
                            full_name=reg_name,
                            email=reg_email,
                            password=reg_password,
                            confirm_password=reg_confirm,
                        )
                        if success:
                            st.success(f"✅ {message}")
                            st.info("👉 Switch to the **🔑 Sign In** tab above to sign in.")
                        else:
                            st.error(f"❌ {message}")

                already_html = """<div style="text-align: center; margin-top: 14px; font-size: 0.8rem; color: #64748B;">
Already registered? Switch to the <b>Sign In</b> tab above.
</div>"""
                render_html(already_html)
