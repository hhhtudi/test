# 导入库
import streamlit as st
from openai import OpenAI

# —————— 配置 AI 模型 ——————
# 这里可以用任何兼容 OpenAI 格式的大模型
client = OpenAI(
    api_key="sk-aa36646db4ef4af9901f02c4a56ba7b0",  # 去平台申请
    base_url="https://api.deepseek.com"  # 可替换成其他模型地址
)

# —————— 网页界面 ——————
st.title("我的 AI 助手")
st.subheader("用 AI 快速开发并部署的软件")

# 用户输入
user_input = st.text_input("你想问 AI 什么问题？")

# —————— AI 核心逻辑 ——————
if user_input:
    # 调用 AI
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": user_input}]
    )
    # 显示结果
    st.success("AI 回答：")
    st.write(response.choices[0].message.content)