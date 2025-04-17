from optimum.intel import OVModelForCausalLM
from transformers import AutoTokenizer, pipeline
from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments, TextDataset, DataCollatorForLanguageModeling

# Load GPT-2 and tokenizer
model_id = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = GPT2LMHeadModel.from_pretrained(model_id)  # Use PyTorch model for training

# Set up inference pipeline
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Add padding if missing
tokenizer.pad_token = tokenizer.eos_token

# Load dataset
def load_dataset(file_path, tokenizer, block_size=128):
    return TextDataset(
        tokenizer=tokenizer,
        file_path=file_path,
        block_size=block_size
    )

train_dataset = load_dataset("./dataset.json", tokenizer)



# Data collator
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=False
)

# Training arguments (CPU-based)
training_args = TrainingArguments(
    output_dir="./gpt2-quest",
    overwrite_output_dir=True,
    num_train_epochs=10,
    per_device_train_batch_size=1,
    save_steps=10,
    save_total_limit=2,
    prediction_loss_only=True,
    logging_steps=2
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset
)

# Train model
trainer.train()

# Save
trainer.save_model("./gpt2-quest")
tokenizer.save_pretrained("./gpt2-quest")
