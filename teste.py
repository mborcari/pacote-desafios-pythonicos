from collections import Counter
with open("letras.txt") as f:
        contador = Counter([word.upper() for word in f.read() if word !=' ' and word != '\n'])
        print(contador, type(contador))
