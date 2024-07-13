import os
from dotenv import load_dotenv

# Memuat variabel lingkungan dari file .env jika ada
load_dotenv()

# Mendapatkan variabel lingkungan
TOKEN = os.environ.get("7422100791:AAHH8hkoriac0gLDPWH6bqnxW1EoqITSPKI")  # Dapatkan di @botfather
if not TOKEN:
    raise ValueError("Bot token is not defined. Please set the TOKEN environment variable.")

OWNER = os.environ.get("OWNER", "skoyi19")  # Isi dengan username kalian tanpa tanda @
GROUP = os.environ.get("GROUP", "Cari_pacar_jodoh_teman")  # Isi dengan username grup kalian tanpa tanda @ kalau gak punya gak usah isi
CHANNEL = os.environ.get("CHANNEL", "ofcbotxaiko")  # Isi dengan username channel kalian tanpa tanda @ kalau gak punya gak usah isi
DB_URI = os.environ.get("mongodb+srv://xaikomusic:vipmongo@vipmongo.2sp5lfs.mongodb.net/?retryWrites=true&w=majority&appName=vipmongo")  # Database URI
if not DB_URI:
    raise ValueError("Database URI is not defined. Please set the DATABASE_URL environment variable.")
