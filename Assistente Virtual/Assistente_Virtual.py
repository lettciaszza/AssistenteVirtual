import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import os

audio = sr.Recognizer()
maquina = pyttsx3.init()
maquina.say('Olá, eu sou a Letícia, o que deseja saber?')
maquina.runAndWait()

def executa_comando():

    try:
        with sr.Microphone() as source:
            print('Ouvindo...')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()

            if 'Letícia' in comando:
                comando = comando.replace('Letícia', '')
                maquina.say(comando)
                maquina.runAndWait()
    except:
        print('Microfone não está funcionando')
    return comando

def comando_voz_usuario():
    comando = executa_comando()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são' + hora)
        maquina.runAndWait()
    elif 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'navegador' in comando:
		        os.system("start Brave.exe")  
    elif 'toque' in comando:
        musica = comando.replace('toque', '')
        resultado = pywhatkit.playonyt(musica)
        maquina.say('Tocando musica')
        maquina.runAndWait()

    elif 'canal do youtube' in comando:
        canal = comando.replace('canal do youtube', '')
        resultadoCanal = pywhatkit.playonyt(canal)
        maquina.say('Encontrar canal')
        maquina.runAndWait()

comando_voz_usuario()