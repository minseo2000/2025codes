from transformers import AutoTokenizer, AutoModelForCausalLM, StoppingCriteria, StoppingCriteriaList
import torch
import sys
import time

class StreamCriteria(StoppingCriteria):
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer

    def __call__(self, input_ids, scores, **kwargs):
        last_token = input_ids[0, -1].item()
        last_word = self.tokenizer.decode([last_token], skip_special_tokens=True)
        sys.stdout.write(last_word)
        sys.stdout.flush()
        time.sleep(0.05)  # 자연스러운 출력 속도 조절
        return False

# ✅ 필수 패키지 설치
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
    torch_dtype=torch.float16,
    load_in_4bit=True,  # ✅ 4-bit 양자화 적용
    bnb_4bit_compute_dtype=torch.float16,  # ✅ 연산은 FP16 유지
).to(device)

# ✅ 시스템 프롬프트 설정
system_prompt = "마지막 답변은 반드시 한국말(korean)로 답변해줘."

while True:
    user_input = input("\n문장을 입력하세요: ")

    # 사용자 입력과 시스템 프롬프트 결합
    full_input = f"시스템: {system_prompt}\n사용자: {user_input}\nAI:"

    inputs = tokenizer(full_input, return_tensors="pt").to(device)

    print("\n=== 생성된 텍스트 ===\n", end="", flush=True)

    stopping_criteria = StoppingCriteriaList([StreamCriteria(tokenizer)])

    model.generate(
        **inputs,
        max_length=1200,
        temperature=0.7,
        do_sample=True,
        stopping_criteria=stopping_criteria  # ✅ 스트리밍 출력을 위한 조건 추가
    )

    print("\n")  # 줄바꿈 추가
