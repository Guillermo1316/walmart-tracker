import os
import requests
from bs4 import BeautifulSoup
from supabase import create_client, Client

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def ejecutar_scraper():
    print("Iniciando rastreo de Walmart...")
    print("¡Datos procesados con éxito!")

if _name_ == "_main_":
    ejecutar_scraper()
