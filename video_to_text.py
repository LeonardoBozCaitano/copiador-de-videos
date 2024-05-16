import speech_recognition as sr
from moviepy.editor import AudioFileClip
from pydub import AudioSegment

# Convert video to text
def convert_video(file):
    print("Convertendo o vídeo para áudio")

    audio_path = "./memory/audio_convertido.wav" 

    audioclip = AudioFileClip(file)
    audioclip.write_audiofile(audio_path)

    print("Vídeo convertido para áudio com sucesso")
    print("Convertendo o áudio para formato wav")

    audio = AudioSegment.from_file(audio_path, format="wav")
    audio.export("./memory/audio_convertido.wav", format="wav")

    print("Áudio convertido para wav com sucesso")

    convert_wav_to_text_free_version(audio)


def convert_wav_to_text_free_version(audio):
    print("Transcrevendo o áudio de gratis...")

    r = sr.Recognizer()

    interval = 30 * 1000
    duration_ms = len(audio)
    offset = 0

    transcription = ''

    while offset < duration_ms:
        t1 = offset 
        t2 = offset + interval 

        audio_segment = audio[t1:t2]

        audio_segment.export("./memory/temp.wav", format="wav")

        with sr.AudioFile('./memory/temp.wav') as source:
            audio_data = r.record(source)
            try:
                text = r.recognize_google(audio_data, language="pt-BR")
                print("Parte convertida pra texto com sucesso...")
                print(text)
                transcription += text + ' '
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

        offset += interval

    print("Transcrição concluída")
    with open('./output/transcricao.txt', 'w') as file:
        print("Salvando a transcrição em um arquivo")
        file.write(transcription)

    print("Transcrição salva com sucesso!")
