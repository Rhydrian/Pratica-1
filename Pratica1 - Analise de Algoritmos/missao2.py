import time


print("Gerando vetor na memoria...")
vetor_gigante = list(range(10000000))
print("Vetor gerado!\n")

def busca(lista, alvo):
    for elemento in lista:
        if elemento == alvo:
            return True
    return False


inicio = time.time()
busca(vetor_gigante, 0)
fim = time.time()
print(f"Tempo Cenario A (Buscando 0): {fim - inicio:.6f} s")


inicio = time.time()
busca(vetor_gigante, -1)
fim = time.time()
print(f"Tempo Cenario B (Buscando -1): {fim - inicio:.6f} s")
