from transformers import AutoTokenizer, AutoModelForCausalLM, StoppingCriteria, StoppingCriteriaList
import torch
import sys
import time

class StreamCriteria(StoppingCriteria):
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer

    def __call__(self, input_ids, scores, **kwargs):
        # 마지막 토큰을 가져와 출력
        last_token = input_ids[0, -1].item()
        last_word = self.tokenizer.decode([last_token], skip_special_tokens=True)
        sys.stdout.write(last_word)  # 한 글자씩 출력
        sys.stdout.flush()  # 즉시 출력
        time.sleep(0.05)  # 자연스러운 출력 속도 조절 (선택 사항)
        return False  # False를 반환하면 계속 생성

# Load tokenizer
model_name = "deepseek-ai/DeepSeek-R1-Distill-Qwen-14B"
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Use CUDA if available, otherwise fallback to CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Load model **without quantization**
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16  # ✅ FP16 연산 적용
).to(device)

while True:
    user_input = input("\n문장을 입력하세요: ")
    inputs = tokenizer(user_input, return_tensors="pt").to(device)

    print("\n=== 생성된 텍스트 ===\n", end="", flush=True)

    stopping_criteria = StoppingCriteriaList([StreamCriteria(tokenizer)])

    model.generate(
        **inputs,
        max_length=500,
        temperature=0.7,
        do_sample=True,
        stopping_criteria=stopping_criteria  # ✅ 스트리밍 출력을 위한 조건 추가
    )

    print("\n")  # 줄바꿈 추가
