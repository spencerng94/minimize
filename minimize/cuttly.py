import requests
import sys
import config as api

# the URL you want to shorten (example here)
url = "https://www.thepythoncode.com/topic/using-apis-in-python"

# preferred name in the URL

api_url = f"https://cutt.ly/api/api.php?key={api.api_key}&short={url}"
# or
# api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}&name=some_unique_name"

# make the request
data = requests.get(api_url).json()["url"]
if data["status"] == 7:
    # OK, get shortened URL
    shortened_url = data["shortLink"]
    print("Shortened URL:", shortened_url)
else:
    print("[!] Error Shortening URL:", data)