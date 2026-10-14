import os
import requests
from bs4 import BeautifulSoup
from supabase import create_client, Client

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
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
            nombre = item.select_text('h3')
            precio = item.select_text('span.price')
            
            if nombre and precio:
                productos.append({
                    "name": nombre.strip(),
                    "store_name": "Walmart",
                    "price": float(precio.replace('$', '').replace(',', '').strip())
                })
                
        return productos

    except Exception as e:
        print(f"Ocurrió un error durante el scraping: {e}")
        return []

def guardar_en_supabase(productos):
    for producto in productos:
        supabase.table("products").insert(producto).execute()
        print(f"Guardado: {producto['name']} - ${producto['price']}")

if _name_ == "_main_":
    print("Iniciando extracción de precios de Walmart...")
    items = scrape_walmart()
    if items:
        guardar_en_supabase(items)
    else:
        print("No se encontraron productos o el sitio bloqueó la petición temporalmente.")
