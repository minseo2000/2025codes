import torch
import wandb

from transformers import (

    AutoModelForCausalLM,
    AutoTokenizer,
    TrainingArguments,
    pipeline,
    Trainer
)
from transformers.integrations import WandbCallback
from trl import DataCollatorForCompletionOnlyLM
import evaluate

model_name = "google/gemma-2b-it"
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    use_cache=False,
    device_map="auto",
    torch_dtype=torch.bfloat16,
    low_cpu_mem_usage=True,
    attn_implementation="eager",
)
tokenizer = AutoTokenizer.from_pretrained(model_name)
