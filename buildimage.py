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
            
            # Update the build command from 'build' to 'bud'
            if '${CONTAINER_RUNTIME} build ' in line:
                line = line.replace('${CONTAINER_RUNTIME} build ', '${CONTAINER_RUNTIME} bud ')
            
            # Update the condition to check only for 'buildah'
            if '[ "${CONTAINER_RUNTIME}" != "docker" ] && [ "${CONTAINER_RUNTIME}" != "podman" ]' in line:
                line = 'if [ "${CONTAINER_RUNTIME}" != "buildah" ]; then\n'
            
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
    input_script_path = 'buildimages.sh'
    # Define the path to save the modified shell script
    output_script_path = 'updatedbuild1.sh'
    # Call the function with the specified paths
    modify_script(input_script_path, output_script_path)
