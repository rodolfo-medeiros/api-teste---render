## API´s retornam json (dicionarios python), sites retornam HTML
import pandas as pd
import requests
from flask import Flask


df = pd.read_excel("Vendas - Dez.xlsx")


app = Flask(__name__) ## cria o site

@app.route("/") ## diz em qual link a função vai rodar
def faturamento():
    faturamento = float(df['Valor Final'].sum())
    return {"Faturamento":faturamento}


@app.route("/vendas/produtos")
def vendas_produtos():
    df_vendas_produtos = df[['Produto','Valor Final']].groupby('Produto').sum()
    return {df_vendas_produtos}
clear

@app.route("/vendas/produtos/produtoespecifico")
def vendas_produto_especifico():
    return {"arroz":500}




app.run(host="0.0.0.0") 