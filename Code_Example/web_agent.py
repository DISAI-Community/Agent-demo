import streamlit as st
import os
from dotenv import load_dotenv
from disai.disai_jazz import Agent, Task, OpenAIModel, SequentialFlow, InputType, OutputType
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
serp_api_key = os.getenv("SERP_API_KEY")

#Define agent properties
expertise = "Webagent"
task = Task("Search web and answer accordingly")
input_type = InputType("Text")
output_type = OutputType("Text")
agent = Agent(expertise, task, input_type, output_type)
api_key = openai_api_key
model = OpenAIModel(api_key=api_key,model="gpt-3.5-turbo",serp_api_key = os.getenv("SERP_API_KEY"))
sequential_flow = SequentialFlow(agent, model)

msg= sequential_flow.web_agent("When is the Next Iphone coming out?")
print(msg)