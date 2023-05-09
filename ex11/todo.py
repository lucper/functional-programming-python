def num_coins(N, coins):
    """O numero minimo de moedas cujos valores estao em coins que de soma N.

    Exemplos:
    * num_coins(10, {1, 3, 4}) == 3
    * num_coins(10, [1, 2, 4]) == 3
    * num_coins(11, [1, 4, 5]) == 3
    * num_coins(21, [1, 4, 5]) == 5
    * num_coins(21, range(1, 4, 2)) == 7

    Parameters:
        N (int): inteiro que deve ser construido como uma soma de moedas.
        coins (int iter): conjunto com os valores de moedas.

    Returns:
        integer denoting minimum number of coints that add up to x.
    """
    # TODO: implementar essa funcao.
    return 0

def num_ways(N, coins):
    """Numero de formas diferentes de construir N como soma de moedas em coins.

    Exemplos:
    * num_ways(10, {1, 3, 4}) == 64
    * num_ways(10, [1, 2, 4]) == 64
    * num_ways(11, [1, 4, 5]) == 41
    * num_ways(21, [1, 4, 5]) == 2252
    * num_ways(21, range(1, 4, 2)) == 1873

    Parameters:
        N (int): inteiro que deve ser construido como uma soma de moedas.
        coins (int iter): conjunto com os valores de moedas.

    Returns:
        int que representa o numero de formas de somarmos moedas ateh x.
    """
    # TODO: implementar essa funcao.
    return 0

def longest_increasing_subsequence(s):
    '''Longest Increasing Subsequence.

    Essa funcao encontra o tamanho da maior subsequencia de caracteres
    dentro da string. Exemplos:
    1. longest_increasing_subsequence("") == 0 -> string vazia
    2. longest_increasing_subsequence("ebfacg") == 3 -> b-c-g
    3. longest_increasing_subsequence("eafbca") == 3 -> a-b-c
    4. longest_increasing_subsequence("eafbcah") == 4 -> a-b-c-h

    Parameters:
        s (str): string que representa a sequencia de caracteres.

    Returns:
        int que representa a maior subsequencia crescente (e nao contigua) de
        caracteres dentro de s
    '''
    # TODO: implementar essa funcao.
    return 0