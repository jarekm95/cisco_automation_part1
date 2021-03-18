#!/usr/bin/python
"""
Script to get company name assigned to MAC address using https://macaddress.io/ site
"""
import sys
import os
import requests

API_QUERY = "https://api.macaddress.io/v1?output={output_type}&search={mac_address}"
OUTPUT_TYPE = "json"  # str: "json", "xml", "csv", "vendor"
API_KEY_ENVVAR_NAME = "MACADDRESS_IO_API_KEY"

if __name__ == "__main__":
    api_key = os.getenv(API_KEY_ENVVAR_NAME)

    if not api_key:
        print(f"{API_KEY_ENVVAR_NAME} not found in environemrnt variables. "
              f"Please store your personal key in environemnt variables")
        print(f"Command example: export {API_KEY_ENVVAR_NAME}=<your api key>")
        sys.exit(1)

    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <macaddresss>")
        sys.exit(2)

    mac_address = sys.argv[1]
    headers = {'X-Authentication-Token': api_key}
    response = requests.get(API_QUERY.format(**{"output_type": OUTPUT_TYPE,
                                                "mac_address": mac_address}),
                            headers=headers)
    if response.ok:
        companyName = response.json().get("vendorDetails").get("companyName")
        print(f"MAC: {mac_address} Company Name: {companyName}")
    else:
        print(f"Bad API response! code: {response.status_code} content: {response.text}")
        sys.exit(3)
