"""
14. mimic

Neste desafio você vai fazer um gerador de lero-lero.

É um programa que lê um arquivo, armazena a relação entre as palavras e
então gera um novo texto respeitando essas relações para imitar um
escritor de verdade.

Para isso você precisa:

A. Abrir o arquivo especificado via linha de comando.

B. Ler o conteúdo e separar as palavras obtendo uma lista de palavras.

C. Criar um dicionário de "imitação".

Nesse dicionário a chave será uma palavra e o valor será uma lista
contendo as palavras que aparecem no texto após a palavra usada na chave.

Por exemplo, suponha um arquivo com o conteúdo: A B C B A

O dicionário de imitação deve considerar que:
* a chave A contém uma lista com a palavra B
* a chave B contém uma lista com as palavras C e A
* a chave C contém uma lista com a palavra B

Além disso precisamos considerar que:
* a chave '' contém uma lista com a primeira palavra do arquivo
* a última palavra do arquivo contém uma lista com a palavra ''.

Com o dicionario imitador é bastante simples emitir aleatoriamente texto
que imita o original. Imprima uma palavra, depois veja quais palavras podem
vir a seguir e pegue uma aleatoriamente como a proxima palavra do texto.

Use a string vazia como a primeira palavra do texto para preparar as coisas.

Nota: o módulo padrão do python 'random' conta com o random.choice(list),
método que escolhe um elemento aleatório de uma lista não vazia.
"""

import random
import sys
from collections import defaultdict

def clear_words(word):
    return word.lower().replace("\n", "").replace("''", "").replace(".", "")

def file_to_list(filename):
    with open(filename) as f:
        lista_words = f.read().lower().split(" ")
        # aplica padrão nos textos, limpado quebra de linha e colocando em minusculo
        lista_words = list(map(lambda word: clear_words(word), lista_words))
    return lista_words

def mimic_dict(filename):
    d = defaultdict(list)
    mimic_list = file_to_list(filename)
    first_word, last_word = mimic_list[0], mimic_list[-1]
    mimic_list = mimic_list[1:-2]
    mimic_tuple = list(zip(mimic_list, mimic_list[1:]))
    for k, v in mimic_tuple:
        if v not in d[k]:
            d[k].append(v)
    d[""], d[last_word] = first_word, ""
    return d

def print_mimic(mimic_dict, word):
    """Dado o dicionario imitador e a palavra inicial, imprime texto de 200 palavras."""
    # +++ SUA SOLUÇÃO +++
    texto = word.capitalize()
    count_text = 0
    capitalize_next_word = False
    word_init = word
    for count in range(200):
        lista_word = mimic_dict[word]
        #trata listas vazias
        if lista_word != [''] and lista_word:
            word = random.choice(lista_word)
        else:
            word = word_init
        # Capitaliza primeira palavra após ponto final.
        texto += f' {word.capitalize()}' if capitalize_next_word else f' {word}'
        # a cada 20 paalvras, coloca um ponto final
        if count % 20 == 0:
            texto += "."
            capitalize_next_word = True
        else:
            capitalize_next_word = False
    print(texto)


# Chama mimic_dict() e print_mimic()
def main():
    for a in sys.argv:
       print(a)
    if len(sys.argv) != 2:
        print('Utilização: ./14_mimic.py file-to-read')
        sys.exit(1)

    dict = mimic_dict(sys.argv[1])
    print_mimic(dict, 'we')


if __name__ == '__main__':
  main()
