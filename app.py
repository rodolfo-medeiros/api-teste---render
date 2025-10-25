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
    dict_vendas_produtos = df_vendas_produtos.to_dict()
    return dict_vendas_produtos


@app.route("/vendas/produtos/<produto>")
def vendas_produto_especifico(produto):
    df_vendas_produtos = df[['Produto','Valor Final']].groupby('Produto').sum()
    if produto in df_vendas_produtos.index:
        vendas_produto = df_vendas_produtos.loc[produto]
        dic_vendas_produto = vendas_produto.to_dict()
        return dic_vendas_produto
    
    else:
        return {produto: 'Inexistente'}
        

app.run(host="0.0.0.0") 
