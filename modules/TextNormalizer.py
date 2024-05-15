import re

from unidecode import unidecode


class TextNormalizer:
    """Class to normalize text for matching with audio files."""

    @staticmethod
    def normalize(text):
        """Normalize text by removing diacritics, punctuation, and converting to lowercase."""
        text = unidecode(text)
        text = re.sub(r'[^\w\s]', '', text)
        text = text.lower()
        text = text.replace(' ', '_')
        return text