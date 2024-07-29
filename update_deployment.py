import sys
import yaml
import glob
import os

def update_files(version_tag):
    # Predefined directory path for YAML files
    directory = '../yamls/'  # Modify this path as necessary
    # Patterns to match files
    deployment_pattern = os.path.join(directory, '*-deployment.yaml')
    route_pattern = os.path.join(directory, '*-route.yaml')

    # Update deployment files
    deployment_files = glob.glob(deployment_pattern)
    for file_name in deployment_files:
        try:
            with open(file_name, 'r') as file:
                data = yaml.safe_load(file)

            containers = data['spec']['template']['spec']['containers']
            for container in containers:
                image = container['image']
                if 'latest' in image:
                    new_image = ':'.join(image.split(':')[:-1] + [version_tag])
                    container['image'] = new_image

            with open(file_name, 'w') as file:
                yaml.safe_dump(data, file)

            print(f"Updated image version in file: {file_name}")
        except Exception as e:
            print(f"Failed to update {file_name}: {str(e)}")

    # Remove host and path from route files
    route_files = glob.glob(route_pattern)
    for file_name in route_files:
        try:
            with open(file_name, 'r') as file:
                data = yaml.safe_load(file)

            if 'spec' in data:
                if 'host' in data['spec']:
                    del data['spec']['host']
                if 'path' in data['spec']:
                    del data['spec']['path']

            with open(file_name, 'w') as file:
                yaml.safe_dump(data, file, default_flow_style=False)

            print(f"Removed host and path from: {file_name}")
        except Exception as e:
            print(f"Failed to update {file_name}: {str(e)}")

# Example usage of the function
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 update_files.py <version_tag>")
    else:
        version_tag = sys.argv[1]
        update_files(version_tag)
