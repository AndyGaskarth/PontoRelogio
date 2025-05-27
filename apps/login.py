import json
import os
from .ponto import menu_ponto

def menu_login():
    print("=== Login Menu ===")
    usuario = input("Digite seu usuário: ").strip()
    senha = input("Digite sua senha: ").strip()

    caminho_json = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'usuarios', 'users.json')

    try:
        with open(caminho_json, 'r', encoding='utf-8') as f:
            usuarios = json.load(f)
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")
        return

    # Busca o usuário na lista
    usuario_encontrado = None
    for u in usuarios:
        if u.get("usuario") == usuario:
            usuario_encontrado = u
            break

    if usuario_encontrado:
        if usuario_encontrado.get("senha") == senha:
            print("Login realizado com sucesso!")
            menu_ponto()
        else:
            print("Senha incorreta.")
    else:
        print("Usuário não encontrado.")



