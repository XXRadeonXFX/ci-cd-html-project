# CI/CD HTML Project

This project demonstrates a Continuous Integration and Continuous Deployment (CI/CD) pipeline for a simple HTML application. It includes scripts to automate the deployment process and monitor the repository for changes.

## Project Structure

- **index.html**: The main HTML file for the web application.
- **commit_checker.py**: A Python script that checks for new commits in the repository.
- **last_commit.txt**: Stores the hash of the last processed commit.
- **run_script.sh**: A shell script that runs the `commit_checker.py` script.
- **run_script.ps1**: A PowerShell script that runs the `commit_checker.py` script.
- **index.html.bak**: A backup of the `index.html` file.

## Prerequisites

- **Python 3.x**: Ensure Python is installed on your system.
- **Git**: Required for repository operations.

## Setup and Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/XXRadeonXFX/ci-cd-html-project.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd ci-cd-html-project
   ```

3. **Install Required Python Packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Repository URL**:
   Update the `repo_url` variable in `commit_checker.py` with your repository's URL.

5. **Run the Commit Checker Script**:
   - **For Unix-based Systems**:
     ```bash
     ./run_script.sh
     ```
   - **For Windows Systems**:
     ```powershell
     ./run_script.ps1
     ```

   These scripts will execute `commit_checker.py`, which monitors the repository for new commits and triggers the deployment process accordingly.

## Deployment Process

The `commit_checker.py` script performs the following steps:

1. Checks for new commits in the repository.
2. If a new commit is detected, it pulls the latest changes.
3. Triggers the deployment process to update the live application.

## Notes

- Ensure that the scripts have the necessary execution permissions. For Unix-based systems, you may need to run `chmod +x run_script.sh`.
- Customize the deployment steps within `commit_checker.py` to fit your specific requirements.

## License

This project is licensed under the [MIT License](LICENSE).
