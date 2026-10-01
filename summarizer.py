import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct"
print("Loading model...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float32
)
print("Model loaded successfully!")
def summarize_medical_report(text, language="English"):

    prompt = f"""
You are a medical report summarization assistant.

Your task is to simplify the following medical report for a patient.

Important rules:
- Do not diagnose the patient.
- Do not invent medical information.
- Do not change numerical values.
- Do not recommend medication.
- Explain medical terminology in simple language.
- Clearly separate findings from general explanations.
- Mention important abnormal findings when present.
- If information is unclear, say that it is unclear.
- Tell the user to consult a qualified healthcare professional for medical interpretation.

Write the summary in {language}.

Medical Report:
{text}

Provide the response using these sections:

1. Simple Summary
2. Important Findings
3. Medical Terms Explained
4. Questions to Discuss With a Doctor
5. Disclaimer
"""

    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]

    formatted_prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    inputs = tokenizer(
        formatted_prompt,
        return_tensors="pt"
    ).to(model.device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=800,
            temperature=0.3,
            do_sample=True,
            top_p=0.9
        )

    generated_tokens = outputs[0][inputs["input_ids"].shape[1]:]

    result = tokenizer.decode(
        generated_tokens,
        skip_special_tokens=True
    )

    return result
