from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import os

# Save credentials from GitHub secret
with open("gdrive_key.json", "w") as f:
    f.write(os.environ["GDRIVE_KEY"])

# Authenticate using pydrive2's LoadServiceConfigFile method
gauth = GoogleAuth()
gauth.LoadServiceConfigFile("gdrive_key.json")
drive = GoogleDrive(gauth)

file_name = "yellowpages_hammer_unions.csv"
folder_id = "1QyoY1rs9Mv1yHa9-XDXGPZ4VK8ETduY3"

gfile = drive.CreateFile({
    "title": file_name,
    "parents": [{"id": folder_id}]
})
gfile.SetContentFile(file_name)
gfile.Upload(param={"supportsAllDrives": True})

print(f"✅ Uploaded '{file_name}' to Shared Drive folder {folder_id}")
