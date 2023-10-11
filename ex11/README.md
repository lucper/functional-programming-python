A programação dinâmica é uma metodologia de desenvolvimento de algoritmos, que busca deconstruir um problema em problemas menores.
A solução ótima dos problemas menores é usada para encontrar uma solução ótima do problema alvo.
Um componente chave da programação dinâmica é a capacidade de salvar resultados parciais, isso é, dos problemas menores, durante a construção da solução final do problema alvo.
Essa capacidade, a memoização, é muito importante, pois os subproblemas são superpostos, isso é, durante a construção da solução do problema alvo, os mesmos subproblemas costumam ser resolvidos muitas vezes.
Neste trabalho prático, você deverá resolver três problemas clássicos de programação dinâmica, a saber:

num\_coins(N, coins): dado um conjunto de valores inteiros "coins", encontre o menor número desses valores que produza a soma N.
Note que repetições do mesmo inteiro são aceitas.
Por exemplo, num\_coins(10, {1, 2, 3}) é 4, pois temos que 3 + 3 + 3 + 1 = 10.

num\_ways(N, coins): dado um conjunto de valores inteiros "coins", encontre o número de maneiras diferentes de conseguirmos obter a soma N a partir de combinações deles.
Novamente, note que repetições de inteiros são aceitas.
Por exemplo, num\_ways(3, {1, 2}) é dois, pois temos as seguintes formas de obter o inteiro três: {1+1+1, 1+2}.

longest\_increasing\_subsequence(s): encontra o tamanho da maior sequência crescente de caracteres na string s.
Por exemplo: longest\_increasing\_subsequence("badceb") = 3, pois temos a sequência a-c-e (ou a sequência a-d-e, ou b-d-e, etc).
