import os
import logging
import sys

# 1. SETUP LOGGING (The "Clear Logging" requirement)
# This makes logs look like: "2023-10-27 10:00:00 - INFO - Starting build..."
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def main():
    logging.info("--- STARTING AUTOMATION SCRIPT ---")

    output_folder = "artifact_folder"
    file_name = "my_software_build.txt"
    file_path = os.path.join(output_folder, file_name)

    # 2. ERROR HANDLING (The "Reliability" requirement)
    try:
        # Step A: Check/Create Folder
        if not os.path.exists(output_folder):
            logging.info(f"Folder '{output_folder}' not found. Creating it...")
            os.makedirs(output_folder)
        else:
            logging.info(f"Folder '{output_folder}' already exists.")

        # Step B: Write the file
        logging.info(f"Attempting to write file: {file_path}")
        
        with open(file_path, "w") as f:
            f.write("Build Version: 2.0.0 (Enhanced)\n")
            f.write("Status: Stable\n")
            f.write("Logs: Active\n")
        
        logging.info("File written successfully.")

    except Exception as e:
        # This block only runs if something crashes
        logging.error(f"CRITICAL FAILURE: {e}")
        # We force the script to exit with an error code so the pipeline turns Red
        sys.exit(1)

    logging.info("--- PROCESS FINISHED SUCCESSFULLY ---")

if __name__ == "__main__":
    main()
