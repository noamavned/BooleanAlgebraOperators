def nand_gate(x: bool, y: bool) -> bool:
    """
        Performs a logical NAND operation on two boolean inputs.
    
        Args:
            x (bool): The first input.
            y (bool): The second input.
    
        Returns:
            bool: The result of the logical NAND operation on the two inputs.
    """
    return not (x and y)


def nand_gate3(x: bool, y: bool, z: bool) -> bool:
    """
        Performs a logical NAND operation on three boolean inputs.
        
        Args:
            x (bool): The first input.
            y (bool): The second input.
            z (bool): The third input.
        
        Returns:
            bool: The result of the logical NAND operation on the three inputs.
    """
    return not (x and y and z)


def nand_gate4(x: bool, y: bool, z: bool, r: bool) -> bool:
    """
    Performs a logical NAND operation on four boolean inputs.
    
    Args:
        x (bool): The first input.
        y (bool): The second input.
        z (bool): The third input.
        r (bool): The fourth input.
    
    Returns:
        bool: The result of the logical NAND operation on the four inputs.
    """
    return not (x and y and z and r)
