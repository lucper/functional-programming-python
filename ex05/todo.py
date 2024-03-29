from functools import reduce

def delInitials(L):
    """Esta funcao recebe uma lista de strings L, e retorna uma string S.
    S contem os elementos de L que possuem mais de um caracter, sempre com a
    primeira letra maiuscula. Ex.:
    >>> delInitials(['Fer', 'mag', 'Q', 'pereira'])
    ['Fer', 'Mag', 'Pereira']
    """
    return [s.capitalize() for s in L if len(s) > 1]

def everyOccurrence(S, Q):
    """Esta funcao retorna uma lista L formada pelos indices de caracteres na
    string S que existem tambem na string Q.
    Para resolver esse exercicio, voce pode usar a funcao enumerate, ex.:
    [(a, b) for a, b in enumerate('abc')] == [(0, 'a'), (1, 'b'), (2, 'c')]
    Outra dica eh usar combinacoes de 'for' em compreencoes de lista, ex.:
    [(a, b) for a in 'xyz' for b in [1, 2]] ==
    [('x', 1), ('x', 2), ('y', 1), ('y', 2), ('z', 1), ('z', 2)]
    Ex:
    >>> everyOccurrence('Fernando', 'abcde')
    [1, 4, 6]
    >>> everyOccurrence('xaxbxaxyza', 'abcde')
    [1, 3, 5, 9]
    """
    return [i for i, s in enumerate(S) if s in Q]

def factors(N):
    """Retorna uma lista com os divisores do numero N, exceto 1 e N.
    Exemplos:
    >>> factors(6)
    [2, 3]
    >>> factors(10)
    [2, 5]
    >>> factors(12)
    [2, 3, 4, 6]
    >>> factors(28)
    [2, 4, 7, 14]
    """
    return [k for k in range(2, (N // 2) + 1) if N % k == 0]

def isPerfect(N):
    """N eh perfeito se a soma de seus fatores (exceto ele mesmo) eh N.
    obs.: se for utilizar "factors" para resolver esse exercicio, lembre-se,
    que aquela funcao nao retorna o '1' como fator.
    Exemplos:
    >>> isPerfect(6)
    True
    >>> isPerfect(10)
    False
    >>> isPerfect(12)
    False
    >>> isPerfect(28)
    True
    """
    import operator
    #return sum(k for k in range(1, N) if N % k == 0) == N
    return reduce(operator.add, factors(N)) == N - 1
