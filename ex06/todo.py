# Procure usar o pacate itertools para resolver os quatro exercicios deste
# VPL. Embora seja possivel resolver os exercicios sem itertools, este modulo
# facilita a resolucao das questoes (e exercita os conceitos aprendidos no
# curso).
from itertools import *

# The list of week days:
dias = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]

# The list of possible shifts: Day or Night.
periodos = ["D", "N"]

def buildTurns(profs):
    """Esta funcao recebe uma lista profs de profissionais, e constroi uma
    lista de tuplas. Cada tupla possui quatro elementos:
    - Um dia da semana;
    - Um periodo de trabalho (dia ou noite);
    - Um nome de profissional
    - Um indice indicando qual eh aquele turno. O primeiro turno (Seg/D) possui
    indice 1. O segundo turno (Seg/N) possui indice 2, o terceiro turno (Ter/D)
    possui indice 3, e assim por diante.
    """
    turns = product(dias, periodos)
    tXprof = zip(turns, cycle(profs), count(1))
    return ([a, b, c, d] for (a, b), c, d in tXprof)

def printCSV(profs):
    """Esta funcao recebe uma lista de profissionais, e imprime uma tabela
    CSV com os turnos, usando as colunas: indice, dia, periodo e profissional:
    """
    print("indice, dia, periodo, profissional")
    # TODO: imprima o resto do arquivo CSV aqui. Esta rotina devera retornar
    # a string 'fim'. Assim, nao altere o comando de retorno. Insira, logo
    # apos esse comentario, codigo para construir a lista de turnos, e
    # imprimir a tabela CSV.
    print('\n'.join(f'{idx}, {day}, {shift}, {prof}' for day, shift, prof, idx in buildTurns(profs)))
    return 'fim'

def firstDay(profs, prof):
    """Esta funcao imprime o primeiro dia em que trabalha o profissional 'prof'.
    Caso 'prof' nao esteja presente na lista profs, ou nao exista em um turno
    valido, a funcao precisa retornar a string 'Inexistente'
    Exemplos:
    >>> firstDay(['Ana', 'Bruno', 'Camila'], 'Ana')
    'Seg'
    >>> firstDay(['Ana', 'Bruno', 'Camila'], 'Camila')
    'Ter'
    >>> firstDay(['Ana', 'Bruno', 'Camila'], 'Douglas')
    'Inexistente'
    """
    notProf = lambda p: lambda e: e[2] != p
    rest = dropwhile(notProf(prof), buildTurns(profs))
    tup = next(rest, None)
    return tup[0] if tup else "Inexistente"


def countTurns(profs, prof):
    """Esta funcao retorna o numero de turnos em que trabalha o profissional
    'prof'. Caso 'prof' nao trabalhe em algum turno, entao a funcao retorna
    zero.
    Exemplos:
    >>> countTurns(['Ana', 'Bruno', 'Camila'], 'Ana')
    5
    >>> countTurns(['Ana', 'Bruno', 'Camila'], 'Camila')
    4
    >>> countTurns(['Ana', 'Bruno', 'Camila'], 'Douglas')
    0
    """
    return sum(1 for _, _, p, _ in buildTurns(profs) if p == prof)

def payTurns(profs, prof):
    """Esta funcao retorna o salario semanal de um profissional, assumindo que
    cada turno diurno lhe paga 1000 e cada turno noturno lhe paga 1333.
    Caso 'prof' nao trabalhe em algum turno, a funcao deve retornar zero.
    Exemplos:
    >>> payTurns(['Ana', 'Bruno', 'Camila'], 'Ana')
    5666
    >>> payTurns(['Ana', 'Bruno', 'Camila'], 'Camila')
    4666
    >>> payTurns(['Ana', 'Bruno', 'Camila'], 'Douglas')
    0
    """
    return sum(1000 if t == 'D' else 1333 for _, t, p, _ in buildTurns(profs) if p == prof)
