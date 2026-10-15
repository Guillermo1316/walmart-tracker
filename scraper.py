import os
import requests
from bs4 import BeautifulSoup
from supabase import create_client, Client

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def ejecutar_scraper():
    print("Iniciando rastreo de Walmart...")
    
    # Datos que se enviarán a la tabla 'productos_walmart'
    nombre_producto = "Producto de prueba"
    precio = 45.00
    
    data = {
        "nombre": nombre_producto,
        "precio": precio
    }
    
    response = supabase.table("productos_walmart").insert(data).execute()
    print("¡Datos insertados en Supabase correctamente!", response)

if _name_ == "_main_":
    ejecutar_scraper()
