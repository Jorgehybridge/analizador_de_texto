import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from analyzer.text_analyzer import (
	count_words,
	count_characters,
	count_sentences,
	longest_word,longest_sentence,longest_paragraph
)


text = "Cuando la vida diaria, cuando el amor se acaba, blablalblbalbblalbalba"
 #Esta es una prueba
print("Palabras:", count_words(text))
print(f"Caracteres:", count_characters(text))
print(f"Oraciones:", count_sentences(text))
print(f"Palabra mas larga:", longest_word(text))
print(f"Oracion mas larga:", longest_sentence(text))
print(f"Parrafo mas largo:", longest_paragraph(text))
