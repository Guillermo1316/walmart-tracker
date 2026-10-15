import os
import time
import requests
from bs4 import BeautifulSoup
import json
from supabase import create_client, Client

# 1. Conexión a Supabase usando variables secretas de GitHub
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# 2. Lista de enlaces de productos de Walmart que deseas monitorear
walmart_urls = [
    "https://www.walmart.com/ip/tu-producto-1",  # Reemplaza con tus enlaces reales de Walmart
    "https://www.walmart.com/ip/tu-producto-2",
]

# Encabezados para simular un navegador real y evitar bloqueos
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
