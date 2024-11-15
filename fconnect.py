ascii_art = """
███████╗               ██████╗ ██████╗ ███╗   ██╗███╗   ██╗███████╗ ██████╗████████╗
██╔════╝              ██╔════╝██╔═══██╗████╗  ██║████╗  ██║██╔════╝██╔════╝╚══██╔══╝
█████╗      █████╗    ██║     ██║   ██║██╔██╗ ██║██╔██╗ ██║█████╗  ██║        ██║   
██╔══╝      ╚════╝    ██║     ██║   ██║██║╚██╗██║██║╚██╗██║██╔══╝  ██║        ██║   
██║                   ╚██████╗╚██████╔╝██║ ╚████║██║ ╚████║███████╗╚██████╗   ██║   
╚═╝                    ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝ ╚═════╝   ╚═╝   
"""
print(ascii_art)


import requests
import time
from colorama import Fore, Style

def testar_conexao(url, intervalo=5, max_tentativas=3, timeout=10):

    print(f"Testando conexão com {url}...\n")
    falhas_consecutivas = 0

    while True:
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
            }
            resposta = requests.get(url, timeout=timeout, headers=headers)
            
            if resposta.status_code == 200:
                print(f"{Fore.GREEN}[OK]{Style.RESET_ALL} O site está acessível.")
                falhas_consecutivas = 0  
            else:
                print(f"{Fore.YELLOW}[ALERTA]{Style.RESET_ALL} Conexão Cortada {resposta.status_code}.")
        except requests.RequestException as e:
            falhas_consecutivas += 1
            print(f"{Fore.RED}[ERRO]{Style.RESET_ALL} Falha ao conectar: {e}. Tentativa {falhas_consecutivas}/{max_tentativas}")

            if falhas_consecutivas >= max_tentativas:
                print(f"{Fore.RED}felipe71k Out{Style.RESET_ALL}")
                break
        
        time.sleep(intervalo)

if __name__ == "__main__":
    url = input("Digite a URL para realizar conexão: ").strip()

    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url
    
    testar_conexao(url)
