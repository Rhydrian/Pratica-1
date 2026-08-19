import time

# Criando uma instancia: vetor de 0 a 9.999.999
print("Gerando vetor na memoria...")
vetor_gigante = list(range(10000000))
print("Vetor gerado!\n")

def busca(lista, alvo):
    for elemento in lista:
        if elemento == alvo:
            return True
    return False

# Cenario A: Buscando o numero 0
inicio = time.time()
busca(vetor_gigante, 0)
fim = time.time()
print(f"Tempo Cenario A (Buscando 0): {fim - inicio:.6f} s")

# Cenario B: Buscando o numero -1
inicio = time.time()
busca(vetor_gigante, -1)
fim = time.time()
print(f"Tempo Cenario B (Buscando -1): {fim - inicio:.6f} s")
