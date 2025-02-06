# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from tqdm import tqdm  # Import tqdm for progress bar

# Free MPS memory before running
if torch.backends.mps.is_available():
    torch.mps.empty_cache()
    torch.mps.synchronize()

# Load tokenizer and model
model_name = "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Check if MPS (Apple GPU) is available, otherwise use CPU
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
print(f"Using device: {device}")

# Load model onto the selected device
model = AutoModelForCausalLM.from_pretrained(model_name)
model.to(device)

# Set pad token ID (to avoid warnings)
tokenizer.pad_token = tokenizer.eos_token


while True:
    # 사용자 입력 받기
    user_input = input("\n문장을 dd 입력하세요: ")

    # 입력 문장 토큰화
    inputs = tokenizer(user_input, return_tensors="pt", padding=True, truncation=True)
    input_ids = inputs.input_ids.to(device)
    attention_mask = inputs.attention_mask.to(device)

    # Maximum length of generated text
    max_length = 100  # 속도와 메모리 절약을 위해 100으로 설정

    # Create a progress bar
    print("\nGenerating text...")
    generated_ids = input_ids  # 초기 입력값 설정
    progress_bar = tqdm(total=max_length, desc="Generating", unit="token")

    # Step-by-step token generation
    for _ in range(max_length):
        output = model.generate(
            input_ids,
            attention_mask=attention_mask,
            max_length=100,  # 🚀 max_new_tokens 대신 사용
            temperature=0.7,
            top_k=50,
            top_p=0.9,
            repetition_penalty=1.2,
            pad_token_id=tokenizer.pad_token_id,
            do_sample=True,
        )

        # 새 토큰 추가
        new_token_id = output[0, -1].unsqueeze(0).unsqueeze(0)  # 마지막 생성된 토큰 추출
        generated_ids = torch.cat([generated_ids, new_token_id], dim=-1)  # 새로운 토큰 추가

        # 진행률 바 업데이트
        progress_bar.update(1)

        # 만약 모델이 EOS(종료) 토큰을 생성하면 종료
        if new_token_id.item() == tokenizer.eos_token_id:
            break

    progress_bar.close()  # 진행 완료 후 tqdm 종료

    # 생성된 문장 디코딩
    generated_text = tokenizer.decode(generated_ids[0], skip_special_tokens=True)

    # 결과 출력
    print("\n=== 생성된 텍스트 ===")
    print(generated_text)
