import requests
import json


dict_vendas_produtos = requests.get("https://api-teste-render-xgxa.onrender.com/vendas/produtos/Terno Linho")
print(dict_vendas_produtos.json())
