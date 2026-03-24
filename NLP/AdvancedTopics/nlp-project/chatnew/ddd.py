from openai import OpenAI

client = OpenAI(
    base_url="http://192.168.29.105:1234/v1",
    api_key="lm-studio"
)

messages = []

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="qwen3-vl-4b",
        messages=messages
    )

    reply = response.choices[0].message.content
    print("Bot:", reply)

    messages.append({"role": "assistant", "content": reply})