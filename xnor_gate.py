def xnor_gate(x: bool, y: bool) -> bool:
    """
    Performs a logical XNOR operation on two boolean inputs.
    
    Args:
        x (bool): The first input.
        y (bool): The second input.
    
    Returns:
        bool: The result of the logical XNOR operation on the two inputs.
    """
    return (not (x or y)) and (x != y)