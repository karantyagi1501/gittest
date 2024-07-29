import os

# Define the base directory containing multiple folders
BASE_DIR = '/Users/katyagi/Downloads/move2kube-demos-main/samples/enterprise-app/myproject/source'

def update_dockerfile(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        updated = False
        with open(file_path, 'w') as file:
            for line in lines:
                if line.startswith('FROM registry.access.redhat.com/ubi8/python-36'):
                    file.write('FROM docker.local.python\n')
                    updated = True
                else:
                    file.write(line)
        
        if updated:
            print(f"Updated {file_path}")

    except Exception as e:
        print(f"Error updating {file_path}: {e}")

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file == 'Dockerfile':
                file_path = os.path.join(root, file)
                update_dockerfile(file_path)

if __name__ == '__main__':
    # Process each folder in the base directory
    for folder in os.listdir(BASE_DIR):
        folder_path = os.path.join(BASE_DIR, folder)
        if os.path.isdir(folder_path):
            process_directory(folder_path)
    
    print("Update complete.")
