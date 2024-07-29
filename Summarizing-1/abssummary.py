
from transformers import BartForConditionalGeneration, BartTokenizer
import torch

# Load the pre-trained BART model and tokenizer
model_name = "facebook/bart-large-cnn"
model = BartForConditionalGeneration.from_pretrained(model_name)
tokenizer = BartTokenizer.from_pretrained(model_name)


def gen_abs_summary(text, max_length=600, min_length=40, num_beams=4):
    # Tokenize the input text
    inputs = tokenizer.encode(
         text, return_tensors="pt", max_length=1024, truncation=True
    )

    # Generate the summary
    summary_ids = model.generate(
        inputs,
        max_length=max_length,
        min_length=min_length,
        num_beams=num_beams,
        length_penalty=2.0,
        early_stopping=True,
    )

    # Decode the summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary, text, len(text.split()), len(summary.split())