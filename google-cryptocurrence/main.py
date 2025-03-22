import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime



#Coins to get price data
coins = [
    'bitcoin',
    'ethereum',
    'bnb',
    'dogecoin',
    'xrp'
]

# Get user input for which coin to track
print("Moedas disponíveis:")
for i, coin in enumerate(coins, 1):
    print(f"{i}. {coin}")

while True:
    try:
        choice = int(input("\nSelecione uma moeda (1-5): "))
        if 1 <= choice <= len(coins):
            selected_coin = coins[choice-1]
            break
        else:
            print("Por favor, insira um número válido entre 1 e 5")
    except ValueError:
        print("Por favor, insira um número válido")

print(f"\nVocê selecionou {selected_coin}. Iniciando rastreio de preço...")


# URL of the coin page on CoinMarketCap
url = f"https://coinmarketcap.com/currencies/{selected_coin}/" #if dont workout, use the api from binance "https://data-api.binance.vision/api/v3/exchangeInfo?symbol=BTCUSDT"


# Function to get the price and save to CSV
def obter_preco():
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()

        # Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Finding the span with the price
        span = soup.find("span", class_="sc-65e7f566-0 WXGwg base-text", attrs={"data-test": "text-cdp-price-display"})
        
        if span:
            preco = span.text.strip()
            horario = datetime.now().strftime("%H:%M:%S")
            data = datetime.now().strftime("%Y-%m-%d")
            
            # Save data to CSV
            with open(f'{selected_coin}_prices.csv', 'a') as f:
                if f.tell() == 0:  # If file is empty, write the header
                    f.write("Data,Hora,Preço\n")
                f.write(f"{data},{horario},{preco}\n")
            
            return f"Preço da {selected_coin}: {preco} (Atualizado em: {horario})"
        else:
            return "Não foi possível encontrar o preço."

    except requests.exceptions.RequestException as e:
        return f"Erro ao buscar preço: {e}"

# Loop to check the price every 30 seconds
try:
    while True:
        print(obter_preco())
        time.sleep(30)
except KeyboardInterrupt:
    print("\nPrograma encerrado pelo usuário.")