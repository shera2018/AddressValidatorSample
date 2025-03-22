"""
Multilingual spellcheck functionality for NLTK using spylls.
"""

from typing import List
from spylls.hunspell import Dictionary
from nltk.tokenize import word_tokenize

def word_spellcheck(word: str, language: str) -> List[str]:
    """
    Perform word-level spellcheck for a given word in specified language.
    
    Args:
        word (str): The word to check
        language (str): Language code (e.g., 'en_US', 'de_DE')
        
    Returns:
        List[str]: List of spelling suggestions if word is incorrect, empty list if correct
    """
    try:
        # Initialize dictionary for the specified language
        dictionary = Dictionary.from_files(language)
        
        # Check if word is correct
        if dictionary.dic.check(word):
            return []
        
        # Get spelling suggestions
        return dictionary.dic.suggest(word)
    except Exception as e:
        raise ValueError(f"Error in spellcheck: {str(e)}")

def sentence_spellcheck(sentence: str, language: str) -> List[str]:
    """
    Perform sentence-level spellcheck for a given sentence in specified language.
    
    Args:
        sentence (str): The sentence to check
        language (str): Language code (e.g., 'en_US', 'de_DE')
        
    Returns:
        List[str]: List of incorrect words found in the sentence
    """
    # Tokenize the sentence
    words = word_tokenize(sentence)
    
    # Initialize dictionary for the specified language
    dictionary = Dictionary.from_files(language)
    
    # Check each word and collect incorrect ones
    incorrect_words = []
    for word in words:
        if not dictionary.dic.check(word):
            incorrect_words.append(word)
    
    return incorrect_words

def demo():
    """
    Demo function to test the spellcheck functionality.
    """
    # Test word-level spellcheck
    print("Testing word-level spellcheck:")
    word = "rainning"
    language = "en_US"
    suggestions = word_spellcheck(word, language)
    print(f"Word: {word}")
    print(f"Suggestions: {suggestions}")
    
    # Test sentence-level spellcheck
    print("\nTesting sentence-level spellcheck:")
    sentence = "There are fishe in the lke"
    incorrect_words = sentence_spellcheck(sentence, language)
    print(f"Sentence: {sentence}")
    print(f"Incorrect words: {incorrect_words}")

if __name__ == "__main__":
    demo() 