from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from oauth2client.service_account import ServiceAccountCredentials
import os

# Save service account credentials from secret
with open("gdrive_key.json", "w") as f:
    f.write(os.environ["GDRIVE_KEY"])

gauth = GoogleAuth()
scope = ['https://www.googleapis.com/auth/drive']
gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name("gdrive_key.json", scope)
gauth.Authorize()

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
