import openai

def get_initial_message():
    messaage=[
        {
        "role":"system",
        "content":"you are an helpful tutor who answers questions on AI in short"
        },
        {
            "role":"user",
            "content":"Hi, i want to learn about artficial intelligence"
        },
        {
            "role":"system",
            "content":"Hey, thats great what do you learn about?"
        }

    ]
    return messaage

def bot_reponse(messages,model="gpt-3.5-turbo-0301"):
    response=openai.ChatCompletion.create(
        model=model,
        messages=messages
    )
    return response['choices'][0]['message']['content']


def update_chat(messages,role,content):
    messages.append({
        "role":role,
        "content":content
    })
    return messages 
