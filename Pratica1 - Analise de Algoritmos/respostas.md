# Prática de Laboratório 01 - Introdução à Análise de Algoritmos

Dupla: Diana da Silva e Rhydrian Coutinho



## Missão 1 - A Corrida Assintótica (O(n) vs O(n²))

Saída obtida:


--- Testando Algoritmo Linear O(n) ---
n =  1000 | Tempo: 0.00100 segundos
n =  5000 | Tempo: 0.00000 segundos
n = 10000 | Tempo: 0.00000 segundos

--- Testando Algoritmo Quadratico O(n^2) ---
n =  1000 | Tempo: 0.03100 segundos
n =  5000 | Tempo: 0.70630 segundos
n = 10000 | Tempo: 2.80789 segundos
```

**1. O que aconteceu quando n passou de 1.000 para 10.000?**

No algoritmo linear, o tempo continuou muito baixo e apareceu como 0.00000 segundos nos testes. Teoricamente, aumentando n em 10 vezes, o tempo também aumenta aproximadamente 10 vezes.

No algoritmo quadrático, o tempo aumentou bastante, passando de 0.031 segundos para 2.80789 segundos. Isso acontece porque o número de operações cresce com n².

**2. E com n = 100.000?**

O algoritmo linear continuou rápido, levando apenas 0.003 segundos. Já o quadrático levou 398.13048 segundos, mais de 6 minutos.
Isso acontece porque com n = 100.000 são cerca de 10 bilhões de operações. Por isso, algoritmos O(n²) podem ficar muito lentos quando o tamanho da entrada aumenta.

```
Linear   n = 100000 | Tempo: 0.00300 segundos
Quadrat. n = 100000 | Tempo: 398.13048 segundos
```



---

## Missão 2 - Caçando o Pior e o Melhor Caso



```

Tempo Cenario A (Buscando 0): 0.000000 s
Tempo Cenario B (Buscando -1): 0.130187 s
```

**1. Houve diferença no tempo? Por quê?**

Sim. Ao procurar o número 0, o programa encontrou o elemento logo na primeira posição e terminou rapidamente.
Já procurando -1, como ele não existe no vetor, o programa precisou percorrer os 10 milhões de elementos.

**2. Qual cenário é T_min(n) e qual é T_max(n)?**

O cenário A, procurando 0, é o melhor caso, Tmin(n), porque o elemento está na primeira posição.

O cenário B, procurando -1, é o pior caso, Tmax(n), porque o elemento não existe e o programa precisa percorrer o vetor inteiro.

---

## Missão 3 - Identificando o Gargalo (O(n) + O(n²) = ?)


```
--- Testando para n = 100 ---
Tempo Etapa 1 (Linear): 0.00143 s
Tempo Etapa 2 (Quadratica): 0.00032 s

--- Testando para n = 1000 ---
Tempo Etapa 1 (Linear): 0.01704 s
Tempo Etapa 2 (Quadratica): 0.03213 s
Tempo Total: 0.04916 s

--- Testando para n = 5000 ---
Tempo Etapa 1 (Linear): 0.07315 s
Tempo Etapa 2 (Quadratica): 0.69911 s
Tempo Total: 0.77226 s
```


**1. Para n = 100, qual etapa demorou mais?**

A Etapa 1 demorou mais. Ela levou 0.00143 segundos, enquanto a Etapa 2 levou 0.00032 segundos.
Isso acontece porque, nesse caso, a Etapa 1 faz 50.000 operações e a Etapa 2 faz 10.000.
**2. Para n = 5000, qual etapa dominou?**

A Etapa 2 dominou o tempo de execução. Ela levou 0.69911 segundos, enquanto a Etapa 1 levou 0.07315 segundos.
Isso acontece porque a Etapa 2 faz 25 milhões de operações, enquanto a Etapa 1 faz 2,5 milhões

**3. Por que otimizar gargalos quadráticos deve ser prioridade?**

Porque o algoritmo O(n²) cresce muito mais rápido que o O(n). Quando a quantidade de dados aumenta, ele passa a consumir uma parte cada vez maior do tempo de execução.
Por isso, se o sistema estiver lento, é melhor começar pela parte quadrática, pois ela é a principal responsável pelo aumento do tempo.
