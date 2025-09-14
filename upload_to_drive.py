from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from oauth2client.service_account import ServiceAccountCredentials
import os

# Save credentials from GitHub secret to file
with open("gdrive_key.json", "w") as f:
    f.write(os.environ["GDRIVE_KEY"])

# Authenticate with service account
gauth = GoogleAuth()
gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name(
    "gdrive_key.json",
    ["https://www.googleapis.com/auth/drive"]
)
drive = GoogleDrive(gauth)

# Upload to specific folder
file_name = "yellowpages_hammer_unions.csv"
folder_id = "1QyoY1rs9Mv1yHa9-XDXGPZ4VK8ETduY3"  # Replace with your actual folder ID

gfile = drive.CreateFile({
    "title": file_name,
    "parents": [{"id": folder_id}]
})
gfile.SetContentFile(file_name)
gfile.Upload()

print(f"✅ Uploaded '{file_name}' to Google Drive folder {folder_id}")
