def xor_gate(x: bool, y: bool) -> bool:
    """
    Performs a logical XOR operation on two boolean inputs.
    
    Args:
        x (bool): The first input.
        y (bool): The second input.
    
    Returns:
        bool: The result of the logical XOR operation on the two inputs.
    """
    return (x or y) and (x != y)