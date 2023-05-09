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
    if not q:
        return -1
    elif not s:
        return 0
    else:
        occurs = 0
        for i in range(len(s) - len(q) + 1):
            if s[i:len(q)+i] == q:
                occurs += 1
        return occurs

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
    def num_to_str(n):
        if n % 105 == 0:
            return 'kanguru'
        elif n % 35 == 0:
            return 'guru'
        elif n % 21 == 0:
            return 'kanru'
        elif n % 15 == 0:
            return 'kangu'
        elif n % 7 == 0:
            return 'ru'
        elif n % 5 == 0:
            return 'gu'
        elif n % 3 == 0:
            return 'kan'
        elif not (n % 3 == 0 and n % 5 == 0 and n % 7 == 0):
            return str(n)
    return [num_to_str(i) for i in L]
