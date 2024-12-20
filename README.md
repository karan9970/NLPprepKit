# Text Preprocessor
# Text Preprocessor

A Python package for preprocessing textual data for machine learning and natural language processing tasks. It includes functionality for:

- Converting text to lowercase
- Removing punctuation, numbers, and special characters
- Handling negations
- Removing stopwords
- Stemming and lemmatization
- Correcting spelling (optional)

## Installation
1. Clone or download the package.
2. Add the folder to your project or install via pip (if published).

## Usage
```python
from text_preprocessor import TextPreprocessor

preprocessor = TextPreprocessor()
text = "This is an example! Isn't it great?"
clean_text = preprocessor.preprocess(text, correct_spelling=True)
print(clean_text)

