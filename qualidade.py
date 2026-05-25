#Multiplas Funçoes -- Exeercicio Controle de Qualidade--
def cabecalho():
    print("\n" + "=" *30)
    print("SISTEMA DE QUALIDADE") 
def verificar_status(peso):
    if peso >= 50 and peso <=100:
        return "Aprovada" 
    else:
        return "Reprovada"
cabecalho()
peso_item = float(input("Digite o Peso do Item em Gramas:"))
status = verificar_status(peso_item)
print(F"Resultado do Inspeção:{status}")
print("=" *30)