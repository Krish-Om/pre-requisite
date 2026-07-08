import time

import tiktoken
from dotenv import dotenv_values
from google import genai

config = dotenv_values()
API_KEY = config["API_KEY"]
enc = tiktoken.encoding_for_model("gpt-4-o")

client = genai.Client(api_key=API_KEY)
text = "The quick brown fox jumps over the lazy dog."
tokens = enc.encode(text)
print(f"Tokens: {tokens}")
models_list = list(client.models.list())
models_name = [model.name for model in models_list]
# print(f"Models: {models_name}")
for name in models_name:
    total_tokens = client.models.count_tokens(model=name, contents=text)
    print(f"Total tokens for {name}: {total_tokens.total_tokens}")
    time.sleep(0.3)
