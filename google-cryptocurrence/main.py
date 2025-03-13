import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

# URL da página do Ethereum no CoinMarketCap
url = "https://coinmarketcap.com/currencies/ethereum/"

# Função para obter o preço
def obter_preco():
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()

        # Parse do HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Encontrando o span com o preço
        span = soup.find("span", class_="sc-65e7f566-0 WXGwg base-text", attrs={"data-test": "text-cdp-price-display"})
        
        if span:
            preco = span.text.strip()
            horario = datetime.now().strftime("%H:%M:%S")
            return f"Preço do Ethereum: {preco} (Atualizado em: {horario})"
        else:
            return "Não foi possível encontrar o preço."

    except requests.exceptions.RequestException as e:
        return f"Erro ao buscar preço: {e}"

# Loop para verificar o preço a cada 30 segundos
try:
    while True:
        print(obter_preco())
        time.sleep(30)
except KeyboardInterrupt:
    print("\nPrograma encerrado pelo usuário.")