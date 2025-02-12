import torch
print(torch.cuda.is_available())  # True이면 CUDA 사용 가능!
print(torch.cuda.device_count())  # 사용 가능한 GPU 개수 확인
print(torch.cuda.get_device_name(0))  # GPU 모델 확인
