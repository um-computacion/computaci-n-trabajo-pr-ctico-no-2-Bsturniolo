def is_palindrome(value): 
# Normalizamos el texto
    word = value.lower()
    replacements = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'ü': 'u', 'ñ': 'n'
    }
    # Limpiamos el texto: solo letras y números, con reemplazo de acentos
    clean_text = ''.join(
        replacements.get(c, c) for c in word if c.isalnum()
    )
    # Verificamos si es un palíndromo
    return clean_text == clean_text[::-1]