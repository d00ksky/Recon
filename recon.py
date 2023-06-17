import argparse
import os
import subprocess

# Argument parser
parser = argparse.ArgumentParser(description="Automated Recon Script for Bug Bounty")
parser.add_argument('-d', '--domain', help='Target Domain', required=True)
args = parser.parse_args()

def connect_vpn():
    print("Connecting to VPN...")
    os.system("sudo protonvpn disconnect")
    os.system("sudo protonvpn c -r")

# Amass
connect_vpn()
print("Running Amass...")
command = f"amass enum -d {args.domain} -o amass_output.txt"
os.system(command)

# Sublist3r
connect_vpn()
print("Running Sublist3r...")
command = f"python3 ../tools/Sublist3r/sublist3r.py -d {args.domain} -o sublist3r_output.txt"
os.system(command)

# Subfinder
connect_vpn()
print("Running Subfinder...")
command = f"subfinder -d {args.domain} -o subfinder_output.txt"
os.system(command)

# Combine all findings
print("Combining all findings...")
command = "cat amass_output.txt sublist3r_output.txt subfinder_output.txt | sort -u > all_endpoints.txt"
os.system(command)

# Run httpx to check which endpoints are alive
connect_vpn()
print("Running httpx to check which endpoints are alive...")
command = "cat all_endpoints.txt | httpx -silent -o alive_endpoints.txt"
os.system(command)

