"""
Tests for the spellcheck module.
"""

import unittest
from nltk.spellcheck import word_spellcheck, sentence_spellcheck

class TestSpellcheck(unittest.TestCase):
    def test_word_spellcheck(self):
        # Test correct word
        self.assertEqual(word_spellcheck("rain", "en_US"), [])
        
        # Test incorrect word
        suggestions = word_spellcheck("rainning", "en_US")
        self.assertIsInstance(suggestions, list)
        self.assertIn("raining", suggestions)
        
        # Test invalid language
        with self.assertRaises(ValueError):
            word_spellcheck("test", "invalid_lang")
    
    def test_sentence_spellcheck(self):
        # Test correct sentence
        self.assertEqual(sentence_spellcheck("The rain is falling.", "en_US"), [])
        
        # Test sentence with incorrect words
        incorrect_words = sentence_spellcheck("There are fishe in the lke", "en_US")
        self.assertIsInstance(incorrect_words, list)
        self.assertIn("fishe", incorrect_words)
        self.assertIn("lke", incorrect_words)
        
        # Test invalid language
        with self.assertRaises(ValueError):
            sentence_spellcheck("Test sentence", "invalid_lang")

if __name__ == "__main__":
    unittest.main() 