import json
from ponto import menu_ponto

def menu_login():

    print("=== Login Menu ===")
    usuario = input("digite teu usuario: ")
    senha = input("digite tua senha: ")

    # Carrega os dados dos usuários do arquivo JSON
    with open('usuarios/users.json', 'r', encoding='utf-8') as f:
        usuarios = json.load(f)

    # Verifica se o usuário existe e se a senha está correta
    if usuario in usuarios and usuarios[usuario]['senha'] == senha:
        print("Login realizado com sucesso!")
    else:
        print("Usuário ou senha incorretos.")
        return
    # Se o login for bem-sucedido, chama o menu de ponto
    menu_ponto()
    # Aqui você pode adicionar mais funcionalidades após o login, se necessário
        
    

    