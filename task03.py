# Боєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа
import timeit

from boyer_moore_search import boyer_moore_search
from kmp_search import kmp_search
from rabin_karp_search import rabin_karp_search


search_functions = [
    boyer_moore_search,
    kmp_search,
    rabin_karp_search
]

articles = [
    "стаття 1.txt",
    "стаття 2.txt"
]


patterns = [
    "У данній статті було розглянуто",
    "Пошук стрибками",
    "Жадібні алгоритми",
    "Методи та структури даних для реалізації бази даних рекомендаційної системи соціальної мережі",
    "Параметри 1 серії експериментів: кількість агентів 65536, кількість предметів 131072",
    "Zero-suppressed BDDs and their applications. International Journal on Software Tools"
]


def measure_time(search_func, text, pattern):
    """
    Evaluate time of search function

    Returns:
        time in seconds
    
    Args:
        search_func: Search function
        text: text for searching
        pattern: some text for search
    """
    start_time = timeit.default_timer()
    search_result = search_func(text, pattern)
    end_time = (timeit.default_timer() - start_time) * 1000
    print(f"{search_func.__name__:<24} {search_result:<10} {end_time}") 


def text_from_file(file):
    """
    Get text from openned file

    Returns:
        text from file
    
    Args:
        file: link to file
    """
    with open(file, 'r', encoding="utf-8") as f:
        content = f.read()
        return content


def function_comparison(search_functions, articles, patterns):
    """
    Execute evaluation of search functions
    
    Args:
        search_functions: list of search functions for evaluation
        articles: list of texts for search
        patterns: list of patterns for search in text
    """
    experiment = 0
    for article in articles:
        text = text_from_file(article)
        for pattern in patterns:
            experiment += 1
            print(f"Start experiment #{experiment}: Article: {article}, Pattern: {pattern}")
            print(f"  FUNCTION         SEARCH RESULT      DURATIONS MILISECONDS")
            for search_func in search_functions:
                measure_time(search_func, text, pattern)
            print()


def main():
    print("-"*46)
    print(f"{"*"*4} Start bunch of searching experiments {"*"*4}")
    print("-"*46)
    function_comparison(search_functions, articles, patterns)
    print(f"{"*"*4} End bunch of searching experiments {"*"*4}")
    print("-"*40)   


if __name__ == "__main__":
    main()

