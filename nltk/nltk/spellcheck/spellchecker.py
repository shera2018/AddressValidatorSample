"""
Multilingual spellcheck implementation using spylls.
"""

from typing import List, Tuple, Dict
from nltk.tokenize import word_tokenize
from spylls.hunspell import Dictionary

def word_spellcheck(word: str, language: str) -> List[Tuple[str, str]]:
    """
    Check if a word is spelled correctly and return suggestions with their types if incorrect.
    
    Args:
        word (str): The word to check
        language (str): Language code (e.g., 'en_US', 'de_DE')
        
    Returns:
        List[Tuple[str, str]]: List of tuples containing (suggestion, type) if word is incorrect,
                             empty list if correct. Types can be:
                             - 'badchar': Bad character
                             - 'twowords': Split into two words
                             - 'phonet': Phonetic suggestion
                             - 'other': Other type of suggestion
    """
    try:
        # Initialize dictionary for the specified language
        dictionary = Dictionary(language)
        
        # Check if word is correct
        if dictionary.lookup(word):
            return []
            
        # Get suggestions with their types for incorrect word
        return list(dictionary.suggest(word))
    except Exception as e:
        raise ValueError(f"Error in spellcheck: {str(e)}")

def sentence_spellcheck(sentence: str, language: str) -> Dict[str, List[Tuple[str, str]]]:
    """
    Check a sentence for spelling errors and return dictionary of incorrect words with their suggestions.
    
    Args:
        sentence (str): The sentence to check
        language (str): Language code (e.g., 'en_US', 'de_DE')
        
    Returns:
        Dict[str, List[Tuple[str, str]]]: Dictionary mapping incorrect words to their suggestions with types
    """
    # Tokenize the sentence
    words = word_tokenize(sentence)
    
    # Initialize dictionary for the specified language
    dictionary = Dictionary(language)
    
    # Check each word and collect incorrect ones with their suggestions
    incorrect_words = {}
    for word in words:
        if not dictionary.lookup(word):
            incorrect_words[word] = list(dictionary.suggest(word))
            
    return incorrect_words

def demo():
    """
    Demo function to test the spellcheck APIs.
    """
    # Test word-level spellcheck
    print("Testing word-level spellcheck:")
    word = "rainning"
    suggestions = word_spellcheck(word, "en_US")
    print(f"Word: {word}")
    print("Suggestions with types:")
    for suggestion, type_ in suggestions:
        print(f"  - {suggestion} ({type_})")
    
    # Test sentence-level spellcheck
    print("\nTesting sentence-level spellcheck:")
    sentence = "There are fishe in the lke"
    incorrect_words = sentence_spellcheck(sentence, "en_US")
    print(f"Sentence: {sentence}")
    print("Incorrect words with suggestions:")
    for word, suggestions in incorrect_words.items():
        print(f"\nWord: {word}")
        for suggestion, type_ in suggestions:
            print(f"  - {suggestion} ({type_})")

if __name__ == "__main__":
    demo() 