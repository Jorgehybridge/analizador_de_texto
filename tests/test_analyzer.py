import sys
import os

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from analyzer.text_analyzer import (
	count_words,
	count_characters,
	count_sentences,
	longest_word
)


def test_count_words():
	text = "Hola mundo"
	assert count_words(text) == 2


def test_count_characters():
	text = "Hola"
	assert count_characters(text) == 4


def test_count_sentences():
	text = "Hola mundo. Esto es una prueba."
	assert count_sentences(text) == 2


def test_longest_word():
	text = "Hola mundo de programacion"
	assert longest_word(text) == "programacion"
