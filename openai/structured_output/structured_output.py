"""
llm 格式化输出
"""
from langchain_core.output_parsers import SimpleJsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


class Movie(BaseModel):
    """
    infomation for movie
    """
    title: str = Field(..., description="电影标题")
    year: int = Field(..., description="电影发行年份")
    director: str = Field(..., description="电影导演")
    rating: float = Field(..., description="电影评分（满分10分）")

base_url = "https://qianfan.baidubce.com/v2/"
api_key = "xxx"
llm = ChatOpenAI(
    model="deepseek-v3.1-250821",
    base_url=base_url,
    api_key=api_key
)

# 方式 1:
chain = llm.with_structured_output(Movie, include_raw=False)  # include_raw可以返回原始的ai message信息
response = chain.invoke("提供电影盗梦空间的详细信息")
print(type(response), ':', response)  # <class '__main__.Movie'>：title='盗梦空间' year=2010 director='克里斯托弗·诺兰' rating=8.8

# 方式 2:
prompt = ChatPromptTemplate.from_template(
    "尽可能回答用户所有问题"  # 基本指令
    '你必须始终输出一个包含"title", "year", "director", "rating"键的JSON对象'
    "{question}"  # 用户问题占位符
)
chain = prompt | llm | SimpleJsonOutputParser()
response = chain.invoke("提供电影盗梦空间的详细信息")
print(type(response), ':', response)
"""
返回结果：
<class 'dict'> : 
{
    'title': '盗梦空间',
    'originalTitle': 'Inception', 
    'year': 2010, 
    'director': '克里斯托弗·诺兰', 
    'rating': 9.4, 
    'description': '一名技术高超的盗贼通过潜入他人梦境来窃取机密信息，这次他被赋予了一项看似不可能的任务——在目标潜意识中植入一个想法。', 
    'genre': ['科幻', '动作', '惊悚'], 
    'duration': '148分钟', 
    'leadActor': '莱昂纳多·迪卡普里奥'
}
"""

# 方式 3：
chain = llm.bind_tools([Movie])
evaluation = chain.invoke("提供电影盗梦空间的详细信息")
response = evaluation.tool_calls[-1]["args"]
print(type(response), ':', response)  # <class 'dict'> : {'title': '盗梦空间', 'year': 2010, 'director': '克里斯托弗·诺兰', 'rating': 8.8}