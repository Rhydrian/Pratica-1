import time

def algoritmo_linear(n):
    soma = 0
    for i in range(n):
        soma += 1

def algoritmo_quadratico(n):
    soma = 0
    for i in range(n):
        for j in range(n):
            soma += 1

tamanhos = [1000, 5000, 10000]

print("--- Testando Algoritmo Linear O(n) ---")
for n in tamanhos:
    inicio = time.time()
    algoritmo_linear(n)
    fim = time.time()
    print(f"n = {n:5d} | Tempo: {fim - inicio:.5f} segundos")

print("\n--- Testando Algoritmo Quadratico O(n^2) ---")
for n in tamanhos:
    inicio = time.time()
    algoritmo_quadratico(n)
    fim = time.time()
    print(f"n = {n:5d} | Tempo: {fim - inicio:.5f} segundos")
