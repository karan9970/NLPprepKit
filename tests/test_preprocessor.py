import unittest
from text_preprocessor.preprocessor import TextPreprocessor

class TestTextPreprocessor(unittest.TestCase):
    def test_clean_text(self):
        preprocessor = TextPreprocessor(remove_stopwords=False)
        text = "This is an example! Visit https://example.com"
        cleaned = preprocessor.clean_text(text)
        self.assertEqual(cleaned, "this is an example visit")
