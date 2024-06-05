import re
import re

def find_names(string):
    # Padronize a string para facilitar a busca
    padrao = re.compile(r'[A-ZÁ-Ú][a-zá-ú]+ ou [A-ZÁ-Ú][a-zá-ú]+')

    matches = padrao.findall(string)

    nomes = [match.split(" ou ") for match in matches]

    try:
        return nomes[0]
    except IndexError:
        return []

def extrair_palavras_por_classe(texto, classe1, classe2):
    padrao = re.compile(r'([^\n-]+(?:-[^\n-]+)*) - ([^\n]+)')

    lista_classe1 = []
    lista_classe2 = []

    # Encontrar todos os pares correspondentes
    correspondencias = padrao.findall(texto)

    for frase, classe in correspondencias:
        frase = frase.strip()
        classe = classe.strip()
        if classe == classe1:
            lista_classe1.append(frase)
        elif classe == classe2:
            lista_classe2.append(frase)

    return lista_classe1, lista_classe2