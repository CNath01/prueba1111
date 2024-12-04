import speech_recognition as speech_recog

def speech():
    mic = speech_recog.Microphone()
    recog = speech_recog.Recognizer()

    with mic as audio_file:
        recog.adjust_for_ambient_noise(audio_file)
        print("Por favor, pronuncie la palabra...")
        audio = recog.listen(audio_file)
        try:
            # Intenta reconocer el audio
            recognized_text = recog.recognize_google(audio, language="es-ES")
            print(f"Texto reconocido: {recognized_text}")  # Muestra el texto reconocido
            return recognized_text
        except speech_recog.UnknownValueError:
            print("No se pudo entender el audio.")
            return None
        except speech_recog.RequestError as e:
            print(f"No se pudo solicitar resultados del servicio de reconocimiento de voz; {e}")
            return None