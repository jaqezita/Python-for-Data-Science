from sys import argv
from ft_filter import ft_filter


def main():
    """
    Função principal do programa.

    Recebe uma string e um número inteiro via argumentos
    do terminal e retorna as palavras cujo tamanho é
    maior que o número informado.
    """
    try:

        if len(argv) != 3:
            raise AssertionError("the arguments are bad")

        texto = argv[1]

        numero = int(argv[2])

        palavras = texto.split(" ")

        resultado = ft_filter(
            lambda palavra: len(palavra) > numero,
            palavras
        )

        print(resultado)

    except Exception:

        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()