import whisper
import librosa
from record_audio import record_audio_file
import text_processor as tp



def filter_question_type(question_type):
    print(question_type['question_type'])
    if question_type['question_type'] == "General Inquiry":
        result = tp.general_inquiry_info_gathering()
        print(result)
        return "general"
    elif question_type['question_type'] == "Technical Support":
        result = tp.tech_support_info_gathering(requester_name=None, project_name=None, email=None)
        print(result)
        return "technical"
    elif question_type['question_type'] == "Sales Inquiry":
        return "sales"
    return question_type(question_type['question_type'])


model = whisper.load_model("turbo")  # or "small", "medium", "large"
# record_audio_file("audio.wav", duration=10, fs=44100)
audio, sr = librosa.load("./src/audio.wav", sr=16000)  # Load
result = model.transcribe(audio, language="nl")
text = result["text"]
print(f"Transcribed text: {text}")
question_type = tp.categorize_request(text)
filter_question_type(question_type)


