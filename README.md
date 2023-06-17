# Recon 

Simple scripts used in my recon process

## recon.py

This script is using amass, sublist3r and subfinder to enumerate endpoints, and protonvpn 
for VPN.
Than it uniques findings to remove duplicates and saves it in file.
Between starting each tool it also disconnects from vpn and makes new connection with different IP.

## js_download.py

This simple script just downloads all js files it can find in url.

## js_search.py

This script downloads all js files and then in separate txt file
provides you with all endpoints it found with names of files.
It also creates txt file with all comments from js files.
