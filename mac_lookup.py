import json
from collections import OrderedDict
import requests
import os
import argparse
import re

from exceptions import MyError


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-mac', '--macaddress', type=str,
                         default='Default', help='Mac address',required=True)
    return parser.parse_args()

def retrieve_mac_details():
    mac_address=vars(parse_args())
    if re.match("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac_address['macaddress'].lower()):
        env_var = os.environ
        api_key = env_var['API_KEY']
        api_url = 'https://api.macaddress.io/v1'
        response = requests.get(url=api_url + '?output=json&search=' + mac_address['macaddress'],headers= {'X-Authentication-Token': api_key} )
        mac_details = response.json()
        if mac_details:
            out_put = OrderedDict()
            out_put['company_name'] = mac_details['vendorDetails']['companyName']
            out_put['address'] = mac_details['macAddressDetails']['searchTerm']
            out_put['company_address'] = mac_details['vendorDetails']['companyAddress']
            out_put['country_code'] = mac_details['vendorDetails']['countryCode']
            out_put= json.dumps(out_put)
            print("Mac details {} for the given mac_address {}".format(out_put,mac_address['macaddress']))
        else:
            print("Mac details not found")

if __name__ == '__main__':
    retrieve_mac_details()
