import os

# The folder we created in prep.py
output_folder = "artifact_folder"

# The name of our "software" file
file_path = os.path.join(output_folder, "my_software_build.txt")

# Create the file and write some text into it
with open(file_path, "w") as f:
    f.write("--------------------------------\n")
    f.write("BUILD SUCCESSFUL\n")
    f.write("Version: 1.0.0\n")
    f.write("Checked by: PowerShell\n")
    f.write("--------------------------------\n")

print(f"Success! Created artifact at: {file_path}")
