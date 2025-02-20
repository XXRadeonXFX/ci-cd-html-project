import os
import subprocess
import platform

# Configuration
REPO_PATH = os.getcwd()  # Get the current working directory
LAST_COMMIT_FILE = os.path.join(REPO_PATH, "last_commit.txt")  # File to store the last commit hash
SCRIPT_SH = os.path.join(REPO_PATH, "run_script.sh")  # Bash script path
SCRIPT_PS = os.path.join(REPO_PATH, "run_script.ps1")  # PowerShell script path

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

def is_wsl():
    """Detect if running inside WSL."""
    return "microsoft" in platform.uname().release.lower()

def run_script():
    """Runs the appropriate script based on the environment (WSL or Windows)."""
    if is_wsl():
        return run_bash_script()
    else:
        return run_powershell_script()

def run_bash_script():
    """Runs the Bash script inside WSL."""
    if os.path.exists(SCRIPT_SH):
        try:
            subprocess.run(["chmod", "+x", SCRIPT_SH], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run(["/bin/bash", SCRIPT_SH], check=True)
            print("✅ Bash script executed successfully.")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Bash script failed: {e}")
            return False
    else:
        print("❌ Bash script not found.")
        return False

def run_powershell_script():
    """Runs the PowerShell script in Windows."""
    powershell_cmd = "pwsh" if shutil.which("pwsh") else "powershell"

    if os.path.exists(SCRIPT_PS):
        try:
            subprocess.run([powershell_cmd, "-ExecutionPolicy", "Bypass", "-File", SCRIPT_PS],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            print("✅ PowerShell script executed successfully.")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ PowerShell script failed: {e}")
            return False
    else:
        print("❌ PowerShell script not found.")
        return False

def main():
    """Main execution logic."""
    latest_commit = get_latest_commit()
    if latest_commit is None:
        print("❌ Failed to fetch latest commit.")
        return

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
