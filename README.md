# Soluções para Desafios Técnicos

## 3. Valor da Variável `SOMA`

O trecho de código abaixo calcula o valor da variável `SOMA` após o processamento:

```c
int INDICE = 12, SOMA = 0, K = 1;
while (K < INDICE) {
    K = K + 1;
    SOMA = SOMA + K;
}
printf("%d", SOMA);
```

# Resultado
Ao final do processamento, o valor da variável SOMA será 91

#Descobrindo a lógica e completando o próximo elemento:
- a) 1, 3, 5, 7, ...: Sequência de números ímpares.
Próximo número: 9.

- b) 2, 4, 8, 16, 32, 64, ...: Sequência onde cada número é o dobro do anterior.
Próximo número: 128.

- c) 0, 1, 4, 9, 16, 25, 36, ...: Sequência de quadrados perfeitos (0², 1², 2², 3², ...).
Próximo número: 49.

- d) 4, 16, 36, 64, ...: Sequência de números pares elevados ao quadrado (2², 4², 6², 8², ...).
Próximo número: 100.

- e) 1, 1, 2, 3, 5, 8, ...: Sequência de Fibonacci.
Próximo número: 13.

- f) 2, 10, 12, 16, 17, 18, 19, ...: Sequência de números começando com 2 e depois números entre 10 e 19.
Próximo número: 20.

# Resolvendo o problema dos interruptores:
Dado o problema de descobrir qual interruptor controla cada lâmpada em três salas diferentes:

Ligue o primeiro interruptor e aguarde alguns minutos.
Desligue o primeiro interruptor e ligue o segundo.
Vá até a sala e observe as lâmpadas:
- A lâmpada ligada pertence ao segundo interruptor.
- A lâmpada que está quente, mas apagada pertence ao primeiro interruptor.
- A lâmpada fria e apagada pertence ao terceiro interruptor.
