import asyncio
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.runnables import RunnableConfig

"""
测试短期记忆存储
"""


async def main():
    """
    init agent
    """
    base_url = "https://qianfan.baidubce.com/v2/"
    api_key = "xxx"
    """
    无checkpointer:
    请输入问题：我叫张三
    你好张三！很高兴认识你！请问有什么可以帮助你的吗？比如生活技巧、日常疑问或者你需要建议的事情？😊
    请输入问题：请问我叫什么？
    很抱歉，我不知道您的名字哦！😊 如果您愿意告诉我的话，我可以记住并在以后的对话中称呼您。或者您现在有什么其他问题需要我帮忙吗？

    有checkpointer:
    请输入问题：我叫张三
    你好张三！很高兴认识你！在这里我可以帮你解决生活中的各种问题，比如提供实用建议、制定计划、分享小技巧等等～

    有什么我可以帮你的吗？
    请输入问题：请问我叫什么
    你的名字是张三哦！刚刚我们互相介绍过的～ 😊 需要我帮你记住什么信息吗？
    """
    checkpointer = InMemorySaver()  # 如果没有这个做短期存储那么你运行这个代码后它不会记住你之前的对话信息
    model = ChatOpenAI(
        model="deepseek-v3.1-250821",
        base_url=base_url,
        api_key=api_key
    )
    agent = create_agent(
        model=model,
        system_prompt="你是一个生活小助手，你需要尽可能回答用户问题",
        checkpointer=checkpointer
    )

    while True:
        human_message = input("请输入问题：")
        async for chunk in agent.astream(
            input={"messages": {"role": "human", "content": human_message}},
            config=RunnableConfig(configurable={"thread_id": "1"})
        ):
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




