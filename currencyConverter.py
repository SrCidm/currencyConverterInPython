from dotenv import load_dotenv
import os
from requests import get
from pprint import PrettyPrinter
from datetime import datetime

# Inicializar el pretty printer
printer = PrettyPrinter()

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Acceder a la API key
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    print("❌ API_KEY not found. Please check your .env file.")
    exit()

BASE_URL = "http://api.coinlayer.com/api/"
LIVE = f"live?access_key={API_KEY}"
HISTORICAL = "YYYY-MM-DD?access_key=" + API_KEY + "&target=USD&symbols=BTC,ETH"
CONVERTER = f"convert?access_key={API_KEY}"
TIMEFRAME = f"timeframe?access_key={API_KEY}"

def fetch_api_data(url):
    """ Realiza una solicitud a la API y maneja errores de forma genérica. """
    try:
        response = get(url)
        response.raise_for_status()
        data = response.json()

        if not data.get("success", False):
            print(f"❌ API Error: {data.get('error', {}).get('info', 'Unknown error')}")
            return None
        return data
    except Exception as e:
        print(f"❌ Error fetching data: {e}")
        return None

def get_live_all_data():
    """ Obtiene y devuelve los datos en vivo de todas las monedas. """
    url = BASE_URL + LIVE
    data = fetch_api_data(url)
    return sorted(data["rates"].items()) if data else []

def print_live_all_data():
    """ Imprime los datos en vivo de todas las monedas disponibles. """
    print("\n🌍📈 Live Exchange Rates 📈🌍")
    data = get_live_all_data()
    if not data:
        print("⚠️ No data available.")
        return
    for currency, value in data:
        print(f"💰 {currency}: {value:.2f}")

def get_live_data(symbols, target="USD"):
    """ Obtiene y muestra datos en vivo de monedas específicas. """
    symbols = symbols.upper()
    target = target.upper()
    url = f"{BASE_URL}{LIVE}&target={target}&symbols={symbols}"

    data = fetch_api_data(url)
    if data:
        rates = data.get("rates", {})
        if symbols not in rates:
            print(f"⚠️ No data available for {symbols} with target {target}.")
            return
        
        print(f"\n🔹 Currency: {symbols}\n🔹 Target: {target}\n🔹 Exchange Rate: {rates[symbols]:.2f}\n")

def get_historical_data(date, target_currency, symbols):
    """ Obtiene datos históricos de una fecha específica. """
    try:
        date = datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d")
        url = BASE_URL + HISTORICAL.replace("YYYY-MM-DD", date) + f"&target={target_currency}&symbols={symbols}"
        
        data = fetch_api_data(url)
        if data:
            rates = data.get("rates", {})
            if not rates:
                print(f"⚠️ No historical data available for {symbols} on {date}.")
                return

            print("\n📅 Historical Data")
            print("-------------------------")
            print(f"📆 Date: {data['date']}")
            print(f"🎯 Target Currency: {data['target']}")
            for currency, value in rates.items():
                print(f"💰 {currency}: {value:.2f}")
            print("-------------------------\n")
    
    except ValueError:
        print("❌ Error: Invalid date format. Please use YYYY-MM-DD.")

def convert_currency(amount, from_currency, to_currency):
    """ Convierte una cantidad de una moneda a otra usando tasas de cambio en vivo. """
    try:
        amount = float(amount)
        from_currency, to_currency = from_currency.upper(), to_currency.upper()
        
        url = f"{BASE_URL}{LIVE}&symbols={from_currency},{to_currency}"
        data = fetch_api_data(url)
        
        if data:
            rates = data.get("rates", {})
            if from_currency not in rates or to_currency not in rates:
                print(f"⚠️ No data available for {from_currency} or {to_currency}.")
                return

            rate_from, rate_to = rates[to_currency], rates[from_currency]
            converted_amount = (amount / rate_from) * rate_to

            print(f"💵 {amount} {from_currency} ≈ {converted_amount:.4f} {to_currency} 💱")
    
    except ValueError:
        print("❌ Error: amount must be a number.")


def display_menu():
    """ Muestra el menú principal con más emojis 🎉. """
    print("\n💰💱 Welcome to Crypto Exchange 💱💰")
    print("===================================")
    print("1️⃣  📊 List of all currencies")
    print("2️⃣  🔍 Get live data for a specific currency")
    print("3️⃣  📆 Get historical data")
    print("4️⃣  💸 Convert currency")
    print("5️⃣  ❌ Exit")
    print("===================================")

def handle_user_choice(choice):
    """ Maneja la selección del usuario en el menú. """
    if choice == "1":
        print_live_all_data()
    elif choice == "2":
        symbols = input("🔎 Enter symbols (comma-separated): ")
        target_currency = input("🎯 Enter target currency: ")
        get_live_data(symbols, target_currency) 
    elif choice == "3":
        date = input("📆 Enter date (YYYY-MM-DD): ")
        target_currency = input("🎯 Enter target currency: ")
        symbols = input("💰 Enter symbols (comma-separated): ")
        get_historical_data(date, target_currency, symbols)
    elif choice == "4":
        amount = input("💰 Enter amount: ")
        from_currency = input("🔄 Enter from currency: ")
        to_currency = input("🔁 Enter to currency: ")
        convert_currency(amount, from_currency, to_currency)
    elif choice == "5":
        print("👋 Goodbye! Have a great day! 🚀💸")
        exit()
    else:
        print("❌ Invalid choice. Please try again.")

def main():
    """ Función principal que ejecuta el programa. """
    while True:
        display_menu()
        choice = input("👉 Enter your choice: ")
        handle_user_choice(choice)
        input("🔄 Press Enter to continue...")

if __name__ == "__main__":
    main()

    