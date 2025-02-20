import os
import subprocess
import platform  # Added to detect OS

# Configuration
REPO_PATH = os.getcwd()  # Set to the current working directory
LAST_COMMIT_FILE = os.path.join(REPO_PATH, "last_commit.txt")  # Store commit hash in current dir
SCRIPT_SH = os.path.join(REPO_PATH, "run_script.sh")  # Bash script
SCRIPT_PS = os.path.join(REPO_PATH, "run_script.ps1")  # PowerShell script

def get_latest_commit():
    """Fetches the latest commit hash using git log."""
    try:
        result = subprocess.run(["git", "-C", REPO_PATH, "log", "-1", "--format=%H"],
                                capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None

def get_stored_commit():
    """Reads the last stored commit hash."""
    if os.path.exists(LAST_COMMIT_FILE):
        with open(LAST_COMMIT_FILE, "r") as file:
            return file.read().strip()
    return None

def update_stored_commit(commit_hash):
    """Updates the stored commit hash."""
    with open(LAST_COMMIT_FILE, "w") as file:
        file.write(commit_hash)

def run_script():
    """Attempts to run the Bash script; falls back to PowerShell if it fails."""
    script_sh_path = SCRIPT_SH.replace("\\", "/")  # Convert Windows path to Unix-compatible format

    if os.path.exists(SCRIPT_SH):
        # Skip chmod on Windows
        if platform.system() != "Windows":
            subprocess.run(["chmod", "+x", script_sh_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        try:
            # Run Bash script
            subprocess.run(["bash", script_sh_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            print("✅ Bash script executed successfully.")
            return True
        except subprocess.CalledProcessError:
            pass  # Do not print failure message yet

    # Try running PowerShell script if Bash script fails
    return run_powershell_script()

def run_powershell_script():
    """Attempts to run the PowerShell script."""
    if os.path.exists(SCRIPT_PS):
        try:
            subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", SCRIPT_PS],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            print("✅ PowerShell script executed successfully.")
            return True
        except subprocess.CalledProcessError:
            pass  # Do not print failure message yet

    return False  # Neither script succeeded

def main():
    latest_commit = get_latest_commit()
    if latest_commit is None:
        return  # Exit if unable to fetch the latest commit

    stored_commit = get_stored_commit()

    if latest_commit and latest_commit != stored_commit:
        print(f"🚀 New commit detected: {latest_commit}")
        success = run_script()
        if not success:
            print("❌ Both scripts failed to execute.")
        else:
            update_stored_commit(latest_commit)
    else:
        print("✅ No new commit detected.")

if __name__ == "__main__":
    main()
