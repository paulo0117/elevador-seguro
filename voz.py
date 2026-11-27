# A voz é um extra. Se o pyttsx3 não estiver instalado, o programa só mostra o texto.
try:
    import pyttsx3
    motor_de_voz = pyttsx3.init()
except Exception:
    motor_de_voz = None


def falar(texto):
    """O alto-falante da cabine: mostra na tela e, se der, fala em voz alta."""
    print(f"[CABINE] {texto}")
    if motor_de_voz is not None:
        motor_de_voz.say(texto)
        motor_de_voz.runAndWait()


def ouvir():
    """O microfone da cabine: o passageiro digita o que falaria."""
    return input("[PASSAGEIRO] ").strip().lower()
