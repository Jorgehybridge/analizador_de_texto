import sys
import os

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from analyzer.text_analyzer import (
	count_words,
	count_characters,
	count_sentences,
	longest_word
)

def test_count_words():
	text = "Hola mundo"
	result = count_words(text)
	assert result == 2, f"Expected 2, got {result}"
	print("✓ test_count_words pasó")

def test_count_characters():
	text = "Hola"
	result = count_characters(text)
	assert result == 4, f"Expected 4, got {result}"
	print("✓ test_count_characters pasó")

def test_count_sentences():
	text = "Hola mundo. Esto es una prueba."
	result = count_sentences(text)
	assert result == 2, f"Expected 2, got {result}"
	print("✓ test_count_sentences pasó")

def test_longest_word():
	text = "Hola mundo de programacion"
	result = longest_word(text)
	assert result == "programacion", f"Expected 'programacion', got '{result}'"
	print("✓ test_longest_word pasó")

if __name__ == "__main__":
	try:
		test_count_words()
		test_count_characters()
		test_count_sentences()
		test_longest_word()
		print("\n✅ Todos los tests pasaron correctamente!")
	except AssertionError as e:
		print(f"\n❌ Error en test: {e}")
		sys.exit(1)
