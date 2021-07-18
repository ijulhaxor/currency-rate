import requests
import bs4
import os

def banner():
    clear()
    print(f"""===================
Konverter Mata Uang
===================
    """)
    pass
def clear():
    os.system('clear')
    pass
def pause():
    input()
    pass

def USDtoIDR(nominal):
    url    = f"https://www.google.com/search?q={nominal}+dollar+ke+rupiah"
    req    = requests.get( url )
    soup   = bs4.BeautifulSoup( req.text, "html.parser" )
    result = soup.find('div', class_='BNeawe').text

    print(f"\n{nominal} Dolar Amerika Serikat sama dengan {result}")
    pass

def IDRtoUSD(nominal):
    url    = f"https://www.google.com/search?q={nominal}+idr+ke+usd"
    req    = requests.get( url )
    soup   = bs4.BeautifulSoup( req.text, "html.parser" )
    result = soup.find('div', class_='BNeawe').text

    print(f"\n{nominal} Rupiah Indonesia sama dengan {result}")
    pass
    
def fromToCurrency(nominal, fromCurrency, toCurrency):
    url    = f"https://www.google.com/search?q={nominal}+{fromCurrency}+ke+{toCurrency}"
    req    = requests.get( url )
    soup   = bs4.BeautifulSoup( req.text, "html.parser" )
    result = soup.find('div', class_='BNeawe').text

    print(f"\n{nominal} {fromCurrency} sama dengan {result}")
    pass

clear()
while True:
    banner()
    print("[1] USD to IDR\n[2] IDR to USD\n[3] From currency to currency\n[q] Exit\n")
    choose = input(">> ")
    if choose == "1":
        banner()
        print('USD to IDR\n')
        nominal = input('Nominal : ')
        USDtoIDR(nominal)
        pause()
        pass
    if choose == "2":
        banner()
        print('IDR to USD\n')
        nominal = input('Nominal : ')
        IDRtoUSD(nominal)
        pause()
        pass
    if choose == "3":
        banner()
        print('From currency to currency\n')
        nominal      = input('Nominal       : ')
        fromCurrency = input('From currency : ')
        toCurrency   = input('To currency   : ')
        fromToCurrency(nominal, fromCurrency, toCurrency)
        pause()
        pass
    if choose == "q":
        exit()
        pass
    pass
