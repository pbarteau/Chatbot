from groq import Groq
client = Groq(api_key="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")

print("Chatbot (Groq Streaming): Type 'exit', 'quit' or 'bye' to stop\n")

while True:
    prompt = input("You:")
    if prompt.lower() in ['exit', 'quit', 'bye']:
        print("\n Goodbye!")
        break

    print("Chatbot:", end="", flush=True)

    stream = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "user", "content": "Good boy!"},
            {"role": "user", "content": prompt}
        ],
        stream=True
    )

    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)

    print()   
