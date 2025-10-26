# Jenkins Pipeline Project

## Overview
This project demonstrates a complete CI/CD pipeline using Jenkins, Python, and GitHub. The pipeline automates the process of checking out code, building the environment, testing, and deploying the application.

## Project Structure
\\\
simple-pipeline/
├── app.py                 # Python application with utility functions
├── test_app.py            # Unit tests for the application
 requirements.txt       # Python dependencies
 Jenkinsfile            # Jenkins pipeline configuration
 README.md              # This file
\\\

## Pipeline Stages

### 1. **Checkout**
- **What it does:** Clones the source code from the GitHub repository to the Jenkins workspace
- **Why it matters:** Ensures Jenkins has the latest code to work with
- **Command:** \git clone https://github.com/FranklinChinonso/Jenkins-pipeline.git\

### 2. **Build**
- **What it does:** Sets up the Python environment and installs all required dependencies
- **Why it matters:** Prepares the environment with necessary packages before testing
- **Commands:**
  - \python -m pip install --upgrade pip\ - Updates pip package manager
  - \pip install -r requirements.txt\ - Installs project dependencies

### 3. **Test**
- **What it does:** Executes all unit tests to verify the application functions correctly
- **Why it matters:** Catches bugs early and ensures code quality before deployment
- **Command:** \pytest test_app.py -v\ - Runs tests in verbose mode

### 4. **Deploy**
- **What it does:** Simulates deployment by running the Python application and displaying output
- **Why it matters:** Verifies the application runs successfully in the deployed environment
- **Command:** \python app.py\ - Executes the main application

## How to Run

### Local Testing
\\\ash
pip install -r requirements.txt
pytest test_app.py -v
python app.py
\\\

### Jenkins Pipeline
1. Jenkins automatically triggers the pipeline when changes are pushed to GitHub
2. All 4 stages execute sequentially
3. If any stage fails, the build stops and reports the error
4. On success, a green checkmark appears in Jenkins UI

## Technologies Used
- **Jenkins** - CI/CD orchestration platform
- **Python** - Application and test framework
- **Git/GitHub** - Version control and repository hosting
- **Pytest** - Testing framework
