from functools import reduce

def lastNames(L):
    """Mapeia uma lista de nomes para o ultimo nome de cada item.
    Por exemplo, seja:
    L = [['Antonio', 'Franco'], ['Caius', 'Vitelus'], ['Cristovao', 'Buarque']]
    Entao lastNames(L) == ['Franco', 'Vitelus', 'Buarque']
    >>> list(lastNames([]))
    []
    >>> list(lastNames([['Antonio', 'Franco']]))
    ['Franco']
    >>> list(lastNames([['Antonio', 'Franco'], ['Caius', 'Vitelus'], ['Cristovao', 'Buarque']]))
    ['Franco', 'Vitelus', 'Buarque']
    """
    return map(lambda e: e[-1], L)

def citations(L):
    """Mapeia uma lista de nomes para a primeira letra mais sobrenome.
    Por exemplo, seja:
    L = [['Antonio', 'Franco'], ['Caius', 'Vitelus'], ['Cristovao', 'Buarque']]
    entao citations(L) = ['A. Franco', 'C. Vitelus', 'C. Buarque']
    Note que a primeira letra precisa estar capitalizada.
    >>> list(citations([]))
    []
    >>> list(citations([['Antonio', 'Franco']]))
    ['A. Franco']
    >>> list(citations([['Antonio', 'Franco'], ['Caius', 'Vitelus'], ['Cristovao', 'Buarque']]))
    ['A. Franco', 'C. Vitelus', 'C. Buarque']
    """
    initial = lambda e: e[0].capitalize() + '.'
    return map(lambda e: initial(e[0]) + ' ' + e[-1], L)

def fullCitations(L):
    """Mapeia uma lista de nomes para as iniciais mais o ultimo nome.
    Por exemplo, seja:
    L = [
        ['Antonio', 'Franco', 'Molina'],
        ['Caius', 'vitelus', 'Aquarius'],
        ['cristovao', 'buarque', 'Holanda']]
    entao fullCitations(L) = ['A. F. Molina', 'C. V. Aquarius', 'C. B. Holanda']
    Note que as iniciais precisam estar capitalizada.
    >>> list(fullCitations([]))
    []
    >>> list(fullCitations([['Antonio', 'Franco', 'Molina']]))
    ['A. F. Molina']
    >>> list(fullCitations([['Antonio', 'Franco', 'Molina'], ['Caius', 'Vitelus', 'Aquarius'], ['Cristovao', 'Buarque']]))
    ['A. F. Molina', 'C. V. Aquarius', 'C. Buarque']
    """
    initial = lambda e: e[0].capitalize() + '.'
    initials = lambda e: ' '.join(map(initial, e.split()))
    citation = lambda s: reduce(lambda acc, e: initials(acc) + ' ' + e, s)
    return map(citation, L)
