from transformers import pipeline

def generate_text(prompt):
    generator = pipeline("text-generation")
    return generator(prompt, max_length=50)