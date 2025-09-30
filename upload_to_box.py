import os
import json
import datetime
from boxsdk import JWTAuth, Client

# Load Box config
raw_json = os.environ["BOX_CONFIG_JSON"]
config = json.loads(raw_json)
print("✅ Loaded Box config OK")

# Authenticate
auth = JWTAuth.from_settings_dictionary(config["boxAppSettings"])
client = Client(auth)

# Folder ID
folder_id = "224419986473"

# Today's date
today = datetime.datetime.now().strftime("%m%d")
filename = f"企業一覧とユーザー一覧_{today}.xlsx"

# Upload
folder = client.folder(folder_id=folder_id)
uploaded_file = folder.upload(f"output/{filename}", file_name=filename)
print(" File uploaded:", uploaded_file.get_shared_link_download_url())