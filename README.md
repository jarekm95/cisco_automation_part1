# cisco_automation_part1

Script to get company name assigned to MAC address using https://macaddress.io/ site

Usage:
1. Create environement variable with api key from macaddress.io site:
export {API_KEY_ENVVAR_NAME}=<your api key>

2. Run script with argument mac address:
python3 mac_to_company_name.py <macaddresss>