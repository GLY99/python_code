"""
Docstring for graph_state.graph_state
1. graph状态是存放工作流运行过程中所有messages以及状态的变化。
2. 在所有node的输入中都默认会注入这个状态，状态中的数据可以在任意node中获取到。
3. 所有node返回的内容都会更新到状态对应的key。
4. 状态类一般都继承自TypedDict或者BaseModel或者graph提供的MessagesState。
5. 状态的key如果没有定义reducer函数那么在更新状态时会进行覆盖而不是追加，只有通过Annotated增加reducer函数才能实现追加
messages: List[str] 这个就是覆盖
messages: Annotated[List[str], add] 这个就会追加，add就是reducer函数，来自operator.add_messages也是一种reducer函数
"""
from langchain.agents import create_agent
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from typing import TypedDict, Literal
from pydantic import BaseModel, Field

class State(TypedDict):  # MessagesState其实就是继承自TypedDict然后预先定义了messages: Annotated[list[AnyMessage], add_messages]
    joke: str
    topic: str
    feedback: str
    funny_or_not: str


class FeedBack(BaseModel):
    grade: Literal["funny", "not_funny"] = Field(description="判断笑话是否幽默", examples=["funny", "not_funny"])
    feedback: str = Field(description="若不幽默，提出改进建议", examples=["可以加入双关语或者意外结局"])


base_url = "https://qianfan.baidubce.com/v2/"
api_key = "xxx"
model = ChatOpenAI(
    model="deepseek-v3.1-250821",
    base_url=base_url,
    api_key=api_key
)


def generatoer_joke(state: State):
    """
    generatoer joke
    """
    prompt = (
        f"根据反馈改进笑话：{state["feedback"]}\n主题：{state["topic"]}\n"
        if state.get("feedback", None) else f"生成一个关于{state["topic"]}的冷笑话"
    )
    # 使用agent
    agent = create_agent(
        model=model,
        system_prompt="你是一个笑话生成助手，需要你根据输入生成笑话或者改进笑话"
    )
    resp = agent.invoke({"messages": {"role": "human", "content": prompt}})
    return {"joke": resp["messages"][-1].content}
    
    # 直接使用model
    # resp = model.invoke(prompt)
    # return {"joke": resp.content}


def avaluator_joke(state: State):
    """
    avaluator_joke
    """
    # 结构化输出
    
    # 第一种
    # chain = model.with_structured_output(FeedBack)
    # resp = chain.invoke(f"评估此笑话的幽默程度：{state["joke"]}\n注意：幽默应该包含意外性或者巧妙措辞")
    # return {
    #     "feedback": resp.feedback,
    #     "funny_or_not": resp.grade
    # }
    
    # 第二种
    chain = model.bind_tools([FeedBack])
    evaluation = chain.invoke(f"评估此笑话的幽默程度：{state["joke"]}\n注意：幽默应该包含意外性或者巧妙措辞")
    resp = evaluation.tool_calls[-1]["args"]
    return {
        "feedback": resp["feedback"],
        "funny_or_not": resp["grade"]
    }


def router_func(state: State) -> str:
    """
    rotuer func
    """
    return (
        END if state["funny_or_not"] == "funny" else "generator_joke"
    )


if __name__ == "__main__":
    # 构建一个工作流
    builder = StateGraph(State)

    builder.add_node("generator_joke", generatoer_joke)
    builder.add_node("avaluator_joke", avaluator_joke)

    builder.add_edge(START, "generator_joke")
    builder.add_edge("generator_joke", "avaluator_joke")
    builder.add_conditional_edges(
        "avaluator_joke",
        router_func
    )

    graph = builder.compile()

    
    state = State(topic="北极熊")
    resp = graph.invoke(state)
    print(resp["joke"])
