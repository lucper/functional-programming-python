Na primeira parte deste exercício, iremos resolver um problema clássico de programação: devemos implementar uma função "kanguru", que mapeia cada número N de uma lista em uma das seguintes saídas possíveis:

A string "kan", se N for divisível por 3.
A string "gu", se N for divisível por 5.
A string "ru", se N for divisível por 7.
A string "kangu", se divisível por 15.
A string "kanru", se divisível por 21.
A string "guru", se divisível por 35.
A string "kanguru", se divisível por 105.
A string que representa o próprio número, caso N não seja divisível nem por 3, nem por 5 e nem por 7.

Por exemplo, a chamada "kanguru([9, 10, 11, 21, 23, 105])" irá produzir a lista "['kan', 'gu', '11', 'kanru', '23', 'kanguru']".
Busque resolver esse exercício aos poucos.
O arquivo todo.py contém testes nos comentários.
Procure passar nos testes disponíveis nos comentários da função "kanguru".
Você pode executá-los com o comando "python3 -m doctest todo.py".

Na segunda parte, iremos implementar uma função "all\_subs(s, q)", que conta a quantidade de ocorrências da substring q dentro da string s.
Veja que sobreposições precisam ser contadas.
Por exemplo, a string "aaa" aparece 4 vezes dentro da string "aaaaaa".
