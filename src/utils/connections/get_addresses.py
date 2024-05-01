'''
Description:
    Get's the associated IP addresses of the game
'''

import subprocess

# retrieve the addresses
def retrieve():
    addresses = []
    
    # hostname 
    host = 'game-us.habbo.com'

    try:
        # execute dig command and capture the output
        result = subprocess.check_output(["dig", host], text=True)

        # split the output into lines
        result_lines = result.split('\n')

        # process each line of the dig output
        for line in result_lines:
            # check if the line contains the hostname and IP address (in ANSWER section)
            if host in line and line.startswith(host):
                # split the line into parts
                parts = line.split()

                # extract the IP address from the line (assuming it's the last part)
                if len(parts) > 4 and parts[3] == 'A':
                    ip_address = parts[4]
                    addresses.append(ip_address)

    except subprocess.CalledProcessError as e:
        print(f"Failed executing subprocess: {e.returncode}")

    return addresses