import re
from collections import Counter
import json

def main():

    with open("corpus/spanish/spanish.json", "r") as archivo:
        g_spanish = json.load(archivo)
    with open("corpus/english/english.json", "r") as archivo:
        g_english = json.load(archivo)

    g_spanish = Counter(g_spanish)
    g_english = Counter(g_english)

    text = input("Text: ")
    text = term_frequency(counter(n_grama(clean_text(text))))

    coincidences_span = similarities(text, g_spanish)
    coincidences_eng = similarities(text, g_english)
    total_coincidences = coincidences_span + coincidences_eng


    if total_coincidences == 0:
        print("Could not determine the language")
    elif coincidences_span > coincidences_eng:
        percentage_span = round(coincidences_span / total_coincidences * 100, 2)
        print(f"The text is in Spanish ({percentage_span}%)")
    elif coincidences_eng > coincidences_span:
        percentage_eng = round(coincidences_eng / total_coincidences * 100, 2)
        print(f"The text is in English ({percentage_eng}%)")
    else:
        percentage_span = round(coincidences_span / total_coincidences * 100, 2)
        percentage_eng = round(coincidences_eng / total_coincidences * 100, 2)
        print(f"Could not determine the language: English({percentage_eng}%) Spanish({percentage_span}%)")


def clean_text(t: str) -> str:
    cleaner = re.sub(r"""[\d.,!?¿¡'"():;\n\r]""", " ", t).lower()
    return cleaner

def n_grama(t: str) -> list:
    n_grama = []
    for i in range(len(t) - 3 + 1):
        n_grama.append(t[i:i+3])
    return n_grama

def counter(g: list) -> Counter:
    conteo = Counter(g)
    return conteo

def term_frequency(t: Counter) -> Counter:
    total = t.total()
    for n_gram in t:
        t[n_gram] = t[n_gram]/total
    return t

def similarities(text: Counter, language: Counter) -> float:
    similarity = 0
    for n_gram in text:
        if n_gram in language:
            similarity += min(text[n_gram], language[n_gram])
    return similarity



if __name__ == "__main__":
    main()
