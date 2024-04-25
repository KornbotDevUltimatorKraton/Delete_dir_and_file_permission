import shutil
import subprocess
import getpass

def delete_folder_with_password(folder_path):
    # Get password securely
    #password = getpass.getpass("Enter your password: ")

    # Construct the command to delete the folder with sudo
    command = f"echo {'Rklc3548@##'} | sudo -S rm -rf {folder_path}"

    try:
        # Execute the command with sudo
        subprocess.run(command, shell=True, check=True)
        print("Folder deleted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print("Failed to delete the folder with sudo.")

# Specify the path of the folder to be deleted
folder_path = '/home/kornbotdev/Test_deletedir'

# Call the function to delete the folder with password permission
delete_folder_with_password(folder_path)
