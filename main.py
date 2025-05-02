from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

gpt_4o = init_chat_model("gpt-4o", model_provider="openai", temperature=0)

output = gpt_4o.invoke("Why is the sky blue?")

print(output.content)

print("Hello World!")