def modify_script(input_file_path, output_file_path):
    try:
        # Open and read the content of the original shell script
        with open(input_file_path, 'r') as file:
            lines = file.readlines()
        
        # Initialize a list to hold the modified lines
        modified_lines = []
        
        # Iterate through each line in the original script
        for line in lines:
            # Change the default CONTAINER_RUNTIME to 'buildah'
            if 'CONTAINER_RUNTIME=podman' in line:
                line = line.replace('podman', 'buildah')
            
            # Update the condition to check only for 'buildah'
            if '[ "${CONTAINER_RUNTIME}" != "docker" ] && [ "${CONTAINER_RUNTIME}" != "podman" ]' in line:
                line = 'if [ "${CONTAINER_RUNTIME}" != "buildah" ]; then\n'
            
            # Append ':v1.0.0' to each tag and push command
            if 'tag ' in line or 'push ' in line:
                parts = line.split()
                # Modify the part to include the version
                parts[-1] = parts[-1].split(':')[0] + ':v1.0.0'
                line = ' '.join(parts) + '\n'
            
            # Append the modified line to the list
            modified_lines.append(line)
        
        # Write the modified lines to a new file
        with open(output_file_path, 'w') as file:
            file.writelines(modified_lines)
        
        # Print success message with the output file path
        print("Script modified successfully and saved to:", output_file_path)
    except Exception as e:
        # Print any errors encountered during the process
        print("An error occurred while modifying the script:", str(e))

# Example usage of the function
if __name__ == "__main__":
    # Define the path to the input shell script
    input_script_path = 'pushimages.sh'
    # Define the path to save the modified shell script
    output_script_path = 'updatedpush.sh'
    # Call the function with the specified paths
    modify_script(input_script_path, output_script_path)