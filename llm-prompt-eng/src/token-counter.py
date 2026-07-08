import tiktoken

texts = [
    "Hello",
    "What's up man?",
    "fas;dlfj",
]

encoder = tiktoken.encoding_for_model("gpt-4o")
for text in texts:
    tokens = encoder.encode(text)
    print(f"Number of tokens: {len(tokens)}")
