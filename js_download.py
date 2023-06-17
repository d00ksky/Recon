import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# The URL of the webpage you want to scrape
url = "https://bunny.net"

# Send a GET request to the webpage
response = requests.get(url)

# Parse the webpage's content
soup = BeautifulSoup(response.text, "html.parser")

# Create a directory to store the JavaScript files
os.makedirs("js_files", exist_ok=True)

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

