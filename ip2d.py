import os
import socket
import sys

filename = 'art.txt'

if os.path.exists(filename):
    with open(filename, 'r') as f:
        # Read the contents of the file
        readme = f.read()

    # Print the contents of the README file to the console
    print(readme)
else:
    print(f"The file {filename} does not exist.")

# Get the input file name from the command line arguments or use a default value
input_filename = 'input.txt'
if len(sys.argv) > 1:
    input_filename = sys.argv[1]

# Open the input file
with open(input_filename, 'r') as f:
    # Read the IP addresses from the file
    ips = f.read().splitlines()

# Open the output file
output_filename = 'ip_convertedTo_domain.txt'
with open(output_filename, 'w') as f:
    # Iterate over the IP addresses
    for ip in ips:
        # Try to resolve the IP address to a domain name
        domain = None
        try:
            domain = socket.gethostbyaddr(ip)[0]
        except socket.herror:
            domain = ip

        # Write the domain name (or IP address) to the output file
        f.write(domain + '\n')
        # Print the resolution (or IP address) to the console
        print(domain)
