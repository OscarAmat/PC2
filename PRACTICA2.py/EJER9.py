def sin_vocales(palabra):
    vocales = []
    for letra in palabra:
        if letra not in "aeiouAEIOU":
            vocales.append(letra)
    return ''.join(vocales) 

print(sin_vocales('mi corazon late como agua de cacaguate'))