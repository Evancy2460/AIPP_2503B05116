import json
import os
import base64
import secrets
import hmac
from hashlib import pbkdf2_hmac
from getpass import getpass
import sys
import argparse


USERS_FILE = "users.json"
DEFAULT_PBKDF2_ITERATIONS = 150_000


def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    try:
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, dict):
                return data
            return {}
    except (json.JSONDecodeError, OSError):
        return {}


def save_users(users):
    try:
        with open(USERS_FILE, "w", encoding="utf-8") as f:
            json.dump(users, f, indent=2)
    except OSError as exc:
        print(f"Error saving users: {exc}")


def hash_password(password, salt=None, iterations=DEFAULT_PBKDF2_ITERATIONS):
    if salt is None:
        salt = secrets.token_bytes(16)
    if isinstance(salt, str):
        salt = base64.b64decode(salt.encode("utf-8"))
    dk = pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iterations, dklen=32)
    return {
        "salt": base64.b64encode(salt).decode("utf-8"),
        "hash": base64.b64encode(dk).decode("utf-8"),
        "iterations": iterations,
        "algorithm": "pbkdf2_sha256",
    }


def verify_password(password, record):
    try:
        salt_b64 = record["salt"]
        hash_b64 = record["hash"]
        iterations = int(record.get("iterations", DEFAULT_PBKDF2_ITERATIONS))
        algorithm = record.get("algorithm", "pbkdf2_sha256")
        if algorithm != "pbkdf2_sha256":
            return False
        salt = base64.b64decode(salt_b64.encode("utf-8"))
        expected = base64.b64decode(hash_b64.encode("utf-8"))
        computed = pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iterations, dklen=32)
        return hmac.compare_digest(computed, expected)
    except Exception:
        return False


def prompt_password(prompt_text):
    """
    Password input with masking:
    - If --visible (or env forces), characters are shown plainly.
    - Otherwise, show '*' for each typed character on supported terminals.
    - Falls back to hidden or visible input if masking isn't supported.
    """
    global VISIBLE_INPUT
    # If user forced visibility or we're not in a TTY (e.g., some IDE consoles), use visible input
    if VISIBLE_INPUT or not (sys.stdin.isatty() and sys.stdout.isatty()):
        if not VISIBLE_INPUT:
            print("Note: Masked input not supported here; password will be visible as you type.")
        return input(prompt_text)

    # Try Windows masked input using msvcrt
    try:
        import msvcrt

        print(prompt_text, end="", flush=True)
        chars = []
        while True:
            ch = msvcrt.getwch()
            if ch in ("\r", "\n"):
                print()
                break
            if ch == "\003":  # Ctrl+C
                raise KeyboardInterrupt
            if ch == "\b":  # Backspace
                if chars:
                    chars.pop()
                    # erase last '*'
                    print("\b \b", end="", flush=True)
                continue
            if ch in ("\x00", "\xe0"):  # Special keys (arrows, etc.); consume next
                _ = msvcrt.getwch()
                continue
            chars.append(ch)
            print("*", end="", flush=True)
        return "".join(chars)
    except ImportError:
        # Non-Windows: try hidden input; if that fails, fallback to visible
        try:
            return getpass(prompt_text)
        except Exception:
            print("Note: Masked input not supported here; password will be visible as you type.")
            return input(prompt_text)


def register_user():
    users = load_users()
    username = input("Choose a username: ").strip()
    if not username:
        print("Username cannot be empty.")
        return
    if username in users:
        print("Username already exists. Try a different one.")
        return
    while True:
        password = prompt_password("Choose a password: ")
        confirm = prompt_password("Confirm password: ")
        if password != confirm:
            print("Passwords do not match. Try again.")
            continue
        if len(password) < 8:
            print("Password must be at least 8 characters.")
            continue
        break
    users[username] = hash_password(password)
    save_users(users)
    print(f"User '{username}' registered successfully.")


def login_user():
    users = load_users()
    username = input("Username: ").strip()
    if username not in users:
        print("Invalid username or password.")
        return
    password = prompt_password("Password: ")
    if verify_password(password, users[username]):
        print(f"Login successful. Welcome, {username}!")
    else:
        print("Invalid username or password.")


def list_users():
    users = load_users()
    usernames = sorted(users.keys())
    if not usernames:
        print("No users found.")
        return
    print(f"Users ({len(usernames)}):")
    for name in usernames:
        print(f" - {name}")


def delete_user():
    users = load_users()
    username = input("Username to delete: ").strip()
    if username not in users:
        print("User not found.")
        return
    print("To confirm deletion, enter the user's password.")
    password = prompt_password("Password: ")
    if not verify_password(password, users[username]):
        print("Password incorrect. Deletion cancelled.")
        return
    confirm = input(f"Type DELETE to confirm removing '{username}': ").strip()
    if confirm != "DELETE":
        print("Confirmation not entered. Deletion cancelled.")
        return
    del users[username]
    save_users(users)
    print(f"User '{username}' deleted.")


def main():
    parser = argparse.ArgumentParser(description="Simple Login System (local JSON storage)")
    parser.add_argument("--visible", action="store_true", help="Force visible password input (no masking)")
    args = parser.parse_args()

    global VISIBLE_INPUT
    VISIBLE_INPUT = bool(args.visible or os.getenv("VISIBLE_PASSWORD") == "1")

    banner_suffix = " [visible password]" if VISIBLE_INPUT or not (sys.stdin.isatty() and sys.stdout.isatty()) else ""
    print(f"Simple Login System (local JSON storage){banner_suffix}")
    while True:
        print("\nMenu:")
        print("  1) Register")
        print("  2) Login")
        print("  3) List users")
        print("  4) Delete user")
        print("  5) Exit")
        choice = input("Select an option (1-5): ").strip()
        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            list_users()
        elif choice == "4":
            delete_user()
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()

