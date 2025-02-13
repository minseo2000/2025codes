import gradio as gr
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# ✅ 필수 패키지 설치 확인
try:
    import bitsandbytes as bnb
except ImportError:
    print("❌ 'bitsandbytes'가 설치되지 않았습니다. 설치하려면 'pip install bitsandbytes' 실행하세요.")
    exit()

# ✅ 모델 및 토크나이저 로드
model_name = "deepseek-ai/DeepSeek-R1-Distill-Qwen-32B"
tokenizer = AutoTokenizer.from_pretrained(model_name)

# ✅ CUDA 사용 여부 확인
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# ✅ 4-bit 양자화 적용하여 모델 로드
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,  # 연산은 FP16 유지
    load_in_4bit=True,  # ✅ 4-bit 양자화 적용
    bnb_4bit_compute_dtype=torch.float16,  # ✅ 4-bit 양자화 연산 설정
).to(device)

# ✅ 챗봇 함수 정의
def chatbot(user_input):
    inputs = tokenizer(user_input, return_tensors="pt").to(device)
    output = model.generate(**inputs, max_length=5000, temperature=0.7, top_p=0.9, do_sample=True)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

# ✅ Gradio UI 인터페이스
iface = gr.Interface(
    fn=chatbot,
    inputs="text",
    outputs="text",
    title="DeepSeek AI Chatbot (4-bit Quantized)"
)

iface.launch()
