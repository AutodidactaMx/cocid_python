one_dict = {"Direccion": "3212 Morelos", "Año": 2021}
two_dict = {"Nombre": "Jesus", "Age": 33}


def merge_two_dictionaries(a, b):
    return {**a, **b}


print(merge_two_dictionaries(one_dict, two_dict))