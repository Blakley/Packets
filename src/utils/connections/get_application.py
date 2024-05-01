'''
Description:
    Get's the associated open TCP connections for the HabboAir application
'''

import subprocess

def retrieve():
    # Command to list TCP connections and filter for "ESTABLISHED" state
    command = "lsof -iTCP -n -P -sTCP:ESTABLISHED"

    try:
        # execute the command and capture its output
        result = subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE)

        # split the output into lines
        output_lines = result.stdout.split('\n')

        # list to store lines containing "Habbo"
        habbo_connections = []

        # iterate over each line in the output
        for line in output_lines:
            if "Habbo" in line:
                habbo_connections.append(line)

        return habbo_connections

    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        return []