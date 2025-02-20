# 📌 Crypto Exchange CLI

Este es un programa en Python que permite consultar tasas de cambio de criptomonedas en tiempo real, obtener datos históricos y convertir monedas utilizando la API de Coinlayer.

## 🚀 Características
- 📊 Listado de tasas de cambio en vivo para todas las monedas.
- 🔍 Consulta de tasas de cambio en vivo para una moneda específica.
- 📆 Obtención de datos históricos de criptomonedas.
- 💸 Conversión de monedas utilizando tasas de cambio en vivo.
- 🛠 Manejo de errores y validación de datos.

## 🛠 Requisitos
- Python 3.x
- Cuenta en [Coinlayer](https://coinlayer.com/) para obtener una API Key.
- Archivo `.env` con la clave `API_KEY`.

## 📦 Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/SrCidm/currencyConverterInPython
   cd currencyConverterInPython
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Crea un archivo `.env` en la raíz del proyecto y añade tu API Key:
   ```ini
   API_KEY=tu_api_key_aqui
   ```

## 🏃 Uso
Ejecuta el script con:
```bash
python currencyConverter.py
```
Se mostrará un menú interactivo con opciones para consultar datos en vivo, datos históricos y realizar conversiones de moneda.

## 📌 Menú de Opciones
1️⃣ 📊 Listado de todas las monedas en vivo.
2️⃣ 🔍 Consultar tasa de cambio de una moneda específica.
3️⃣ 📆 Obtener datos históricos de criptomonedas.
4️⃣ 💸 Convertir monedas.
5️⃣ ❌ Salir.

## 📜 Licencia
Este proyecto está bajo la licencia MIT.
