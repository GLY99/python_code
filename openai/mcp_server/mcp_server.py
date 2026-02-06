from fastmcp import FastMCP
from fastmcp.prompts.prompt import Message
from typing import Tuple


server = FastMCP(name="my_mcp")


@server.tool(name="calculate_tool")
def calculate_tool(num1: float, num2: float, operation: str) -> Tuple[float, str]:
    """
    计算工具
    """
    if operation in ["+", "add", "加"]:
        return num1 + num2, ""
    if operation in ["/", "除", "÷", "divide", "division"]:
        return num1 / num2, ""
    if operation in ["*", "乘"]:
        return num1 * num2, ""
    if operation in ["-", "减"]:
        return num1 - num2, ""
    return -1, "无法计算结果"


@server.prompt
def ask_about_topic(topic: str) -> str:
    """
    生成特定主题的用户消息模板
    """
    return f"能否解释一下{topic}这个概念?"


@server.prompt
def gen_code_request(language: str, task_description: str) -> Message:
    """
    生成代码编写的用户消息请求模板
    """
    content = f"请用{language}编写一个实现一下功能的函数: {task_description}"
    return Message(role="user", content=content)


@server.resource(uri="resource://config")
def get_config() -> dict:
    """
    以json格式返回应用配置
    """
    return {
        "theme": "dark",
        "version": "1.1.1",
        "features": ["tools", "resources"]
    }



if __name__ == '__main__':
    server.run(transport="sse", host="0.0.0.0", port=8080, log_level="debug", path="/sse")
