"""
11. remove_adjacent

Dada uma lista de números, retorne uma lista onde todos elementos
adjacentes iguais são reduzidos a um único elemento.

Exemplo: [1, 2, 2, 3]
Irá retornar: [1, 2, 3]
"""

def remove_adjacent(nums):
    """
    Neste solução, é criado uma tupla composta pelo função zip.
    É feito um slice na própria lista para começar a compração com o segundo elemento dela.
    Por fim, é comparado se o elemento atual é diferente do elemento anterior.
    Se for verdadeiro, adiciona o elemento em uma lista temporária.
    :param nums:
    :return:
    """
    temp_list = nums[:1]
    print(f'lista inicial: {nums}, {list(zip(nums, nums[1:]))}')
    for previus_value, value in zip(nums, nums[1:]):
        if previus_value != value:
            temp_list.append(value)
    return temp_list


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

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
    test(remove_adjacent, [1, 2, 2, 3], [1, 2, 3])
    test(remove_adjacent, [2, 2, 3, 3, 3], [2, 3])
    test(remove_adjacent, [], [])
    test(remove_adjacent, [2, 2, 3, 3, 3, 2, 2], [2, 3, 2])
    test(remove_adjacent, [2, 2, 4, 4, 4, 4, 3, 3, 3, 2, 2, 1, 1, 1], [2, 4, 3, 2, 1])
