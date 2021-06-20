# Mac_lookup
Retriving macadress_details 
MACLookup Tool

For a given MAC address retrieve company name and virtual machine details

- Program accepts a command line parameter of a MAC address
- Program queries the API for a result over the network
- Program outputs the Company Name associated with that MAC address 

Install required packages

Step 1. python setup.py install
Execute the script with MAC address as an argument

Step 2. python MacLookup.py -mac 6c:96:cf:de:a1:fd 

Pre-requisite
Assuming you have Python 3.x installed on your system

python --version

$ pip install maclookup-cli
step 4.
get an API key From macaddress.io
set variable according your os


# macOS and Linux
export MAC_ADDRESS_IO_API_KEY="your-api-key"

# Windows (CMD)
set MAC_ADDRESS_IO_API_KEY="your-api-key"

# Windows (PowerShell)
$env:MAC_ADDRESS_IO_API_KEY="your-api-key"

$ maclookup B8:C2:53:AC:DC:EF
CLI command to retrieve MAC address details
python MacLookup.py --help

usage: MacLookup.py [-h] -mac MACADDRESS

optional arguments:
  -h, --help            show this help message and exit
  -mac MACADDRESS, --macaddress MACADDRESS
                        Mac address
Sample snippet
python MacLookup.py --macaddress 44:38:39:ff:ef:57 

Mac details {"company_name": "Cumulus Networks, Inc", "address": "44:38:39:ff:ef:57", "company_address": "650 Castro Street, suite 120-245 Mountain
 View CA 94041 US", "country_code": "US"} for the given mac_address 44:38:39:ff:ef:57
