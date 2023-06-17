import os
import re
import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Define the argument parser
parser = argparse.ArgumentParser(description="JavaScript Analysis Script")
parser.add_argument('-u', '--url', help='Target URL', required=True)
args = parser.parse_args()

# The URL of the webpage you want to scrape
url = args.url

# Send a GET request to the webpage
response = requests.get(url)

# Parse the webpage's content
soup = BeautifulSoup(response.text, "html.parser")

# Create a directory to store the JavaScript files
os.makedirs("js_files", exist_ok=True)

# Regex pattern to match URLs
url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

# Regex pattern to match JavaScript comments
comment_pattern = re.compile(r'/\*.*?\*/|//.*?$', re.DOTALL | re.MULTILINE)

# Open output files
endpoints_file = open("endpoints.txt", "w")
comments_file = open("comments.txt", "w")

# Find all script tags
for script in soup.find_all("script"):
    # If the script tag has a src attribute, it's a link to a JavaScript file
    if script.get("src"):
        # Join the URL of the webpage with the URL of the JavaScript file
        js_url = urljoin(url, script.get("src"))
        
        # Send a GET request to the JavaScript file's URL
        js_response = requests.get(js_url)

        # Get the filename of the JavaScript file
        filename = os.path.join("js_files", js_url.split("/")[-1])
        
        # Write the content of the JavaScript file to a local file
        with open(filename, "w") as f:
            f.write(js_response.text)

        # Extract comments
        comments = re.findall(comment_pattern, js_response.text)

        # Extract potential endpoints
        endpoints = re.findall(url_pattern, js_response.text)

        # Write comments and endpoints to their respective files
        for comment in comments:
            comments_file.write(f"{filename}: {comment}\n")
        
        for endpoint in endpoints:
            endpoints_file.write(f"{filename}: {endpoint}\n")

        # Generate a simple summary
        total_lines = len(js_response.text.split('\n'))
        total_comments = len(comments)
        total_endpoints = len(endpoints)

        print(f"Summary for {filename}:")
        print(f"Total lines: {total_lines}")
        print(f"Total comments: {total_comments}")
        print(f"Total potential endpoints: {total_endpoints}\n")

# Close output files
endpoints_file.close()
comments_file.close()

