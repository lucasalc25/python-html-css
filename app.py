from flask import Flask, render_template, g
import sqlite3

DATABASE = "banco.bd"
SECRET_KEY = "chave"

app = Flask("Hello")
app.config.from_object(__name__)

def conecta_bd():
    return sqlite3.connect(DATABASE)


@app.before_request # Sempre antes do app iniciar uma requisição 
def antes_requisicao(): # Cria e chama a função 
    g.bd = conecta_bd() # Guarda a conexão com o banco na variável g 


@app.teardown_request # Sempre depois do app iniciar a requisição 
def depois_requisicao(e): # Cria e chama a função 
    g.bd.close() # Fecha a conexão com o banco

@app.route("/") # Cria a rota do app
def exibir_entradas(): # Cria e chama a função
    sql = "SELECT titulo, texto, criado_em FROM entradas"
    cur = g.bd.execute(sql)
    entradas = []
    for titulo, texto, criado_em in cur.fetchall():
        entradas.append({"titulo": titulo, "texto": texto, "criado_em": criado_em})
    return  render_template("layout.html", entradas = entradas ) # Retorna o arquivo html 'hello'

