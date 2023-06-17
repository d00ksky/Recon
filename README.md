# Recon 

Simple scripts used in my recon process

## recon.py

This script is using amass, sublist3r and subfinder to enumerate endpoints, and protonvpn 
for VPN.
Than it uniques findings to remove duplicates and saves it in file.
Between starting each tool it also disconnects from vpn and makes new connection with different IP.
