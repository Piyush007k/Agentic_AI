from mcp.server.fastmcp import FastMCP


mcp=FastMCP(name="Math")

@mcp.tool()
async def add(a:int,b:int)->int:
    """
Adding two integers and return the result.

Args:
    a (int): The first integer.
    b (int): The second integer.

Returns:
    int: The addition of `a` and `b`.
"""
    if isinstance(a,str):
        a=int(a)

    if isinstance(b,str):
        b=int(b)

    c = a + b
    
    return c


@mcp.tool()
async def multiply(a:int,b:int)->int:
    """
Multiply two integers and return the result.

Args:
    a (int): The first integer.
    b (int): The second integer.

Returns:
    int: The product of `a` and `b`.
"""
    if isinstance(a,str):
        a=int(a)

    if isinstance(b,str):
        b=int(b)

    c = a * b
    
    return c

@mcp.tool()
async def subtract(a:int,b:int)->int:
    """
Subtracts two integers and return the result.

Args:
    a (int): The first integer .
    b (int): The second integer .

Returns:
    int: The substraction of `a` and `b`.
"""
    if isinstance(a,str):
        a=int(a)

    if isinstance(b,str):
        b=int(b)

    c = a - b
    
    return c


@mcp.tool()
async def multiply(a:int,b:int)->int:
    """
Multiply two integers and return the result.

Args:
    a (int): The first integer .
    b (int): The second integer .

Returns:
    int: The product of `a` and `b`.
"""
    if isinstance(a,str):
        a=int(a)

    if isinstance(b,str):
        b=int(b)

    c = a * b
    
    return c

@mcp.tool()
async def divide(a:int,b:int)->int:
    """
Divides two integers and return the result.

Args:
    a (int): The first integer .
    b (int): The second integer .

Returns:
    int: The division of `a` and `b`.
"""
    if isinstance(a,str):
        a=int(a)

    if isinstance(b,str):
        b=int(b)

    c = a / b
    
    return c

# The transport="stdio" argument tells the server to:

# Use standard input/output (stdin and stdout) to receive and respond to tool function calls

# The server will run in the current terminal and can be interacted with using standard input/output.


if __name__ == "__main__":
    mcp.run(transport="stdio")