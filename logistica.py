#Calculador de Frete --
def cabecalho():
    print("\n" + "=" *30)

    print("SISTEMA DE LOGISTICA")
def calcular_frete(peso):
    if peso_carga >= 20 : 
        return peso_carga * 10.00
    else:
        return peso_carga * 15.00
cabecalho()
peso_carga = float(input("Digite o peso da carga em (kg):"))
frete = calcular_frete(peso_carga)
print(F"O valor do frete é: R$ {frete:.2f}")   
print("=" * 30)
