import requests


def get_dados_fundamentus():
  metadata = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"}
  url = 'https://www.fundamentus.com.br/resultado.php'
  
  page = requests.get(url, headers= metadata)

  return page