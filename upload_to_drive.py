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

folder_id = "1QyoY1rs9Mv1yHa9-XDXGPZ4VK8ETduY3"

# 🔍 Check folder access
print("🔍 Checking access to shared folder...")
try:
    file_list = drive.ListFile({
        'q': f"'{folder_id}' in parents and trashed=false",
        'supportsAllDrives': True,
        'includeItemsFromAllDrives': True
    }).GetList()

    print(f"✅ Access check passed. Found {len(file_list)} files:")
    for file in file_list:
        print(f"  📄 {file['title']} ({file['id']})")

except Exception as e:
    print("❌ Access check failed. Service account likely does not have permission to the folder.")
    print("   ➤ Make sure the folder is shared with the service account email.")
    raise e  # Stop the script if access fails

# 🟢 If access check passed, continue with upload
file_name = "yellowpages_hammer_unions.csv"

gfile = drive.CreateFile({
    "title": file_name,
    "parents": [{"id": folder_id}]
})
gfile.SetContentFile(file_name)
gfile.Upload(param={"supportsAllDrives": True})

print(f"✅ Uploaded '{file_name}' to Shared Drive folder {folder_id}")
