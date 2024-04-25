import os
import subprocess


def delete_file_with_password(file_path):
    # Get password securely
   

    # Construct the command to delete the file with sudo
    command = f"echo {'Rccsseere'} | sudo -S rm -f {file_path}"

    try:
        # Execute the command with sudo
        subprocess.run(command, shell=True, check=True)
        print("File deleted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print("Failed to delete the file with sudo.")

# Specify the path of the file to be deleted
file_path = '/home/kornbotdev/file.txt'

# Call the function to delete the file with password permission
delete_file_with_password(file_path)
