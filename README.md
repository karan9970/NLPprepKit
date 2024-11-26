text_preprocessor
"All-in-one text preprocessing toolkit for NLP enthusiasts"

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

##usage

from text_preprocessor import TextPreprocessor

preprocessor = TextPreprocessor()
cleaned_text = preprocessor.clean_text("This is an example text with <html> and numbers 123!")
print(cleaned_text)
