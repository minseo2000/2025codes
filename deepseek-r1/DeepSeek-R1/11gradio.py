import gradio as gr
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# 모델 및 토크나이저 로드
model_name = "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = AutoModelForCausalLM.from_pretrained(
    model_name, torch_dtype=torch.float16
).to(device)

def chatbot(user_input):
    inputs = tokenizer(user_input, return_tensors="pt").to(device)
    output = model.generate(**inputs, max_length=5000, temperature=0.7, top_p=0.9, do_sample=True)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

iface = gr.Interface(fn=chatbot, inputs="text", outputs="text", title="DeepSeek AI Chatbot")
iface.launch()
