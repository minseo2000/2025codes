from transformers import AutoTokenizer, AutoModelForCausalLM, StoppingCriteria, StoppingCriteriaList
import torch
import sys
import time


class StreamCriteria(StoppingCriteria):
    """실시간 단어 출력 (스트리밍 방식)"""

    def __init__(self, tokenizer):
        self.tokenizer = tokenizer

    def __call__(self, input_ids, scores, **kwargs):
        last_token = input_ids[0, -1].item()
        last_word = self.tokenizer.decode([last_token], skip_special_tokens=True)
        sys.stdout.write(last_word)
        sys.stdout.flush()
        time.sleep(0.05)  # 자연스러운 출력 속도 조절
        return False  # False를 반환하면 계속 생성


# ✅ 모델 및 토크나이저 로드
model_name = "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"
tokenizer = AutoTokenizer.from_pretrained(model_name)

# ✅ CUDA 사용 여부 확인
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"🔹 Using device: {device}")

# ✅ 모델 로드 (FP16 사용)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16
).to(device)

print("\n💬 [대화 시작] 문장을 입력하세요. (종료: Ctrl+C)\n")

try:
    while True:
        user_input = input("👤 사용자: ")

        if not user_input.strip():  # 빈 입력 방지
            print("⚠️ 문장을 입력하세요!")
            continue

        inputs = tokenizer(user_input, return_tensors="pt").to(device)

        print("\n🤖 모델:", end=" ", flush=True)

        stopping_criteria = StoppingCriteriaList([StreamCriteria(tokenizer)])

        model.generate(
            **inputs,
            max_length=500,
            temperature=0.7,
            do_sample=True,
            stopping_criteria=stopping_criteria
        )

        print("\n")  # 줄바꿈 추가

except KeyboardInterrupt:
    print("\n👋 대화를 종료합니다. 안녕히 가세요!")
