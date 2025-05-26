
def registrar_entrada():
    from datetime import datetime
    entrada = datetime.now()
    with open("ponto.txt", "a") as f:
        f.write(f"Entrada: {entrada.strftime('%Y-%m-%d %H:%M:%S')}\n")
    print(f"Entrada registrada: {entrada.strftime('%Y-%m-%d %H:%M:%S')}")

def registrar_saida():
    from datetime import datetime
    saida = datetime.now()
    with open("ponto.txt", "a") as f:
        f.write(f"Saída: {saida.strftime('%Y-%m-%d %H:%M:%S')}\n")
    print(f"Saída registrada: {saida.strftime('%Y-%m-%d %H:%M:%S')}")

def verificar_horas_trabalhadas():
    from datetime import datetime
    try:
        with open("ponto.txt", "r") as f:
            registros = f.readlines()
        
        if not registros:
            print("Nenhum registro encontrado.")
            return
        
        horas_trabalhadas = 0
        ultima_entrada = None

        for registro in registros:
            if "Entrada" in registro:
                ultima_entrada = datetime.strptime(registro.split(": ")[1].strip(), '%Y-%m-%d %H:%M:%S')
            elif "Saída" in registro and ultima_entrada:
                saida = datetime.strptime(registro.split(": ")[1].strip(), '%Y-%m-%d %H:%M:%S')
                horas_trabalhadas += (saida - ultima_entrada).total_seconds() / 3600
                ultima_entrada = None  # Reset after processing a pair

        print(f"Horas trabalhadas: {horas_trabalhadas:.2f} horas")
    except FileNotFoundError:
        print("Arquivo de ponto não encontrado. Registre uma entrada ou saída primeiro.")



def menu_ponto():
    print("=== Ponto Menu ===")
    print("1. Registrar Entrada")
    print("2. Registrar Saída")
    print("3. Verificar Horas Trabalhadas")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        registrar_entrada()
    elif opcao == '2':
        registrar_saida()
    elif opcao == '3':
        verificar_horas_trabalhadas()
    elif opcao == '4':
        print("Saindo do menu de ponto.")
    else:
        print("Opção inválida, tente novamente.")