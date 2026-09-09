# Language Detector using N-Gram Analysis
#### Video Demo: (https://youtu.be/mhkuGnYiPdo)
#### Description:

This project is a Python-based language detection tool designed to identify whether a given text is written in Spanish or English. The program analyzes character sequence patterns (3-grams or trigrams) from the user's input and compares their relative frequencies against pre-calculated reference frequency files for both languages.

---

### How It Works

1. **Corpus Loading**: Upon execution, the program loads reference data from `spanish.json` and `english.json` in the `corpus/` directory. These JSON files store the most frequent trigrams extracted from a reference text corpus for each language.
2. **Text Cleaning & Preprocessing**: The raw text entered by the user is cleaned using regular expressions via `clean_text()`. This process removes punctuation marks, numbers, line breaks, and converts all characters to lowercase to maintain consistency.
3. **N-Gram Generation**: The program generates overlapping character trigrams (sequences of 3 consecutive letters) from the cleaned string using `n_grama()`.
4. **Frequency Calculation**: Using Python's `.Counter`, the code counts each trigram's occurrence and normalizes the results into relative term frequencies (TF) by dividing each count by the total number of extracted trigrams.
5. **Similarity Scoring**: The top 10 most frequent trigrams from the user's input are compared against the top 30 most frequent reference trigrams for Spanish and English using set intersection (`&`).
6. **Classification & Output**: The program calculates match percentages for both languages and outputs the prediction. If no clear match or a tie is detected, it handles the result gracefully with an informative message.

---

### Project Structure & Files

- **`project.py`**: The core application file containing the main execution flow (`main()`) and all helper functions responsible for text preprocessing, trigram extraction, frequency sorting, and similarity calculations.
- **`test_project.py`**: Automated unit testing file executed with `pytest` to ensure that custom functions (such as `clean_text`, `n_grama`, and `counter`) behave as expected.
- **`build_corpus.py`**: A helper script used prior to runtime to process raw text corpora in Spanish and English, extract their character trigram distributions, and save the results into JSON files.
- **`corpus/`**: Folder storing `spanish.json` and `english.json`, which hold the compiled trigram frequency datasets for each target language.
- **`requirements.txt`**: List of external dependencies required for the project (empty, as the program exclusively relies on Python's Standard Library).

---

### Core Functions in `project.py`

- **`clean_text(t: str) -> str`**: Strips away numbers, punctuation marks, symbols, and whitespace characters using regular expressions, returning a lowercase string.
- **`n_grama(t: str) -> list`**: Slices the cleaned text into a list of 3-character sequences (trigrams).
- **`counter(g: list) -> Counter`**: Converts a list of extracted trigrams into a `collections.Counter` frequency mapping.
- **`term_frequency(t: Counter) -> Counter`**: Normalizes raw trigram counts into relative frequencies by dividing each count by the total trigram volume.
- **`sorted_numbers(t: Counter) -> list`**: Sorts trigram counts or relative frequencies in descending order.
- **`corpus/`**: Main directory containing language datasets divided into subfolders:
  - **`corpus/english/`**: Contains raw text source files (`1984.txt`, `frankenstein.txt`, `wikipedia_en.txt`, etc.) used as a reference to generate `english.json`.
  - **`corpus/spanish/`**: Contains raw text source files (`don_quijote.txt`, `regenta.txt`, `periodico1.txt`, `wikipedia.txt`, etc.) used as a reference to generate `spanish.json`.
- **`requirements.txt`**: List of external dependencies required for the project (empty, as the program exclusively relies on Python's Standard Library).

---

### Design Choices

- **Selection of Trigrams (3-Grams)**: Using 3-letter groups is a simple and fast way to get good results without slowing down the code. Unigrams (1-grams) or bigrams (2-grams) lack linguistic distinction, whereas 4-grams or 5-grams require significantly larger datasets to generalize well.
- **Set Intersection for Similarity**: Using set intersection (&) is a quick and easy way to see which top letter combinations overlap, without needing complicated math or heavy tools.
- **Standard Library Reliance**: By using only native Python modules (`re`, `collections`, `json`), the project remains extremely lightweight, fast to execute, and completely free of third-party dependencies.
