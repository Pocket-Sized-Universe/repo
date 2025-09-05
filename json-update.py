import requests
import json
import os

# Path to the JSON file
json_path = os.path.join(os.path.dirname(__file__), "PocketSizedUniverse", "PocketSizedUniverse.json")

# GitHub API for latest release
repo = "Pocket-Sized-Universe/client"
api_url = f"https://api.github.com/repos/{repo}/releases/latest"

response = requests.get(api_url)
release = response.json()

# Find the first .zip asset
zip_asset = next((a for a in release.get("assets", []) if a["name"].endswith(".zip")), None)
if not zip_asset:
    raise Exception("No .zip asset found in the latest release.")

download_url = zip_asset["browser_download_url"]
version = release["tag_name"].lstrip("v")  # Remove 'v' prefix if present

# Load the JSON file
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Update fields
data["DownloadLinkInstall"] = download_url
data["DownloadLinkTesting"] = download_url
data["DownloadLinkUpdate"] = download_url
data["AssemblyVersion"] = version

# Save the updated JSON
with open("plogonmaster.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)