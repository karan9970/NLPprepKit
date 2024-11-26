# Text Preprocessor

A Python library for cleaning and preprocessing text data for NLP tasks.

## Features
- Remove HTML, URLs, numbers, and punctuation
- Normalize text
- Remove stopwords
- Apply stemming or lemmatization
- Spellcheck with TextBlob

## Installation

```bash
pip install text-preprocessor



---

### How to Use the Package in a Project
1. Save the folder `text_preprocessor` in your project directory.
2. Import and use it as:
   ```python
   from text_preprocessor import TextPreprocessor
   
   preprocessor = TextPreprocessor()
   text = "Example: Can't we preprocess this text?"
   clean_text = preprocessor.preprocess(text, correct_spelling=True)
   print(clean_text)
