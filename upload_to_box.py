import os
import json
import datetime
from boxsdk import JWTAuth, Client

# Load Box config from GitHub secret
raw_json = os.environ["BOX_CONFIG_JSON"]
config = json.loads(raw_json)
print("Loaded Box config OK")

# Authenticate with Box
auth = JWTAuth.from_settings_dictionary(config)
auth.authenticate_instance()
client = Client(auth)

# Target folder ID (replace with your real one)
folder_id = "224419986473"

# Build today's filename
today = datetime.datetime.now().strftime("%m%d")
filename = f"企業一覧とユーザー一覧_{today}.xlsx"
file_path = f"output/{filename}"

# Check file exists before upload
if not os.path.exists(file_path):
    raise FileNotFoundError(f"❌ File not found: {file_path}")

# Upload to Box
folder = client.folder(folder_id=folder_id)
uploaded_file = folder.upload(file_path, file_name=filename)
print("✅ File uploaded successfully!")
print("📎 Download link:", uploaded_file.get_shared_link_download_url())
