from sys import argv
from string import punctuation


def contar_caracteres(texto):
    """
    Conta os diferentes tipos de caracteres de uma string.

    Argv:
        texto (str): texto de entrada

    Returns:
        dict: quantidade de cada categoria de import sys
import stringcaractereWhat is the text to count
    """
    contagem = {
        "maiusculas": 0,
        "minusculas": 0,
        "pontuacao": 0,
        "espacos": 0,
        "digitos": 0,
    }

    for caractere in texto:
        if caractere.isupper():
            contagem["maiusculas"] += 1
        elif caractere.islower():
            contagem["minusculas"] += 1
        elif caractere in punctuation:
            contagem["pontuacao"] += 1
        elif caractere.isdigit():
            contagem["digitos"] += 1
        elif caractere.isspace():
            contagem["espacos"] += 1

    return contagem


def mostrar_resultado(texto, contagem):
    """
    Exibe o resultado formatado da contagem.

    Args:
        texto (str): texto original
        contagem (dict): resultado das contagens
    """
    print(f"The text contains {len(texto)} characters:")
    print(f"{contagem['maiusculas']} upper letters")
    print(f"{contagem['minusculas']} lower letters")
    print(f"{contagem['pontuacao']} punctuation marks")
    print(f"{contagem['espacos']} spaces")
    print(f"{contagem['digitos']} digits")


def main():
    """
    Função principal do programa.
    Responsável por tratar argumentos e erros.
    """
    try:
        if len(argv) > 2:
            raise AssertionError("more than one argument provided")

        if len(argv) == 1:
            texto = input("Enter a string?\n")
        else:
            texto = argv[1]

        contagem = contar_caracteres(texto)
        mostrar_resultado(texto, contagem)

    except Exception as erro:
        print(f"AssertionError: {erro}")


if __name__ == "__main__":
    main()
