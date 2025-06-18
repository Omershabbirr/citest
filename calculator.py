def add(a: float, b: float) -> float:
    """
    Add two numbers and return the result.
    
    Args:
        a (float): First number
        b (float): Second number
        
    Returns:
        float: Sum of a and b
    """
    return a + b

def subtract(a: float, b: float) -> float:
    """
    Subtract b from a and return the result.
    
    Args:
        a (float): First number
        b (float): Second number
        
    Returns:
        float: Difference of a and b
    """
    return a - b

def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers and return the result.
    
    Args:
        a (float): First number
        b (float): Second number
        
    Returns:
        float: Product of a and b
    """
    return a * b

def divide(a: float, b: float) -> float:
    """
    Divide a by b and return the result.
    
    Args:
        a (float): First number
        b (float): Second number
        
    Returns:
        float: Quotient of a and b
        
    Raises:
        ZeroDivisionError: If b is zero
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b 