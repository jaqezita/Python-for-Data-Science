# Mostrar as propriedades fundamentais das estruturas de dados em Python
# list : mutável 
# tuple : imutável
# set : mutável, sem ordem, sem elementos duplicados
# dict : mutável, mapeamento chave-valor

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# Modificar ft_list
ft_list[1] = "World!"

# Modificar ft_tuple
ft_tuple = ("Hello", "Brasil!")

# Modificar ft_set
ft_set.discard("tutu!")     #discard remove o elemento se existir, se não existir não faz nada | remove remove o elemento e gera erro se não existir
ft_set.add("Sao Paulo!")

# Modificar ft_dict
ft_dict["Hello"] = "42SaoPaulo!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)