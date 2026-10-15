name: Scraping Diario Walmart

on:
  schedule:
    - cron: '0 8 * * *'  # Se ejecuta todos los días a las 8:00 AM UTC
  workflow_dispatch:      # Permite ejecutar el script manualmente desde GitHub Actions

jobs:
  run-scraper:
    runs-on: ubuntu-latest

    steps:
      - name: Copiar repositorio
        uses: actions/checkout@v3

      - name: Configurar entorno de Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Instalar dependencias
        run: |
          python -m pip install --upgrade pip
          pip install requests beautifulsoup4 supabase

      - name: Ejecutar script de Python
        env:
          SUPABASE_URL: ${{ secrets.SUPABASE_URL }}
          SUPABASE_KEY: ${{ secrets.SUPABASE_KEY }}
        run: python scraper.py
