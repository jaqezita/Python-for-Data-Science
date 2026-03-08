def ft_filter(function, iterable):
    """
    Reimplementação da função filter do Python.

    Retorna os elementos do iterável para os quais
    a função retorna True.

    Args:
        function (callable | None): função de filtro
        iterable (iterable): sequência de elementos

    Returns:
        list: elementos filtrados
    """

    if function is None:
        return [item for item in iterable if item]

    return [item for item in iterable if function(item)]