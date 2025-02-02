import os
import time
from TikTokLive import TikTokLiveClient

# Username TikTok target
username = "itsme.cips"
client = TikTokLiveClient(unique_id=username)

# Path file rekaman
file_name = f"{username}_live.mp4"

@client.on("live")
def start_recording(event):
    print(f"✅ {username} sedang live! Mulai rekam...")

    # Jalankan rekaman pakai yt-dlp
    os.system(f'yt-dlp -o "{file_name}" -f best "https://www.tiktok.com/@{username}/live"')

    print("📤 Mengupload ke Google Drive...")
    
    # Upload ke Google Drive pakai gdrive
    os.system(f'gdrive upload "{file_name}"')

    print("✅ Upload selesai! Menghapus file lokal...")
    
    # Hapus file lokal setelah diupload
    os.remove(file_name)

# Jalankan bot untuk memantau live TikTok
client.run()
