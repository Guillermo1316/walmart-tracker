import os
import requests
from bs4 import BeautifulSoup
from supabase import create_client, Client

# Limpiamos posibles espacios o diagonales extra en los secretos
SUPABASE_URL = os.environ.get("SUPABASE_URL", "").strip().rstrip('/')
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "").strip()

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def scrape_walmart():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "es-ES,es;q=0.9"
    }

    url = "https://www.walmart.com.mx/supermercado"

    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Error al conectar con Walmart: {response.status_code}")
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        productos = []

        for item in soup.select('div.product-card'):
            nombre_elem = item.select_first('h3')
            precio_elem = item.select_first('span.price')

            nombre = nombre_elem.text.strip() if nombre_elem else None
            precio = precio_elem.text.strip() if precio_elem else None

            if nombre and precio:
                productos.append({
                    "name": nombre,
                    "price": precio
                })

        return productos
    except Exception as e:
        print(f"Error durante el scraping: {e}")
        return []

if _name_ == "_main_":
    print("Iniciando scraping de Walmart...")
    productos = scrape_walmart()
    print(f"Se encontraron {len(productos)} productos.")

    if productos:
        try:
            # Asegúrate de que tu tabla en Supabase se llame 'products'
            data = supabase.table("products").insert(productos).execute()
            print("Datos guardados exitosamente en Supabase.")
        except Exception as e:
            print(f"Error al guardar en Supabase: {e}")
