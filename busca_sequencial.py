def buscaSeq(l, chave):
    for(i, el) in enumerate(l):
        if el[0] == chave:
            return i
    return None

# Testes
lAlunos = [['Mickey', 8.7], ['Pateta', 6.5], ['Minnie', 10.0], ['Margarida', 7.7]]

print(buscaSeq(lAlunos, 'Minnie'))
print(buscaSeq(lAlunos, 'Pato Donald'))