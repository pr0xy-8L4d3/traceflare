import os

# Ask for the API key
api_key = input("Please enter your SecurityTrails API key: ")

# Path to the TraceFlare script
traceflare_path = "traceflare.py"

# Check if the file exists
if os.path.exists(traceflare_path):
    # Open the file for reading and modifying
    with open(traceflare_path, 'r') as file:
        file_data = file.readlines()

    # Replace the line containing the API key placeholder
    for i, line in enumerate(file_data):
        if line.strip().startswith('api_key = "your_api_key_here"'):
            # Maintain the original indentation and replace the line
            indentation = line[:len(line) - len(line.lstrip())]  # Get the current indentation
            file_data[i] = f'{indentation}api_key = "{api_key}"  # Replace with your SecurityTrails API key\n'
            break
    else:
        print("Error: Could not find the placeholder line in traceflare.py.")
        exit()

    # Write the modified content back to the file
    with open(traceflare_path, 'w') as file:
        file.writelines(file_data)

    print(f"API key has been successfully added to {traceflare_path}!")
else:
    print(f"Error: {traceflare_path} does not exist. Please ensure the file is present.")
