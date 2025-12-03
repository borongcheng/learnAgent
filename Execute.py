import os
import re

import ExecuteAgent
import Prompt
from OpenAICompatibleClient import OpenAICompatibleClient

TAVILY_API_KEY = "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"
os.environ["TVLY_API_KEY"] = TAVILY_API_KEY

llm = OpenAICompatibleClient(model=ExecuteAgent.MODE_ID,
                                    api_key=ExecuteAgent.API_KEY,
                                    base_url=ExecuteAgent.BASE_URL);
#--  初始化 --
user_prompt = "你好，帮我查询一下杭州今天的天气，然后根据天气推荐一个合适的景点"
prompt_history = [f"{user_prompt}"]

print(f"用户输入: {user_prompt}")
print(f"用户输入: {user_prompt}\n" + "="*40)

#-- 运行主循环 --
for i in range(5): # 设置最大循环次数5
    print(f"----------循环次数{i + 1}")

    # 1、构建prompt
    full_prompt = "/n".join(prompt_history)

    llm_output = llm.generate(full_prompt, system_prompt=Prompt.AGENT_SYSTEM_PROMPT)
    # 通过正则去掉thought部分
    match = re.search(r'(Thought:.*?Action:.*?)(?=\n\s*(?:Thought:|Action:|Observation:)|\Z)', llm_output, re.DOTALL)
    #if match:
