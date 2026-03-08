ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# Modificar ft_list
ft_list[1] = "World!"

# Modificar ft_tuple
ft_tuple = ("Hello", "Brasil!")

# Modificar ft_set
ft_set.discard("tutu!")
ft_set.add("Sao Paulo!")

# Modificar ft_dict
ft_dict["Hello"] = "42SaoPaulo!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
