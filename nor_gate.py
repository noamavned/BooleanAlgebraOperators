def nor_gate(x: bool, y: bool) -> bool:
    """
    Performs a logical NOR operation on two boolean inputs.
    
    Args:
        x (bool): The first input.
        y (bool): The second input.
    
    Returns:
        bool: The result of the logical NOR operation on the two inputs.
    """
    return not (x or y)


def nor_gate3(x: bool, y: bool, z: bool) -> bool:
    """
    Performs a logical NOR operation on three boolean inputs.
    
    Args:
        x (bool): The first input.
        y (bool): The second input.
        z (bool): The third input.
    
    Returns:
        bool: The result of the logical NOR operation on the four inputs.
    """
    return not (x or y or z)

def nor_gate4(x: bool, y: bool, z: bool, r: bool) -> bool:
    """
    Performs a logical NOR operation on four boolean inputs.
    
    Args:
        x (bool): The first input.
        y (bool): The second input.
        z (bool): The third input.
        r (bool): The fourth input.
    
    Returns:
        bool: The result of the logical NOR operation on the four inputs.
    """
    return not (x or y or z or r)