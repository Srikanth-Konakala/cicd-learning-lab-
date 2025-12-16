# cicd-learning-lab-
# CI/CD Automation & Pipeline Optimization

## Project Overview
This project implements a fully automated CI/CD pipeline using **GitHub Actions**, **Python**, and **PowerShell**. It automates the build lifecycle including environment validation, workspace preparation, artifact generation, and secure storage.

## Key Features
* **Automated Workflow:** Orchestrates the build process from code commit to artifact generation.
* **Environment Validation:** Uses **PowerShell** to ensure runtimes (Python) are installed before execution.
* **Resilient Scripting:** Python scripts include robust `try/except` error handling and automated cleanup routines.
* **Observability:** Implements timestamped logging for rapid troubleshooting.
* **Artifact Management:** Automatically archives build outputs for deployment.

## Pipeline Architecture
The pipeline follows a strict linear flow:
1.  **Checkout Code:** Pulls the latest version from GitHub.
2.  **Environment Check (PowerShell):** Verifies system dependencies.
3.  **Preparation (Python):** Cleans old artifacts and creates a fresh workspace.
4.  **Build Execution (Python):** Generates the software build with versioning.
5.  **Artifact Upload:** Saves the final result as a downloadable ZIP.

## Technology Stack
* **CI Engine:** GitHub Actions (YAML)
* **Scripting:** Python 3.x, PowerShell Core
* **OS:** Ubuntu Linux (Latest)

## How to Run
1.  Commit changes to the `main` branch.
2.  Navigate to the **Actions** tab to view live logs.
3.  Download the `my-final-software` zip from the Artifacts section upon success.
