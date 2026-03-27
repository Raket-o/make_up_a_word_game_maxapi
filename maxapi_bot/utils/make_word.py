"""Модуль для поиска слов, составленных из заданных букв."""

import pathlib
from typing import Dict, List


class FindWords:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.dict_words: List[str] = []
        self.update_dict_words()

    def update_dict_words(self) -> None:
        """
        Загружает список слов из файла и сохраняет в нижнем регистре.
        Поддерживает кириллицу, включая 'ё'.
        """
        file_path = pathlib.Path(__file__).parent / self.file_name
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                self.dict_words = file.read().lower().split()
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл не найден: {file_path}")
        except Exception as e:
            raise RuntimeError(f"Ошибка при чтении файла {file_path}: {e}")

    async def _normalize_word(self, word: str) -> str:
        """Заменяет 'ё' на 'е' для корректного сравнения."""
        user_word_split = list(word)
        for ind, sym in enumerate(word):
            if ord(sym) == 235:
                user_word_split[ind] = "ё"
        return "".join(user_word_split)

    async def get_find_words(self, user_word: str) -> Dict[int, List[str]]:
        """
        Находит все слова из словаря, которые можно составить из букв user_word.
        Учитывает количество букв (нельзя использовать букву чаще, чем она встречается).

        Args:
            user_word (str): Строка с буквами, из которых составляются слова.

        Returns:
            Dict[int, List[str]]: Словарь вида {длина_слова: [слова]}, отсортированные по длине и алфавиту.
        """
        user_word = await self._normalize_word(user_word.lower())
        user_letter_count = {char: user_word.count(char) for char in set(user_word)}

        result_words = []

        for word in self.dict_words:
            normalized_word = await self._normalize_word(word)

            # Проверяем, что все буквы слова есть в user_wordи в достаточном количестве
            if len(normalized_word) > len(user_word):
                continue  # Оптимизация: слово длиннее исходного — пропускаем

            valid = True
            for char in set(normalized_word):
                if normalized_word.count(char) > user_letter_count.get(char, 0):
                    valid = False
                    break

            if valid:
                result_words.append(word)

        # Сортируем: сначала по длине, потом по алфавиту
        result_words.sort(key=lambda x: (len(x), x))

        # Группируем по длине
        dict_len_and_word: Dict[int, List[str]] = {}
        for word in result_words:
            dict_len_and_word.setdefault(len(word), []).append(word)

        return dict_len_and_word


# Инициализация объекта
find_words_obj = FindWords("russian_nouns.txt")
