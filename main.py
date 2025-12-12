from street import Street
from custom import Custom
from esportiva import Esportiva
from scooter import Scooter

def sugerir_tipo_por_necessidade():
    print("=== Questionário para sugerir sua moto ideal ===\n")

    print("1) Qual seu nível de experiência como motociclista?")
    print("1 - Iniciante (primeira moto ou pouca experiência)")
    print("2 - Intermediário")
    print("3 - Experiente")
    exp = input("Escolha uma opção (1-3): ")

    print("\n2) Qual é o tipo de trajeto que você mais faz?")
    print("1 - Principalmente cidade")
    print("2 - Principalmente estrada/viagens longas")
    print("3 - Misto (cidade e estrada)")
    traj = input("Escolha uma opção (1-3): ")

    print("\n3) Qual é a sua prioridade principal?")
    print("1 - Economia de combustível / baixo custo")
    print("2 - Conforto")
    print("3 - Desempenho / velocidade")
    prio = input("Escolha uma opção (1-3): ")

    # Regra base aproximada, considerando recomendações comuns do mercado
    # Iniciantes + cidade + economia => Scooter ou Street
    if exp == "1" and traj == "1" and prio == "1":
        return "Scooter"

    # Iniciantes + cidade/misto, mas quer algo mais versátil => Street
    if exp == "1" and traj in ["1", "3"]:
        return "Street"

    # Foco em conforto e viagens/estrada => Custom
    if traj == "2" and prio == "2":
        return "Custom"

    # Foco em desempenho/velocidade e piloto não iniciante => Esportiva
    if prio == "3" and exp in ["2", "3"]:
        return "Esportiva"

    # Misto cidade/estrada e prioridade economia => Street
    if traj == "3" and prio == "1":
        return "Street"

    # Caso genérico: se nada encaixar claramente, sugerir Street
    return "Street"

def escolher_tipo_final(tipo_sugerido):
    print(f"\nTipo sugerido para sua necessidade: {tipo_sugerido}")
    
    print("\nCaso não tenha gostado da sugestão, escolha outro tipo:")
    print("1 - Street")
    print("2 - Custom")
    print("3 - Esportiva")
    print("4 - Scooter")
    print("Pressione ENTER para manter a sugestão.")

    op2 = input("Escolha uma opção (1-4 ou ENTER): ")

    if op2 == "":
        return tipo_sugerido
    elif op2 == "1":
        return "Street"
    elif op2 == "2":
        return "Custom"
    elif op2 == "3":
        return "Esportiva"
    elif op2 == "4":
        return "Scooter"
    else:
        print("Opção inválida. Mantendo o tipo sugerido.")
        return tipo_sugerido

def criar_moto(tipo, modelo, ano, cilindrada):
    if tipo == "Street":
        return Street(modelo, ano, cilindrada)
    elif tipo == "Custom":
        return Custom(modelo, ano, cilindrada)
    elif tipo == "Esportiva":
        return Esportiva(modelo, ano, cilindrada)
    elif tipo == "Scooter":
        return Scooter(modelo, ano, cilindrada)
    else:
        # fallback
        return Street(modelo, ano, cilindrada)

def main():
    print("=== Assistente de Escolha de Moto ===\n")

    tipo_sugerido = sugerir_tipo_por_necessidade()
    tipo_final = escolher_tipo_final(tipo_sugerido)

    print("\nAgora informe alguns dados da moto que você quer simular:")
    modelo = input("Modelo: ")
    ano = int(input("Ano: "))
    cilindrada = int(input("Cilindrada (cc): "))

    moto = criar_moto(tipo_final, modelo, ano, cilindrada)

    print("\n=== Resultado da Análise da Moto Escolhida ===")
    print(moto.analisar())

    print("\n=== Exemplos de outros tipos disponíveis ===")
    motos_exemplo = [
        Street("Honda CG", 2025, 160),
        Custom("Harley Iron", 2024, 883),
        Esportiva("Yamaha R1", 2025, 1000),
        Scooter("Honda PCX", 2025, 150)
    ]
    for m in motos_exemplo:
        print(m.analisar())
        print("---")

if __name__ == "__main__":
    main()
