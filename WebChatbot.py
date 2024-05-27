import streamlit as st
import os
from dotenv import load_dotenv
from disai.disai_jazz import Agent, Task, OpenAIModel, SequentialFlow, InputType, OutputType
load_dotenv()


openai_api_key = os.getenv("OPENAI_API_KEY")
#Define agent properties
expertise = "Webagent"
task = Task("Search web and answer accordingly")
input_type = InputType("Text")
output_type = OutputType("Text")
agent = Agent(expertise, task, input_type, output_type)
api_key = openai_api_key
model = OpenAIModel(api_key=api_key,model="gpt-3.5-turbo")
sequential_flow = SequentialFlow(agent, model)

st.title("💬 DSAI Webagent ")
st.caption("🚀 A Streamlit chatbot powered by DSAI Framework")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hi I'm a webagent, I am an LLM connected to the internet, ask me! 😊"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    msg= sequential_flow.web_agent(prompt)
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
