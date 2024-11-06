import threading
import time
import os

files = []
path = r"C:\Users\igeon\Desktop\Folder"

def filesChecking():
    while True:
        print("Daemon Service: Checking ...")
        global files
        temp_files = []
        all_files = os.listdir(path)
        
        # Check for newly added files
        for file in all_files:
            if file not in files:
                temp_files.append(file)
        
        # If new files are found, add them to the list and print a message
        if temp_files:
            print("Daemon Service: The following files are newly added...")
            print(temp_files)
            files.extend(temp_files)  # Add new files to the tracked list
            print("Backup Done Successfully")
        
        time.sleep(5)  # Check every 5 seconds

def addFile():
    global path
    # Ask for the file name from the user
    file_name = input("Enter the file name (with extension): ")
    
    # Combine the folder path and the file name
    full_path = os.path.join(path, file_name)
    
    # Create and write to the file
    with open(full_path, "w") as file:
        file.write("Hello")
    
    print(f"File '{file_name}' has been created at '{path}'")

# Start the daemon thread to monitor the folder
t1 = threading.Thread(target=filesChecking, daemon=True)
t1.start()

# Main program loop
while True:
    print("Do you want to create a new file? (y/n): ")
    ip = input().strip()
    if ip.lower() == 'y':
        addFile()
    elif ip.lower() == 'n':
        print("Waiting... (type 'y' to create a file, or 'n' to continue waiting)")
        time.sleep(10)  # Main loop delay when no action is taken
    else:
        print("Invalid Input!")
