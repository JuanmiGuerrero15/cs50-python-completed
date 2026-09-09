import re
from collections import Counter
import json

def main():

    with open("project/corpus/spanish/periodico1.txt", "r", encoding="utf-8") as f1:
        file1 = f1.read()
    with open("project/corpus/spanish/periodico2.txt", "r", encoding="utf-8") as f2:
        file2 = f2.read()
    with open("project/corpus/spanish/don_quijote.txt", "r", encoding="utf-8") as f3:
        file3 = f3.read()
    with open("project/corpus/spanish/regenta.txt", "r", encoding="utf-8") as f4:
        file4 = f4.read()
    with open("project/corpus/spanish/wikipedia.txt", "r", encoding="utf-8") as f5:
        file5 = f5.read()

    file1 = n_grama(clean_text(file1))
    file2 = n_grama(clean_text(file2))
    file3 = n_grama(clean_text(file3))
    file4 = n_grama(clean_text(file4))
    file5 = n_grama(clean_text(file5))


    total = file1 + file2 + file3 + file4 + file5
    total = term_frequency(counter(total))

    with open("spanish.json", "w", encoding="utf-8") as archivo:
        json.dump(dict(total), archivo, ensure_ascii=False, indent=4)


def clean_text(t: str) -> str:
    cleaner = re.sub(r"""[\d.,!?¿¡'"():;\n\r]""", " ", t).lower()
    return cleaner

def n_grama(t: str, n: int = 3) -> list:
    gramas = []
    for i in range(len(t) - n + 1):
        gramas.append(t[i:i+n])
    return gramas

def counter(g: list) -> Counter:
    conteo = Counter(g)
    return conteo

def term_frequency(t: Counter) -> Counter:
    total = t.total()
    for n_gram in t:
        t[n_gram] = t[n_gram]/total
    return t

if __name__ == "__main__":
    main()
