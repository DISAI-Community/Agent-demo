import os
from dotenv import load_dotenv
from disai.disai_jazz import Agent, Task, OpenAIModel, SequentialFlow, InputType, OutputType
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
expertise = "Digital Art"
task = Task("Image Generation")
input_type = InputType("Text")
output_type = OutputType("Image")
agent = Agent(expertise, task, input_type, output_type)
model = OpenAIModel(api_key=openai_api_key,model="dall-e-3")
sequential_flow = SequentialFlow(agent, model)

user_prompt = "a futuristic cityscape"
generated_image_url = sequential_flow.execute(user_prompt)
print(f"Generated Image URL: {generated_image_url}")
