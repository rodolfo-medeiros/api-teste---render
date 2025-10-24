import requests
import json


dict_vendas_produtos = requests.get("https://api-teste-render-xgxa.onrender.com/vendas/produtos/<Polo Estampa>").json()

print(dict_vendas_produtos)

