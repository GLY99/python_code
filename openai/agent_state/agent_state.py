import asyncio
from langchain.agents import AgentState, create_agent
from langchain.messages import ToolMessage
from langchain_core.tools import tool, InjectedToolCallId
from langchain_core.runnables import RunnableConfig
from langgraph.prebuilt import InjectedState
from langgraph.types import Command
from langchain_openai import ChatOpenAI
from typing import Annotated

# 动态配置
class MyState(AgentState):
    username: str


@tool
def get_user_name(tool_call_id: Annotated[str, InjectedToolCallId], config: RunnableConfig) -> Command:
    """
    获取当前用户的用户名用于生成祝福语句
    """
    username = config["configurable"].get("username", 'not found username from config["configurable"]')
    print(f"call get_user_name: username is {username}")
    return Command(
        update={
            "username": username,
            "messages": [ToolMessage(tool_call_id=tool_call_id, content="成功得到当前用户名")]
        }
    )


@tool
def greet_user(state: Annotated[MyState, InjectedState]) -> str:
    """
    生成祝福语句
    """
    print(f"call greet_user: state is {state}")
    username = state["username"]
    return f"祝福你，{username}"

async def main():
    """
    init agent
    """
    base_url = "https://qianfan.baidubce.com/v2/"
    api_key = "xxx"
    print(f"api_key is {api_key}")
    model = ChatOpenAI(
        model="deepseek-v3.1-250821",
        base_url=base_url,
        api_key=api_key
    )
    agent = create_agent(
        model=model,
        tools=[get_user_name, greet_user],
        system_prompt="你需要根据用户提供的名字生成祝福语句",
        state_schema=MyState  # 指定agent状态
    )

    # config：RunnableConfig 这是静态配置
    async for chunk in agent.astream(input={"messages": {"role": "human", "content": "给当前用户生成祝福语句"}}, config=RunnableConfig(configurable={"username": "王五"})):
        # print(chunk)
        ai_messages = chunk.get("model", {}).get("messages")
        tool_messages = chunk.get("tools", {}).get("messages")
        if ai_messages and len(ai_messages) > 0:
            print(ai_messages[0].content)
        if tool_messages and len(tool_messages) > 0:
            print(tool_messages[0].content)


if __name__ == "__main__":
    """
    start ai agent
    """
    asyncio.run(main())




