"""
10. sort_last

Dada uma lista de tuplas não vazias, retorne uma lista ordenada em ordem
crescente com base no último elemento de cada tupla.

Exemplo: [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
Irá retornar: [(2, 2), (1, 3), (3, 4, 5), (1, 7)]

Dica: Use uma custom key= function para extrair o ultimo elemento de cada tupla.
"""



def sort_last(tuples):

    # Usando função própria com sort selection
    return selection_sort(tuples, key=1)

    # Usando itemgetter
    #from operator import itemgetter, attrgetter
    # return sorted(tuples, key=itemgetter(1))

    # Usando sorted com o atritbute key
    # return sorted(tuples, key=lambda tuple_: tuple_[-1])


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---
def selection_sort(tuples, key=None):
    temp_list = list(tuples)
    key = 0 if key is None else key
    for index, item in enumerate(temp_list):
        minor_item, minor_item_index = item, index
        flag_swap = False
        for index_, item_ in enumerate(temp_list[index:]):
            if item_[key] < minor_item[key]:
                # soma index_ com index para compensar o slice da lista
                minor_item, minor_item_index = item_,  index_ + index
                # Define flag que sinaliza a necesidade de swap
                flag_swap = True
        #swap itens
        if flag_swap:
            temp_item = temp_list[index]
            temp_list[index], temp_list[minor_item_index] = minor_item, temp_item
    return temp_list


def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(sort_last, [(1, 3), (3, 2), (2, 1)],
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last, [(2, 3), (1, 2), (3, 1)],
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last, [(1, 7), (1, 3), (3, 4, 5), (2, 2)],
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])
