""" Este arquivo contem a implementacao de diferentes buscas em series
    temporais. O objetivo deste trabalho eh terminar essas implementacoes. Voce
    pode trabalhar diretamente no codigo dessas quatro funcoes:

    * find_double_slope,
    * find_increasing_slope,
    * find_high_avg_slope e
    * find_repeated_element_slope

    Mas eh muito mais facil resolve-las implementando os construtores de
    scanner. Voce nao precisa implementar esses construtores, contudo (mas
    realmente, isso facilita a resolucao do trabalho). Caso opte por
    implementar os scanners, suas implementacoes das quatro buscas ficaram
    assim:

    def find_double_slope(serie_temporal):
        return slope_search(serie_temporal, double_slope_builder())

    def find_increasing_slope(serie_temporal, sec_size):
        return slope_search(serie_temporal, increasing_slope_builder(sec_size))

    def find_high_avg_slope(serie_temporal, avg):
        return slope_search(serie_temporal, high_avg_slope_builder(avg))

    def find_repeated_element_slope(serie_temporal):
        return slope_search(serie_temporal, repeated_element_slope_builder())
"""

from typing import NamedTuple
from itertools import dropwhile, accumulate

def make_scanner( \
        stop_condition, \
        next_accumulator, \
        gen_stop_condition, \
        initial_accumulator):
    """Funcao builder que cria scanners para executar buscas em series
    temporais.

    Essa funcao recebe quatro parametros, tres dos quais sao funcoes. Essas
    funcoes possuem dois argumentos: um acumulador e o elemento corrente da
    serie temporal. O acumulador eh um registro com no minimo dois campos:
    prev e idx. O primeiro eh o estado da busca, e o segundo eh o indice da
    serie temporal que estah sendo analisado.

    Parameters:
    -----------
    stop_condition (function): a expressao lambda que determina quando a busca
    chegou ao fim.

    next_accumulator (function): a funcao que produz o proximo acumulador da
    busca.

    gen_stop_condition (function): a funcao que produz o acumulador que denota
    o fim da busca. Esse acumulador precisa ter prev igual a None e idx igual
    ao indice que eh a resposta da busca.

    initial_accumulator (NamedTuple): o acumulador inicial da busca. Geralmente
    eh um acumulador com idx igual a -1, por exemplo.

    Returns:
    -------
    function: uma funcao que implementa um scanner. Um scanner eh uma funcao
    que recebe dois argumentos: um acumulador e o elemento corrente da serie
    temporal. O scanner verifica se o elemento corrente atinge uma certa
    propriedade em relacao ao acumulador.
    """
    def check_if_cond(acc, e):
        if stop_condition(acc, e):
            return gen_stop_condition(acc, e)
        else:
            return next_accumulator(acc, e)
    check_if_cond.initial = initial_accumulator
    return check_if_cond

def slope_search(numbers, scanner):
    """Essa funcao encontra o primeiro indice em que alguma propriedade
    reconhecida pelo scanner se torna verdadeira na serie temporal.

    Parameters:
    -----------
    numbers (list): uma lista de numeros inteiros que denota a serie temporal.

    scanner (function): uma funcao scanner, que recebe acumulador e elemento
    e determina quando a relacao entre acumulador e elemento representa o ponto
    de busca na serie temporal.

    Returns:
    --------
    int: O primeiro indice da serie temporal em que a propriedade reconhecida
    pelo scanner se torna verdadeira, ou -1 se tal indice nao existe.
    """
    indices = list(enumerate(numbers))
    prefixes = accumulate(indices, scanner, initial=scanner.initial)
    head = dropwhile(lambda acc: acc.prev != None, prefixes)
    try:
        return next(head).idx
    except StopIteration:
        return -1

def double_slope_builder():
    """Monta um scanner que encontra o primeiro indice N da serie
    temporal em que o elemento na posicao N eh duas ou mais vezes maior que o
    elemento na posicao N-1.

    Exemplos:
    [4, 2, 5, 1, 6] retorna 2 (Lembre-se que a primeira posicao eh zero!)
    [1, 2, 3] retorna -1 (a relacao eh de maior que, nao de maior ou igual)
    [0, 1, 2, 3] retorna 1, pois 1 > 2*0

    Returns
    -------
    function: um scanner que reconhece o incremento de duas vezes ou mais.
    """
    class Accumulator(NamedTuple):
        idx: int
        prev: int
    st_cond = lambda acc, e: e[1] > 2 * acc.prev
    next_acc = lambda _, e: Accumulator(e[0], e[1])
    gen_st_cond = lambda _, e: Accumulator(e[0], None)
    initial = Accumulator(-1, float('inf'))
    return make_scanner(st_cond, next_acc, gen_st_cond, initial)

def increasing_slope_builder(size):
    """Monta um scanner que encontra o indice inicial da primeira sequencia
    crescente com 'size' ou mais elementos.

    Por exemplo, caso 'size' seja 3, teremos:
    [2, 1, 2, 3, 4, 1, 2, 3, 4] retorna 1 (devido a seq "1, 2, 3")
    [2, 2, 1, 2, 3, 1] retorna 2
    [1, 2, 1, 2, 1] retorna -1

    Parameters:
    -----------
    size (int): o tamanho minimo da sequencia crescente.

    Returns
    -------
    function: um scanner que reconhece a sequencia crescente.
    """
    class Accumulator(NamedTuple):
        idx: int
        sec_size: int
        prev: int
    st_cond = lambda acc, e: e[1] > acc.prev and acc.sec_size + 1 >= size  # !!!
    def next_acc(acc, e):
        has_increased = e[1] > acc.prev
        new_sec_size = acc.sec_size + 1 if has_increased else 1
        new_idx = acc.idx if has_increased else e[0]
        return Accumulator(idx=new_idx, sec_size=new_sec_size, prev=e[1])
    gen_st_cond = lambda acc, _: Accumulator(idx=acc.idx, sec_size=acc.sec_size + 1, prev=None)
    initial = Accumulator(idx=-1, sec_size=1, prev=float('inf'))
    return make_scanner(st_cond, next_acc, gen_st_cond, initial)

