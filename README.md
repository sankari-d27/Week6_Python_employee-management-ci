Employee Management System with CI/CD Integration
1. Project Introduction

The Employee Management System is an intermediate-level Python project developed to demonstrate Continuous Integration (CI) using GitHub Actions.

The application allows users to manage employee records using a SQLite database. It supports adding, viewing, searching, updating, and deleting employee information.

The project integrates automated testing and code linting to maintain software quality.

2. Technologies Used
Python 3.11
SQLite
Pytest
Flake8
Pytest HTML
Git and GitHub
GitHub Actions
3. Project Features
Add employee records.
View all employees.
Search employees using employee ID.
Update employee information.
Delete employee records.
Validate employee information.
Store employee details in SQLite.
4. Project Structure
text
employee-management-ci/
├── employee_management/
│   ├── __init__.py
│   ├── database.py
│   └── employee.py
├── tests/
│   ├── __init__.py
│   └── test_employee.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── reports/
├── main.py
├── requirements.txt
├── pytest.ini
├── .flake8
├── .gitignore
└── README.md

5. Installation Instructions
Step 1: Install Python

Install Python 3.11 or later.

Verify installation:

bash
python --version

Step 2: Clone the repository
bash
git clone YOUR_GITHUB_REPOSITORY_URL

Step 3: Navigate to the project
bash
cd employee-management-ci

Step 4: Create a virtual environment
bash
python -m venv .venv


Activate it on Windows:

bash
.venv\Scripts\activate


Activate it on Linux/macOS:

bash
source .venv/bin/activate

Step 5: Install dependencies
bash
pip install -r requirements.txt

6. Running the Application

Execute:

bash
python main.py


Select an option from the menu to manage employee information.

7. Running Automated Tests

Execute:

bash
pytest -v


The test suite checks employee creation, retrieval, updating, deletion, validation, and duplicate email handling.

8. Running Code Linting

Execute:

bash
flake8 employee_management tests main.py


Flake8 checks the Python source files for coding style issues and common errors.

9. Generating an HTML Test Report

Execute:

bash
pytest --html=reports/test-report.html --self-contained-html


Open the generated HTML file in a browser to view the test results.

10. Continuous Integration Configuration

The project uses GitHub Actions for Continuous Integration.

Configuration file:

.github/workflows/ci.yml

The pipeline performs these operations:

Checks out the GitHub repository.
Sets up Python 3.11.
Installs project dependencies.
Runs Flake8 code linting.
Executes automated tests using Pytest.
Generates an HTML test report.
Uploads the report as a GitHub Actions artifact.

The workflow runs automatically on pushes and pull requests targeting the main or master branch. It can also be started manually.

If linting or testing fails, the CI job is marked as failed.

11. How to Trigger the CI Pipeline

First, configure your GitHub repository.

Push the project files:

bash
git init
git add .
git commit -m "Initial project with CI integration"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main


Whenever you push new changes:

bash
git add .
git commit -m "Update employee management system"
git push origin main


GitHub Actions automatically starts the CI pipeline.

12. Viewing CI Logs
Open your GitHub repository.
Click the Actions tab.
Select Employee Management CI Pipeline.
Open the latest workflow run.
Select the Build and Test job.
View the logs for each step.

A green check indicates success, while a red cross indicates failure.

13. Downloading Test Reports
Open the completed workflow run.
Scroll to the Artifacts section.
Download pytest-html-report.
Extract the downloaded ZIP file.
Open test-report.html in a browser.
14. Challenges Encountered

Some challenges during CI integration include:

Dependency installation issues: Resolved by maintaining a requirements.txt file.
Database isolation: Resolved by using separate temporary databases for automated tests.
Python environment differences: Resolved by specifying Python 3.11 in GitHub Actions.
Code quality errors: Resolved by configuring Flake8.
Test report generation: Resolved by integrating pytest-html.
Pipeline failures: Resolved by checking individual GitHub Actions logs.
15. Final Verification

The CI pipeline should be verified by pushing a small code change to GitHub.

After pushing:

Open the Actions tab.
Confirm that a new workflow run starts.
Check that linting completes successfully.
Check that all automated tests pass.
Confirm that the HTML report is uploaded.

Capture a screenshot of the successful workflow and include it in the final submission.

16. Conclusion

This project demonstrates how Continuous Integration improves software development workflows.

GitHub Actions automates code linting, testing, and report generation whenever changes are pushed to the repository.

The integration helps detect errors early, improves code quality, and provides a repeatable development environment.

The project demonstrates practical CI/CD principles used in professional software development.