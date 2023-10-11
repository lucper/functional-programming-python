O objetivo deste trabalho é implementar um interpretador de uma linguagem de montagem (linguagem assembly). Nossa linguagem terá as seguintes instruções:

```text
const x n  | x := n ;; n eh numero inteiro
add x a b  | x := a + b
mul x a b  | x := a * b
and x a b  | x := a && b
grt x a b  | x := a > b ? 1 : 0
bez x L  | if x == 0 goto L
jump L  | goto L
```

A título de exemplo, o programa abaixo calcula o fatorial de 10:

```text
const n 10
const i 1
const one 1
const fact 1
grt cond n i
bez cond 9
mul fact fact i
add i i one
jump 4
```

O código que interpreta cada instrução é criado por um closure diferente. Por exemplo, abaixo segue a implementação do código que interpreta uma instrução de adição:

```python
def make\_add(lhs, op0, op1):
    def eval(env, instructions):
        v0 = env[op0]
        v1 = env[op1]
        env[lhs] = v0 + v1
    return eval
```

Veja que cada interpretador de instrução é uma função que recebe dois parâmetros: um "ambiente" env e o próprio programa "instructions" (um container de instruções). Esse ambiente (a variável env) é uma tabela (um dicionário) que associa nomes de variáveis a valores. Cada chave do dicionário é uma string, e cada valor é um número inteiro. Algumas instruções alteram essa tabela, como a própria instrução add, vista acima. Outras instruções modificam o chamado "contador de programa", isso é, o indicador da próxima instrução que será buscada. Por exemplo, abaixo vemos a implementação da instrução bez (branch if equal zero):

```python
def make\_bez(pred, goto\_address):
    def eval(env, instructions):
        val = env[pred]
        if val == 0:
            instructions.set\_next\_instruction(int(goto\_address))
    return eval
```

Neste exercício, você deverá implementar as sete instruções que compõem nossa linguagem. Essas instruções devem ser implementadas como closures, no arquivo todo.py. Os testes acontecem em um arquivo Driver.py. Você pode dar uma olhada no arquivo Driver.py (para ver como switches funcionais são implementados, por exemplo). Abaixo vemos alguns programas (área rosa), e os valores que eles retornam (área amarela, logo abaixo):

fig01
