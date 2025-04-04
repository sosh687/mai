import json

arquivo_cadrastros = "cadrastros.json"

def exibir_menu():
    print("/n ---- MENU CADRASTROS -----")
    print("1 - cadrastrar pessoa")
    print("2 - Ver cadrastros")
    print("3 - Sair")
    print("----------------------------")

    def salvar_cadrastros (cadrastros):
        with open (arquivo_cadrastros, "w", encoding="utf-8) as arquivos:
                   json.dump(cadrastros, arquivo, ident=4 ensure_ascii=False)

def carregar-cadrastos():
   try:
      with open (arquivo_cadrastros, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)
 execept (FileNotFoundError, json.JSONDecodeERROR):
    return []

    def cadrastros_pessoas(cadrastros)
    nome = imput("Nome:  ")
    idade = input("Idade: ")
    turma = input("Turma: ")
    curso = input("Curso:  ")
    cadrastros.append({"Nome": nome, "Idade": idadde, "Turma": turma, "Curso": curso})
    salvar_cadrastros(cadrastros)
    print("Cadrastros realizado com sucesso!")

    