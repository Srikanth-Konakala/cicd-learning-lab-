import os

# Define the folder name
output_folder = "artifact_folder"

# Safety Check: Create the folder if it doesn't exist yet
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"Created missing folder: {output_folder}")

# Define the file path
file_path = os.path.join(output_folder, "my_software_build.txt")

# Create the file
with open(file_path, "w") as f:
    f.write("--------------------------------\n")
    f.write("BUILD SUCCESSFUL\n")
    f.write("Version: 1.0.0\n")
    f.write("Checked by: PowerShell\n")
    f.write("--------------------------------\n")

print(f"Success! Created artifact at: {file_path}")