def high_avg_slope_builder(avg):
    """Monta um scanner que encontra o primeiro indice N em que a media da
    serie temporal (vista ateh N) ultrapassa o limiar 'avg'.

    Por exemplo, caso 'avg' seja 2, teremos:
    [1, 2, 3, 4, 5] retorna 3, pois avg(1, 2, 3, 4) == 2.5, que eh maior que 2,
    mas avg(1, 2, 3) = 2, que nao eh maior que 2.

    Parameters:
    -----------
    avg (int): o limiar da media buscada.

    Returns
    -------
    function: um scanner que reconhece a sequencia crescente.
    """
    class Accumulator(NamedTuple):
        idx: int
        qty: int    # number of elements so far
        prev: int   # sum of elements so far
    st_cond = lambda acc, e: (e[1] + acc.prev) / (acc.qty + 1) > avg
    next_acc = lambda acc, e: Accumulator(idx=e[0], qty=acc.qty + 1, prev=acc.prev + e[1])
    gen_st_cond = lambda acc, e: Accumulator(idx=e[0], qty=acc.qty + 1, prev=None)
    initial = Accumulator(idx=-1, qty=0, prev=0)
    return make_scanner(st_cond, next_acc, gen_st_cond, initial)

def repeated_element_slope_builder():
    """Monta um scanner que encontra o indice do primeiro termo repetido na
    serie temporal.

    Por exemplo:
    [0, 1, 2, 3, 0, 1, 2] retorna 4, pois o elemento nas posicoes zero e quatro
    sao iguais.

    Returns:
    --------
    function: um scanner que reconhece elementos repetidos.
    """
    class Accumulator(NamedTuple):
        idx: int
        prev: set
    st_cond = lambda acc, e: e[1] in acc.prev
    next_acc = lambda acc, e: Accumulator(idx=e[0], prev=acc.prev.union({e[1]}))
    gen_st_cond = lambda _, e: Accumulator(idx=e[0], prev=None)
    initial = Accumulator(idx=-1, prev=set())
    return make_scanner(st_cond, next_acc, gen_st_cond, initial)


def find_double_slope(serie_temporal):
    """Encontra o primeiro indice N dentro da serie temporal em que o elemento
    na posicao N eh duas ou mais vezes maior que o elemento na posicao N-1.

    Exemplos:
    [4, 2, 5, 1, 6] retorna 2 (Lembre-se que a primeira posicao eh zero!)
    [1, 2, 3] retorna -1 (a relacao eh de maior que, nao de maior ou igual)
    [0, 1, 2, 3] retorna 1, pois 1 > 2*0

    Parameters:
    -------
    serie_temporal (list): a lista de inteiros que representa a serie temporal.

    Returns:
    --------
    int: o indice em questao ou -1 caso tal indice nao exista.
    """
    return slope_search(serie_temporal, double_slope_builder())

def find_increasing_slope(serie_temporal, sec_size):
    """Encontra o primeiro indice N dentro da serie temporal a partir do qual
    existe uma sequencia crescente de sec_size ou mais elementos.

    Por exemplo, caso 'sec_size' seja 3, teremos:
    [2, 1, 2, 3, 4, 1, 2, 3, 4] retorna 1 (devido a seq "1, 2, 3")
    [2, 2, 1, 2, 3, 1] retorna 2
    [1, 2, 1, 2, 1] retorna -1

    Parameters:
    -------
    serie_temporal (list): a lista de inteiros que representa a serie temporal.

    sec_size (int): o tamanho minimo da sequencia crescente.

    Returns:
    --------
    int: o indice em questao ou -1 caso tal indice nao exista.
    """
    return slope_search(serie_temporal, increasing_slope_builder(sec_size))

def find_high_avg_slope(serie_temporal, avg):
    """Encontra o primeiro indice N em que a media da serie temporal (vista
    ateh N) ultrapassa o limiar 'avg'.

    Por exemplo, caso 'avg' seja 2, teremos:
    [1, 2, 3, 4, 5] retorna 3, pois avg(1, 2, 3, 4) == 2.5, que eh maior que 2,
    mas avg(1, 2, 3) = 2, que nao eh maior que 2.

    Parameters:
    -------
    serie_temporal (list): a lista de inteiros que representa a serie temporal.

    avg (numeric): o limiar de media que estah sendo buscado.

    Returns:
    --------
    int: o indice em questao ou -1 caso tal indice nao exista.
    """
    return slope_search(serie_temporal, high_avg_slope_builder(avg))

def find_repeated_element_slope(serie_temporal):
    """Encontra o indice do primeiro termo repetido na serie temporal.

    Por exemplo:
    [0, 1, 2, 3, 0, 1, 2] retorna 4, pois o elemento nas posicoes zero e quatro
    sao iguais.

    Parameters:
    -------
    serie_temporal (list): a lista de inteiros que representa a serie temporal.

    Returns:
    --------
    int: o indice em questao ou -1 caso tal indice nao exista.
    """
    return slope_search(serie_temporal, repeated_element_slope_builder())
