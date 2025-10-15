def calculaSoma(l):
    soma = 0
    for el in l:
        if type(el) == list:
            soma = soma + calculaSoma(el)
        else:
            soma = soma + el
    return soma


lNumeros = [-12, [54, 0], 10, [8, 7], [5, 2]]
print(calculaSoma(lNumeros))