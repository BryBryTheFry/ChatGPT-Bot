from pathlib import Path
from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech
from tempfile import NamedTemporaryFile
from playsound import playsound
from datasets import load_dataset
import torch
from transformers import SpeechT5HifiGan
import soundfile as sf

temp_file = NamedTemporaryFile().name
speech_file_path = temp_file + ".mp3"

processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")

inputs = processor(text="Don't count the days, make the days count.", return_tensors="pt")

embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
speaker_embeddings = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)

spectrogram = model.generate_speech(inputs["input_ids"], speaker_embeddings)

vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")

with torch.no_grad():
    speech = vocoder(spectrogram)

speech = model.generate_speech(inputs["input_ids"], speaker_embeddings, vocoder=vocoder)

sf.write(speech_file_path, speech.numpy(), samplerate=16000)

playsound(speech_file_path)
