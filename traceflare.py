#!/usr/bin/python3
import os
import requests
import sys
from ipaddress import ip_address, ip_network
from termcolor import colored
from datetime import datetime

if os.name == 'nt':  # For Windows
    os.system('cls')
else:  # For macOS and Linux
    os.system('clear')
# ASCII Art Banner

BANNER = r"""


░▒▓████████▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░      ░▒▓████████▓▒░▒▓█▓▒░       ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░ 
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░             ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
   ░▒▓█▓▒░   ░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░      ░▒▓██████▓▒░        ░▒▓██████▓▒░ ░▒▓█▓▒░      ░▒▓████████▓▒░▒▓███████▓▒░░▒▓██████▓▒░   
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░             ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓████████▓▒░      ░▒▓█▓▒░      ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░ 
                                                                                                                                           
                                                                                                                                           


                                        Track IP History & Detect Cloudflare Presence
-------------------------------------------------------------------------------------------------------------------------------------------
"""

# Cloudflare IP ranges
CLOUDFLARE_IP_RANGES = [
    "103.21.244.0/22",
    "103.22.200.0/22",
    "103.31.4.0/22",
    "104.16.0.0/13",
    "104.24.0.0/14",
    "108.162.192.0/18",
    "131.0.72.0/22",
    "141.101.64.0/18",
    "162.158.0.0/15",
    "172.64.0.0/13",
    "173.245.48.0/20",
    "188.114.96.0/20",
    "190.93.240.0/20",
    "197.234.240.0/22",
    "198.41.128.0/17"
]

def is_cloudflare_ip(ip):
    """Check if an IP address belongs to Cloudflare."""
    try:
        ip_obj = ip_address(ip)
        for range_ in CLOUDFLARE_IP_RANGES:
            if ip_obj in ip_network(range_):
                return True
        return False
    except ValueError:
        return False  # Invalid IP address

def get_historical_ips(domain, api_key):
    """Fetch DNS history for the domain using SecurityTrails API."""
    url = f"https://api.securitytrails.com/v1/history/{domain}/dns/a"
    headers = {"APIKEY": api_key}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            records = data.get("records", [])
            
            ip_history = []
            for record in records:
                if 'values' in record:
                    for value in record['values']:
                        ip_info = {
                            "ip": value.get("ip", "N/A"),
                            "first_seen": record.get("first_seen", "N/A"),
                            "last_seen": record.get("last_seen", "N/A"),
                            "is_cloudflare": is_cloudflare_ip(value.get("ip", "N/A"))
                        }
                        ip_history.append(ip_info)
            return ip_history
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def format_date(date_str):
    """Convert date string to datetime object."""
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except Exception:
        return None

def main():
    print(colored(BANNER, "cyan"))
    
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <domain>")
        sys.exit(1)
    
    domain = sys.argv[1]
    api_key = "your_api_key_here"  # Replace with your SecurityTrails API key

    
    history = get_historical_ips(domain, api_key)
    if history:
        print(f"Historical IP addresses for {domain}:")
        non_cloudflare_ips = []
        
        for record in history:
            cloudflare_status = "Yes" if record['is_cloudflare'] else "No"
            print(f"IP: {record['ip']}, First Seen: {record['first_seen']}, Last Seen: {record['last_seen']}, Cloudflare: {cloudflare_status}")
            
            if not record['is_cloudflare']:
                last_seen_date = format_date(record['last_seen'])
                if last_seen_date:
                    non_cloudflare_ips.append((record['ip'], last_seen_date))
        
        if non_cloudflare_ips:
            # Get the IP with the latest "last seen" date
            latest_non_cf_ip = max(non_cloudflare_ips, key=lambda x: x[1])
            highlighted_message = f"""
#######################################
Possible server IP: {latest_non_cf_ip[0]} 
#######################################
"""
            print(colored(highlighted_message, "red"))
        else:
            print(colored("No non-Cloudflare IPs found in history.", "yellow"))
    else:
        print("No historical IP data found.")

if __name__ == "__main__":
    main()
