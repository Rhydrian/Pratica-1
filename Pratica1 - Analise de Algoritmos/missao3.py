import time

def etapa1_linear(n):
    soma = 0
    # O laco roda 500 vezes o valor de n
    for i in range(n * 500):
        soma += 1

def etapa2_quadratica(n):
    soma = 0
    for i in range(n):
        for j in range(n):
            soma += 1

def programa_completo(n):
    print(f"--- Testando para n = {n} ---")

    t0 = time.time()
    etapa1_linear(n)
    t1 = time.time()

    etapa2_quadratica(n)
    t2 = time.time()

    print(f"Tempo Etapa 1 (Linear): {t1 - t0:.5f} s")
    print(f"Tempo Etapa 2 (Quadratica): {t2 - t1:.5f} s")
    print(f"Tempo Total: {t2 - t0:.5f} s\n")

# Vamos testar valores progressivos
programa_completo(100)
programa_completo(1000)
programa_completo(5000)
