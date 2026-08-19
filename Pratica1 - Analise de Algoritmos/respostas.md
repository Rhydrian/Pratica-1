# Prática de Laboratório 01 - Introdução à Análise de Algoritmos

Dupla: ____________________ / ____________________

Todos os tempos abaixo foram medidos rodando os códigos em Python 3 no notebook usado
na prática. Os valores absolutos mudam de máquina para máquina, mas a proporção entre
eles é o que interessa.

---

## Missão 1 - A Corrida Assintótica (O(n) vs O(n²))

Saída obtida:

```
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

No algoritmo linear, praticamente nada. O tempo é tão baixo que o `time.time()` do
Windows nem tem resolução suficiente para registrar, e por isso aparece 0.00000. Em
teoria o tempo multiplicou por 10 junto com o n, só que 10 vezes quase zero continua
quase zero.

Já no quadrático o salto foi de 0.031 s para 2.808 s, ou seja, cerca de 90 vezes mais
lento. Isso bate com o esperado: multiplicar n por 10 multiplica n² por 100, e a
diferença para 100 vem só de ruído de medição e do custo fixo de chamar a função. De
1.000 para 5.000 (5 vezes) o tempo subiu ~23 vezes, que também é bem próximo de 5² = 25.

**2. E com n = 100.000?**

O linear rodou em 0.003 s, sem esforço nenhum. O quadrático levou 398.13 s, ou seja,
mais de 6 minutos e meio, e durante toda a execução o terminal fica parado sem imprimir
nada, dando a impressão de que o programa travou.

```
Linear   n = 100000 | Tempo: 0.00300 segundos
Quadrat. n = 100000 | Tempo: 398.13048 segundos
```

Comparando com o teste anterior: n foi de 10.000 para 100.000, multiplicou por 10, e o
tempo foi de 2.8 s para 398 s, multiplicou por 142. O esperado pela teoria era 100 vezes;
a diferença para mais provavelmente vem da máquina esquentando e reduzindo o clock ao
longo dos quase 7 minutos de execução, mas a ordem de grandeza é a prevista.

O motivo é que o número de operações é n² = 10.000.000.000, dez bilhões de somas. É
esse o problema dos algoritmos O(n²): o trabalho não cresce junto com a entrada, ele
cresce com o quadrado dela. Cada vez que o volume de dados dobra, o tempo quadruplica.
Então mesmo que a máquina seja rápida, sempre existe um n a partir do qual o programa
simplesmente para de responder em tempo útil. Um sistema com 100 mil registros já é
pequeno para os padrões de hoje, e mesmo assim o algoritmo quadrático precisou de
minutos onde o linear precisou de milissegundos.

---

## Missão 2 - Caçando o Pior e o Melhor Caso

Saída obtida:

```
Gerando vetor na memoria...
Vetor gerado!

Tempo Cenario A (Buscando 0): 0.000000 s
Tempo Cenario B (Buscando -1): 0.130187 s
```

**1. Houve diferença no tempo? Por quê?**

Houve, e enorme. O cenário A terminou instantaneamente e o B levou 0.13 s para o mesmo
vetor de 10 milhões de posições.

A diferença não está no tamanho da instância, que é idêntico nos dois testes, e sim no
alvo procurado. Buscando o 0, o `for` compara o primeiro elemento, encontra e já cai no
`return True`, fazendo uma única comparação. Buscando o -1, que não existe no vetor, o
laço é obrigado a percorrer os 10 milhões de elementos até acabar a lista e só então
retorna `False`.

Isso mostra que o tempo de execução não depende só de n. Instâncias de mesmo tamanho
podem exigir quantidades muito diferentes de operações, dependendo de como os dados
estão organizados em relação ao que se procura.

**2. Qual cenário é T_min(n) e qual é T_max(n)?**

O cenário A é o melhor caso, T_min(n). O elemento procurado está logo na primeira
posição, o laço executa uma iteração só e o custo é constante, O(1), independente do
tamanho do vetor.

O cenário B é o pior caso, T_max(n). Como o alvo não está na lista, não existe nenhum
`return` antecipado que interrompa o laço, então ele roda as n iterações completas. O
custo é proporcional a n, ou seja, O(n). O mesmo pior caso aconteceria se o elemento
estivesse exatamente na última posição.

Vale notar que a análise assintótica normalmente trabalha com o pior caso justamente
por isso: ele é o único que dá garantia. O melhor caso aqui depende de sorte.

---

## Missão 3 - Identificando o Gargalo (O(n) + O(n²) = ?)

Saída obtida:

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

(Para n = 100 os tempos ficaram abaixo da precisão do `time.time()`, então repetimos essa
medição com `time.perf_counter()` para conseguir ver a diferença.)

**1. Para n = 100, qual etapa demorou mais?**

A Etapa 1, a linear. Ela ficou em 0.00143 s contra 0.00032 s da quadrática, mais ou
menos 4,5 vezes mais lenta. Faz sentido pela contagem de operações: a Etapa 1 executa
100 × 500 = 50.000 somas, enquanto a Etapa 2 executa 100² = 10.000. Para n pequeno, a
constante 500 pesa mais do que a ordem de crescimento.

**2. Para n = 5000, qual etapa dominou?**

A Etapa 2, a quadrática, sem discussão. Ela sozinha respondeu por 0.699 s dos 0.772 s
totais, cerca de 90% do tempo. Agora são 25.000.000 de operações contra 2.500.000 da
Etapa 1, uma diferença de 10 vezes.

Dá até para calcular onde a virada acontece: as duas etapas se igualam quando
n × 500 = n², isto é, em n = 500. Abaixo disso a linear manda, acima disso a quadrática
assume e nunca mais devolve a liderança. Nos testes isso aparece direitinho, em n = 1000
a quadrática já passou a linear.

**3. Por que otimizar gargalos quadráticos deve ser prioridade?**

Porque a constante multiplicativa não muda a ordem de crescimento. Aquele 500 da Etapa 1
parece enorme, mas ele é um fator fixo: por maior que seja, existe um n a partir do qual
o n² passa por cima. É exatamente isso que a análise assintótica diz quando afirma que
O(n) + O(n²) = O(n²), o termo de maior grau domina.

Na prática, se esse sistema estivesse travando em produção, otimizar a Etapa 1 seria
perda de tempo. Em n = 5000 ela representa menos de 10% do tempo total, então mesmo que
conseguíssemos deixá-la infinitamente rápida, o ganho máximo seria de uns 9%, e essa
fatia só encolhe conforme a base de dados cresce. O sistema continuaria travando.

Mexer na Etapa 2 é o oposto: trocar um algoritmo O(n²) por um O(n log n) ou O(n) ataca a
causa do problema e o ganho aumenta junto com o volume de dados, em vez de diminuir. Por
isso a análise assintótica é útil antes mesmo de sair medindo, ela aponta onde vale a
pena investir esforço de otimização e onde não adianta.
