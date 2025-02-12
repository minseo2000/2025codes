from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='deepseek-r1:14b', messages=[
    {
        'role' :'user',
        'content' : 'Please write hello world code in python',
    }
])
print(response['message']['content'])