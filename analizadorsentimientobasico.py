palabras_positivas = {"bien": 1, "genial": 2, "fantástico": 3, "excelente": 3, "feliz": 2}
palabras_negativas = {"mal": 1, "terrible": 2, "horrible": 3, "malo": 1, "triste": 2}

def analizar_sentimiento(texto):
    texto = texto.lower()
    conteo_positivo = sum(palabras_positivas.get(palabra, 0) for palabra in texto.split())
    conteo_negativo = sum(palabras_negativas.get(palabra, 0) for palabra in texto.split())

    if conteo_positivo > conteo_negativo:
        return "Sentimiento positivo"
    elif conteo_negativo > conteo_positivo:
        return "Sentimiento negativo"
    else:
        return "Sentimiento neutral"

# Ejemplo de uso
texto = input("Escribe una oración para analizar: ")
resultado = analizar_sentimiento(texto)
print(f"El resultado del análisis es: {resultado}")