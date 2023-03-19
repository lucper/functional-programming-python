from functools import reduce

def firstChars(L):
    """ Maps strings in L to a list with the first character of each string.
    For instance:
    >>> list(firstChars([]))
    []
    >>> list(firstChars(['python']))
    ['p']
    >>> list(firstChars(['python', 'is', 'pythy']))
    ['p', 'i', 'p']
    """
    return map(lambda x: x[0], L)

def sum(L):
    """ Sums the elements in L
    For instance:
    >>> sum([])
    0
    >>> sum([1])
    1
    >>> sum([1,2,3])
    6
    """
    return reduce(lambda x,y: x + y, L) if L else 0

def avg(L):
    """ Returns the average of the elements in L
    For instance:
    >>> avg([])
    0
    >>> avg([1])
    1.0
    >>> avg([1,2])
    1.5
    >>> avg([1,2,3])
    2.0
    """
    return sum(L) / len(L) if L else 0

def maxString(L):
    """ Returns the largest string in L.
    When a tie occurs, return the first string.
    Undefined for empty lists.
    For instance:
    >>> maxString(['is'])
    'is'
    >>> maxString(['python', 'is', 'pythy'])
    'python'
    >>> maxString(['banana', 'python', 'is'])
    'banana'
    """
    return max(L, key=len)

def add2Dict(D, N, S):
    """ Insere a string S na lista associada ao inteiro N dentro
    do dicionario D.
    Por exemplo, se D = {1: ['b'], 2: ['xd'], 3: ['abc']}, entao,
    add2Dict(D, 2, 'ww') produz o novo dicionario:
    {1: ['b'], 2: ['xd', 'ww'], 3: ['abc']}
    Voce pode usar essa funcao para completar buildLenFreq
    """
    D[N] = D[N] + [S] if N in D else [S]
    return D

def buildLenFreq(L):
    """ Esta funcao constroi um dicionario que associa inteiros a listas com
    palavras daquele tamanho. Por exemplo:
    ins(['abc', 'xd', 'b', 'xxx']) = {1: ['b'], 2: ['xd'], 3: ['abc', 'xxx']}
    """
    return None

def incValue(D, N):
    """Esta funcao incrementa o valor associado a chave N dentro do dicionario
    D. Por exemplo, se D = {1: 2, 2: 4, 3: 11}, entao
    Voce pode usar essa funcao para completar countFirsts
    """
    D[N] = D[N] + 1 if N in D else 1
    return D

def countFirsts(L):
    """ Conta o numero de ocorrencias do primeiro caracter de cada string em L.
    Por exemplo, countFirsts(['python', 'is', 'pythy']) === {'i': 1, 'p': 2}
    Note que essa funcao retorna um dicionario com cada caracter associada ao
    numero de strings que comecam com aquele caracter.
    """
    return None

def mostCommonFirstChar(L):
    """ Retorna a letra mais comum entre as primeiras letras de strings em L.
    Por exemplo:
    mostCommonFirstChar(['python', 'is', 'pythy']) === 'p'
    """
    return 'Z'
