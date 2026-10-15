import os
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

data = {
    "nombre": "Producto Prueba Walmart",
    "precio": 99.50
}

try:
    response = supabase.table("productos_walmart").insert(data).execute()
    print("¡Datos insertados con éxito en Supabase!", response)
except Exception as e:
    print("Error al insertar los datos:", e)
