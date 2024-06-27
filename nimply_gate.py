def nimply_gate(x: bool, y: bool) -> bool:
    """
    Performs a logical NIMPLY operation on two boolean inputs.
    
    Args:
        x (bool): The first input.
        y (bool): The second input.
    
    Returns:
        bool: The result of the logical NIMPLY operation on the two inputs.
    """
    return not ((not x) or y)