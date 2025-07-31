from mcp.server.fastmcp import FastMCP


mcp=FastMCP(name="Weather")

@mcp.tool()
async def get_weather(location:str)->str:
    """
    Get the weather for a given location.

    Args:
        location (str): The location to get the weather for.

    Returns:
        str: The weather for the given location.
    """
    return f"Its always raining in {location}!"


if __name__ == "__main__":
    mcp.run(transport="streamable-http") #streamable-http is a transport that allows the server to be accessed via a web socket. Its works like a API endpoint, you can send a request to it and get a response. And the link to the API is http://localhost:8000/mcp/weather







