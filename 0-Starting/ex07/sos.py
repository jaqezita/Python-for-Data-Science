from sys import argv
from typing import Dict


def codifica(code: str) -> str:
    """
    Converte uma string para código Morse.

    Entrada:
    - texto: string contendo apenas letras, dígitos e espaços.

    Saída:
    - string com os códigos Morse separados por espaço;
    """
    NESTED_MORSE: Dict[str, str] = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        " ": "/"
    }

    return " ".join(NESTED_MORSE[c] for c in code.upper())


def validation(argv: str) -> str:
    """
    Valida os argumentos da linha de comando e retorna o texto válido.

    Regras:
    - Deve haver exatamente um argumento do usuário.
    - O argumento deve conter apenas caracteres alfanuméricos ou espaços.

    Retorno:
    - string válida se tudo estiver OK.

    Exceções:
    - Levanta AssertionError quando a validação falha.
    """
    error_msg = "AssertionError: the arguments are bad"

    if len(argv) != 2:
        raise AssertionError(error_msg)

    text = argv[1]
    if not all(c.isalnum() or c == " " for c in text):
        raise AssertionError(error_msg)

    return text


def main():
    """
    Ponto de entrada:
    - valida argumentos
    - converte para Morse com codifica()
    - imprime resultado
    - em caso de erro, imprime a mensagem conforme especificação
    """
    try:
        code = validation(argv)
        print(codifica(code))
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
