# 📌 Currency/Crypto Converter

This is a Python program that allows you to check real-time cryptocurrency exchange rates, retrieve historical data, and convert currencies using the Coinlayer API.

## 🚀 Features
- 📊 Listing of live exchange rates for all currencies.
- 🔍 Query live exchange rates for a specific currency.
- 📆 Retrieve historical cryptocurrency data.
- 💸 Currency conversion using live exchange rates.
- 🛠 Error handling and data validation.

## 🛠 Requirements
- Python 3.x
- A [Coinlayer](https://coinlayer.com/) account to obtain an API Key.
- A `.env` file containing the `API_KEY`.

## 📦 Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/SrCidm/currencyConverterInPython
   cd currencyConverterInPython
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root of the project and add your API Key:
   ```ini
   API_KEY=your_api_key_here
   ```

## 🏃 Usage
Run the script with:
```bash
python currencyConverter.py
```
An interactive menu will be displayed with options to query live data, historical data, and perform currency conversions.

## 📌 Menu Options
1️⃣ 📊 List all live currencies.
2️⃣ 🔍 Query exchange rate for a specific currency.
3️⃣ 📆 Retrieve historical cryptocurrency data.
4️⃣ 💸 Convert currencies.
5️⃣ ❌ Exit.

## 📜 License
This project is licensed under the MIT License.
