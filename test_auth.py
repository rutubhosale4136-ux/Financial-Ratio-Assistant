"""Comprehensive test suite for authentication.py and database integration."""

import os
import tempfile
import sqlite3
from pathlib import Path
import database
import authentication


def run_all_tests():
    print("=" * 60)
    print("RUNNING AUTHENTICATION & REGISTRATION TESTS")
    print("=" * 60)

    # 1. PBKDF2 Password Hashing Tests
    print("\n[Test 1] PBKDF2 Hashing and Verification")
    pwd = "SecureStudentPass@123"
    hash1, salt1 = authentication.hash_password(pwd)
    assert len(salt1) == 32, f"Expected 32 hex chars for salt, got {len(salt1)}"
    assert len(hash1) == 64, f"Expected 64 hex chars for SHA256 hash, got {len(hash1)}"
    assert hash1 != pwd, "Plaintext password must not equal hash!"

    # Verify correct password
    assert authentication.verify_password(pwd, hash1, salt1) is True, "Password verification failed for correct password!"

    # Verify wrong password
    assert authentication.verify_password("WrongPassword!", hash1, salt1) is False, "Verification accepted wrong password!"

    # Verify salt uniqueness
    hash2, salt2 = authentication.hash_password(pwd)
    assert salt1 != salt2, "Two generated salts must be unique!"
    assert hash1 != hash2, "Hashes with different salts must differ!"
    print("  --> PBKDF2 password hashing & verification PASSED.")

    # 2. Input Validation Tests
    print("\n[Test 2] Input Validation")
    # Empty name
    ok, msg = authentication.validate_registration_inputs("", "test@example.com", "pass123", "pass123")
    assert not ok and "Full name" in msg, f"Failed empty name check: {msg}"

    # Invalid email
    ok, msg = authentication.validate_registration_inputs("Ramesh Sharma", "notanemail", "pass123", "pass123")
    assert not ok and "valid email" in msg, f"Failed invalid email check: {msg}"

    # Password too short (< 6 chars)
    ok, msg = authentication.validate_registration_inputs("Ramesh Sharma", "ramesh@example.com", "12345", "12345")
    assert not ok and "at least 6 characters" in msg, f"Failed short password check: {msg}"

    # Password mismatch
    ok, msg = authentication.validate_registration_inputs("Ramesh Sharma", "ramesh@example.com", "password123", "password456")
    assert not ok and "do not match" in msg, f"Failed password mismatch check: {msg}"

    # Valid inputs
    ok, msg = authentication.validate_registration_inputs("Ramesh Sharma", "ramesh@example.com", "pass123", "pass123")
    assert ok, f"Valid registration failed validation: {msg}"
    print("  --> Input validation PASSED.")

    # 3. Registration, Duplicate Email Prevention, and DB Persistence
    print("\n[Test 3] Registration and Database Persistence (Isolated Test DB)")
    temp_dir = tempfile.mkdtemp()
    temp_db = Path(temp_dir) / "test_auth.db"
    database.init_db(temp_db)

    # Register first user
    ok, msg = authentication.register_user(
        "Asha Rao", "asha.rao@college.edu", "AshaPass2026", "AshaPass2026", db_path=temp_db
    )
    assert ok is True, f"Registration failed: {msg}"
    print("  --> User 1 registered successfully.")

    # Verify in DB
    user_record = database.get_user_by_email("asha.rao@college.edu", db_path=temp_db)
    assert user_record is not None, "User record not found in database!"
    assert user_record["full_name"] == "Asha Rao"
    assert user_record["email"] == "asha.rao@college.edu"
    assert "AshaPass2026" not in user_record["password_hash"], "Plaintext password found in database!"
    assert len(user_record["password_salt"]) == 32
    print("  --> User verified in SQLite database (plain-text password NOT stored).")

    # Duplicate email registration attempt (identical)
    ok, msg = authentication.register_user(
        "Asha Duplicate", "asha.rao@college.edu", "AnotherPass123", "AnotherPass123", db_path=temp_db
    )
    assert ok is False, "Duplicate email registration was erroneously allowed!"
    assert "already exists" in msg, f"Unexpected duplicate email message: {msg}"

    # Duplicate email registration attempt (different case: ASHA.RAO@COLLEGE.EDU)
    ok, msg = authentication.register_user(
        "Asha Uppercase", "ASHA.RAO@COLLEGE.EDU", "AnotherPass123", "AnotherPass123", db_path=temp_db
    )
    assert ok is False, "Duplicate uppercase email registration was erroneously allowed!"
    assert "already exists" in msg, f"Unexpected uppercase duplicate email message: {msg}"
    print("  --> Duplicate email prevention PASSED.")

    # 4. User Login and Authentication Tests
    print("\n[Test 4] User Login & Authentication")
    # Successful login
    ok, msg, safe_user = authentication.authenticate_user("asha.rao@college.edu", "AshaPass2026", db_path=temp_db)
    assert ok is True, f"Login failed for valid credentials: {msg}"
    assert safe_user["id"] == user_record["id"]
    assert safe_user["full_name"] == "Asha Rao"
    assert safe_user["email"] == "asha.rao@college.edu"
    assert "password_hash" not in safe_user, "password_hash leaked in safe_user object!"
    assert "password_salt" not in safe_user, "password_salt leaked in safe_user object!"
    print("  --> Valid login succeeded with safe user dictionary.")

    # Wrong password login
    ok, msg, bad_user = authentication.authenticate_user("asha.rao@college.edu", "WrongPassword", db_path=temp_db)
    assert ok is False, "Login succeeded with wrong password!"
    assert bad_user is None
    assert "Invalid email or password" in msg

    # Non-existent email login
    ok, msg, bad_user = authentication.authenticate_user("nobody@college.edu", "SomePassword", db_path=temp_db)
    assert ok is False, "Login succeeded with non-existent email!"
    assert bad_user is None
    assert "Invalid email or password" in msg
    print("  --> Invalid credentials handling PASSED.")

    # 5. User Data Isolation Verification
    print("\n[Test 5] User-Specific Data Isolation")
    # Register second user
    ok, msg = authentication.register_user(
        "Rohan Gupta", "rohan@college.edu", "RohanPass2026", "RohanPass2026", db_path=temp_db
    )
    assert ok is True
    ok, _, user2 = authentication.authenticate_user("rohan@college.edu", "RohanPass2026", db_path=temp_db)

    # User 1 creates a company
    c_id = database.create_company(
        user_id=safe_user["id"],
        company_name="Asha Tech Ltd",
        industry="Technology",
        financial_year="FY 2025-26",
        db_path=temp_db,
    )
    assert c_id > 0

    # User 1 dashboard summary
    summary1 = database.dashboard_summary(safe_user["id"], db_path=temp_db)
    assert summary1["total_companies"] == 1, f"Expected 1 company for User 1, got {summary1['total_companies']}"

    # User 2 dashboard summary (must be 0)
    summary2 = database.dashboard_summary(user2["id"], db_path=temp_db)
    assert summary2["total_companies"] == 0, f"Expected 0 companies for User 2, got {summary2['total_companies']}"

    # User 2 cannot list User 1's companies
    user2_companies = database.list_companies(user2["id"], db_path=temp_db)
    assert len(user2_companies) == 0, f"User 2 can see companies: {user2_companies}"
    print("  --> User-specific data isolation PASSED.")

    # 6. Session Management Simulation
    print("\n[Test 6] Session Management & Logout Simulation")
    import unittest.mock as mock

    # Mock st.session_state
    fake_session = {}
    with mock.patch.object(authentication.st, "session_state", fake_session):
        authentication.init_session_state()
        assert authentication.is_authenticated() is False
        assert authentication.get_current_user() is None
        assert authentication.get_current_user_id() is None

        # Simulate login
        dummy_user = {"id": 42, "full_name": "Test Student", "email": "test@student.edu"}
        authentication.login_session(dummy_user)
        assert authentication.is_authenticated() is True
        assert authentication.get_current_user()["id"] == 42
        assert authentication.get_current_user_id() == 42

        # Simulate logout (mocking st.rerun to prevent exception)
        with mock.patch.object(authentication.st, "rerun"):
            authentication.logout()
            assert authentication.is_authenticated() is False
            assert authentication.get_current_user() is None
            assert authentication.get_current_user_id() is None
    print("  --> Session state initialization, login, and logout PASSED.")

    # 7. Persistence After Restart Simulation
    print("\n[Test 7] Persistence After Application Restart")
    # Simulate completely closing connection and re-opening the file as a new app instance
    del user_record
    del safe_user
    del user2

    # Fresh lookup from disk
    persisted_user = database.get_user_by_email("asha.rao@college.edu", db_path=temp_db)
    assert persisted_user is not None, "User not found after simulated application restart!"
    assert persisted_user["full_name"] == "Asha Rao"

    # Authenticate on the reopened database
    reopened_login_ok, _, reopened_user = authentication.authenticate_user(
        "asha.rao@college.edu", "AshaPass2026", db_path=temp_db
    )
    assert reopened_login_ok is True, "Login failed after simulated application restart!"
    assert reopened_user["email"] == "asha.rao@college.edu"

    # Verify user's company persisted
    persisted_companies = database.list_companies(reopened_user["id"], db_path=temp_db)
    assert len(persisted_companies) == 1, "User's company data did not persist after restart!"
    assert persisted_companies[0]["company_name"] == "Asha Tech Ltd"
    print("  --> Persistence across restart verified (accounts, hashes, and relational data intact).")

    # Clean up temp file
    try:
        os.remove(temp_db)
        os.rmdir(temp_dir)
    except Exception:
        pass

    print("\n" + "=" * 60)
    print("ALL 7 TEST SUITES PASSED! (100% SUCCESS)")
    print("=" * 60)


if __name__ == "__main__":
    run_all_tests()
