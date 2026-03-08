def NULL_not_found(object: any) -> int:

    obj_type = type(object)

    if object is None:
        print(f'Nothing : None {obj_type}')
        return 0
    elif isinstance(object, float) and str(object) == "nan":
        print(f'Cheese:  NaN {obj_type}')
        return 0
    elif isinstance(object, int) and object == 0:
        print(f'Zero : 0 {obj_type}')
        return 0
    elif isinstance(object, str) and object == "":
        print(f'Empty : {obj_type}')
        return 0
    elif object is False:
        print(f'Fake : False {obj_type}')
        return 0
    else:
        print("Type not found")
        return 1
