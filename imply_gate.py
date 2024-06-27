def imply_gate(x: bool, y: bool) -> bool:
    """
    Performs a logical IMPLY operation on two boolean inputs.
    
    Args:
        x (bool): The first input.
        y (bool): The second input.
    
    Returns:
        bool: The result of the logical IMPLY operation on the two inputs.
    """
    return (not x) or y