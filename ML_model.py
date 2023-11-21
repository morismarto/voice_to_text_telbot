import whisper

def speech_rec(model = 'base'):
    speech_model = whisper.load_model(model)
    result = speech_model.transcribe('media/res.mp3', fp16=False, language='Russian')
    return result['text']







