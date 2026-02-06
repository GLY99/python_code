import asyncio
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient


mcp_server_config = {
    "url": "http://127.0.0.1:8080/sse",
    "transport": "sse",
}

client = MultiServerMCPClient(
    {
        "python_mcp": mcp_server_config
    }
)

async def acreate_agent():
    """
    必须是异步函数获取mcp tool
    """
    mcp_tool = await client.get_tools(server_name="python_mcp")
    print(mcp_tool)
    prompt = await client.get_prompt(server_name="python_mcp", prompt_name="ask_about_topic", arguments={"topic": "深度学习"})
    print(prompt)
    resource = await client.get_resources(server_name="python_mcp", uris="resource://config")
    print(resource)

    base_url = "https://qianfan.baidubce.com/v2/"
    api_key = "xxx"
    print(f"api_key is {api_key}")
    model = ChatOpenAI(
        model="deepseek-v3.1-250821",
        base_url=base_url,
        api_key=api_key
    )
    return create_agent(
        model=model,
        tools=mcp_tool,
        system_prompt="你是一个智能助手，尽可能的调用工具回答用户问题",
    )


# 异步主函数
async def main():
    # 创建代理
    agent = await acreate_agent()
    
    # 测试代理
    result = await agent.ainvoke({"messages": {"role": "human", "content": "1/1等于多少？"}})
    
    print("\n代理回答:")
    print(result)


# 运行异步主函数
if __name__ == "__main__":
    asyncio.run(main())
