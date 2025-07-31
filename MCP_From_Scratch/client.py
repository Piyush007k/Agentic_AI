from langchain_mcp_adapters.client import MultiServerMCPClient
# from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent


from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    client = MultiServerMCPClient(
        {
            "Math":{
                "command":"python",
                "args":["mathServer.py"],
                "transport":"stdio",
            },
            "Weather":{
                "url":"http://127.0.0.1:8000/mcp",
                "transport":'streamable_http',
            }
        }
    )

    import os 
    os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")

    tools= await client.get_tools()
    model = ChatGroq(model="qwen/qwen3-32b")
    agent=create_react_agent(
        model,tools
    )

    math_response=await agent.ainvoke(
        {"messages":[{'role':'user', 'content':"Give the step by step solution for (3 + 5) x 12?"}]}
    )

    weather_response=await agent.ainvoke(
        {"messages":[{'role':'user', 'content':"What's the weather in Tokyo?"}]}
    )

    print("Maths response : ",math_response['messages'][-1].content)
    print("Weather response : ",weather_response['messages'][-1].content)


asyncio.run(main())





