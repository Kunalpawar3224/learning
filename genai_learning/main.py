from groq import Groq
# api_key = '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'


def chatbot(message):
    client = Groq(api_key=api_key)
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
        {
            "role": "user",
            "content": message
        }
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False,
        stop=None
    )
    return completion.choices[0].message.content
# for chunk in completion:
#     print(chunk.choices[0].delta.content or "", end="")
