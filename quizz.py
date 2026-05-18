print("=== QUIZ DE VOLEI ===")

pontuacao = 0

# pergunta 1
print("\n1) Quantos jogadores cada time tem em quadra no volei?")
print("a) 5")
print("b) 6")
print("c) 7")

resposta1 = input("digite a resposta: ")

if resposta1 == "b":
    print("Correto")
    pontuacao += 1
else:
    print("Errado! A resposta correta é a b) 6")

#pergunta 2
print("\n2) Qual fundamento é usado para iniciar a jogada no volei?")
print("a) Saque")
print("b) Bloqueio")
print("c) manchete")

resposta2 = input("Digite a resposta: ")

if resposta2 == "a":
    print("Correto!")
    pontuacao += 1
else: 
    print("Errado! A resposta correta é a) Saque")

# pergunta 3 
print("\n3) Quantos sets um time precisa ganhar para vencer uma partida ofcial?")
print("a) 2")
print("b) 3")
print("c) 5")

resposta3 = input("Digite a resposta: ")

if resposta3 == "b":
    print("correto!")
    pontuacao += 1
else:
    print("Errado! A resposta correta é b) 3")

print("\n=== RESULTADO FINAL ===")
print("Voce acertou", pontuacao, "de 3 perguntas.")
