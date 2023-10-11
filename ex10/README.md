O objetivo deste trabalho é implementar quatro tipos diferentes de buscas em séries temporais.
Cada busca será implementada como uma função diferente, a saber:

find\_double\_slope(S): encontra o primeiro índice N dentro da serie temporal S em que o elemento na posição N é duas ou mais vezes maior que o elemento na posição N-1.
Em outras palavras, S[N] > 2*S[N-1], e para todo elemento M < N, S[M] <= 2*S[M-1].

find\_increasing\_slope(S, L): encontra o primeiro índice N dentro da serie temporal S a partir do qual existe uma sequencia crescente de L ou mais elementos.
Em outras palavras, S[N] > S[N-1] > S[N-2] > ... > S[N-L+1], e não é o caso que essa propriedade aconteça antes, para qualquer M < N.

find\_high\_avg\_slope(S, A): encontra o primeiro índice N em que a media da série temporal S (vista até N) ultrapassa o limiar A.
Em outras palavras, (S[0] + S[1] + ... + S[N])/N > A, e tal propriedade não ocorre antes, para qualquer M < N.

find\_repeated\_element\_slope(S): encontra o primeiro índice N tal que S[N] == S[X], para algum X < N, e tal propriedade não acontece antes, para qualquer M < N.
Em outras palavras, encontra o primeiro índice de um elemento repetido em S.

É importante notar que os índices começam em zero. Assim, o primeiro elemento da série temporal S é S[0]; o segundo elemento é S[1]; e assim por diante.

## Usando Builders
Você pode simplesmente implementar cada uma dessas quatro funções a partir de primeiros princípios (sem reusar qualquer código).
Contudo, você pode usar também a infraestrutura já disponível no trabalho para construir scanners, implementando a técnica discutida na aula sobre Slope Search.
Por exemplo, abaixo temos uma implementação de find\_double\_slope() baseada em um construtor de scanners.
Esse construtor, chamado double\_slope\_builder, constrói um scanner que encontra o elemento N tal que S[N] > 2\*S[N-1].

 fig01

Para implementar um construtor (a função double\_slope\_builder acima), basicamente você precisa definir cinco componentes, a saber:

- Uma class que extende NamedTuple. Essa classe precisa ter no mínimo dois campos: idx e prev. O campo idx é o índice do elemento que está sendo retornado, e prev é o valor acumulado até aquele momento.
- stop\_condition (function): a função que determina quando a busca chegou ao fim. Esse acumulador precisa ter prev igual a None e idx igual ao índice que é a resposta da busca.
- next\_accumulator (function): a função que produz o proximo acumulador da busca.
- gen\_stop\_condition (function): a função que produz o acumulador que denota o fim da busca.
- initial\_accumulator (NamedTuple): o acumulador inicial da busca.

Esses componentes estão descritos na figura abaixo.
Essa figura mostra como um scanner pode ser construído.
Nesse caso, estamos construindo um scanner que encontra o índice N da série temporal S tal que S[N] > 2\* S[N-1].
Veja que todo scanner precisa definir uma classe para os acumuladores.
Essa classe precisa ter, no mínimo, dois campos: idx e prev.
Veja também que as funções do scanner recebem, além do acumulador acc, um elemento e.
Esse elemento é uma tupla com dois campos. O primeiro é o índice do elemento na série, e o segundo é o próprio elemento:

fig02

Caso opte por usar os builders (e isso realmente facilita a resolução do trabalho!), busque entender como funciona a função slope\_search().
A figura abaixo contém uma breve descrição da função, mostrando dados intermediários que são produzidos durante a execução dela:

fig03
