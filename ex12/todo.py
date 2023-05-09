def all_subs(s, q):
    """Conta a quantidade de ocorrencias da string q dentro da string s.

    Parameters
    ----------
        s (str): a string que servirah de base para a busca.
        q (str): a substring que serah procurada.

    Returns:
    --------
        A quantidade de vezes em que q ocorre dentro de s. Caso a string q
        seja vazia, entao o valor retornado serah -1

    Example
    >>> all_subs('ababacababa', 'aba')
    4

    >>> all_subs('ababa', 'abba')
    0

    >>> all_subs('', 'a')
    0

    >>> all_subs('ababa', '')
    -1
    """
    #TODO
    return 0

def kanguru(L):
    """Mapeia cada numero 'n' em L para '(kan)?(gu)?(ru)?' ou o proprio 'n'

    Exemplos:
    >>> kanguru([])
    []

    >>> kanguru([9, 10, 11, 21, 23, 105])
    ['kan', 'gu', '11', 'kanru', '23', 'kanguru']

    >>> kanguru(range(2, 8))
    ['2', 'kan', '4', 'gu', 'kan', 'ru']

    >>> kanguru([3, 5, 7, 15, 21, 35, 105, 2])
    ['kan', 'gu', 'ru', 'kangu', 'kanru', 'guru', 'kanguru', '2']
    """
    #TODO
    return L