import whisper
import os

# Set audio file name
filename = "harshdeep.mp3"

# Step 1: Check if file exists
print("Checking audio file...")
if not os.path.exists(filename):
    print(f" File not found: {filename}")
    exit()

# Step 2: Load Whisper model
print("Loading Whisper model...")
model = whisper.load_model("small")

# Step 3: Transcribe with forced English
print("Transcribing audio...")
result = model.transcribe(filename, language="en")

# Step 4: Output the result
print("✅ Full Result:", result)
print("📝 Transcript:", result["text"])

from transformers import MarianMTModel, MarianTokenizer

# Example: English to Hindi
src_lang = "en"
tgt_lang = "hi"
model_name = f"Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}"

tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

translated = model.generate(**tokenizer.prepare_seq2seq_batch(result["text"], return_tensors="pt"))
translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)

print("Translated Text:", translated_text)
