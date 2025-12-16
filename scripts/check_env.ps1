Write-Output "--- ENVIRONMENT CHECK STARTING ---"

# 1. Check if we can see Python
python --version

# 2. If the previous command worked, say success
if ($LASTEXITCODE -eq 0) {
    Write-Output "SUCCESS: Python is installed and ready."
} else {
    Write-Error "CRITICAL ERROR: Python is missing!"
    exit 1
}
