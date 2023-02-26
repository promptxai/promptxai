import re

def search_friendly_filename(filename: str) -> str:
    """Strip a filename of any characters which are not alphabets while preserving whitespace. 
    Then replace whitespace with hyphen. Convert to lowercase.

    Args:
        filename: File name to strip.
    Returns:
        filename_stripped: Stipped file name. Maybe same as input.
    """
    search_friendly_filename = re.sub(r'[^a-zA-Z\s]', '', filename).replace(' ', '-').lower()
    return search_friendly_filename

def words_to_tokens(words: int) -> int:
    """Convert words to tokens."""
    return int(words * 4/3 + 1)

def chars_to_tokens(chars: int) -> int:
    """Convert characters to tokens."""
    return int(chars / 4 + 1)
