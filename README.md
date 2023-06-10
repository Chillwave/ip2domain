# P 2 Domain Name Converter

This script converts a list of IP addresses to domain names.

## Usage

To use the script, run the following command:

python ip2d.py [input_file]

`input_file` is the name of the file containing the list of IP addresses to convert. If no input file is specified, the script will use the default file `input.txt`.

The script will write the results to the file `ip_convertedTo_domain.txt`.

## Example

Suppose the file `input.txt` contains the following list of IP addresses:

8.8.8.8
8.8.4.4
1.1.1.1

Running the script with the default input file will produce the following output:

google-public-dns-a.google.com
google-public-dns-b.google.com
one.one.one.one

The output will be written to the file `ip_convertedTo_domain.txt`.

## Notes

- If an IP address cannot be resolved to a domain name, it will still be included in the output.
- The script requires the Python `socket` module.
