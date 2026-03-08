def all_thing_is_obj(object: any) -> int:

    obj_type = type(object)
    type_name = obj_type.__name__

    if type_name == "str":
        print(f'{object} is in the kitchen : {obj_type}')
    elif type_name not in ["list", "tuple", "set", "dict"]:
        print("Type not found")
    else:
        print(f'{type_name.capitalize()} : {obj_type}')
    return 42
