from typing import Text
from flask import Flask, render_template, request, redirect
import speech_recognition as sr
# from infer import load_audio
import webbrowser as wb

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def speechrecognized():
    transcript = ""
    text = ""

    if request.method == "POST":
            print("FORM DATA RECEIVED")

            if "file" not in request.files:
                return redirect(request.url)

            file = request.files["file"]
            if file.filename == "":
                return redirect(request.url)
            print('\n\nfile upoaded:', file.filename)

            if file:
                recognizer = sr.Recognizer()
                audioFile = sr.AudioFile(file)
                with audioFile as source:
                    data = recognizer.record(source)
                transcript = recognizer.recognize_google(data, language="vi")

    
    if request.method == "GET":
            r1 = sr.Recognizer()
            r2 = sr.Recognizer()
            r3 = sr.Recognizer()
            r4 = sr.Recognizer()

            with sr.Microphone() as source: #sử dụng đầu vào từ micro làm nguồn âm thanh
                print('[search video: search youtube]')
                print('speak now')
                audio = r3.listen(source) #nghe cụm từ đầu tiên rồi trích nó làm dữ liệu âm thanh

            if 'video' in r2.recognize_google(audio):
                r2 = sr.Recognizer()
                url = 'https://www.youtube.com/results?search_query='
                with sr.Microphone() as source:
                    print('search your query')
                    audio = r2.listen(source)

                    try:
                        text = r2.recognize_google(audio, language='vi')
                        print(text)
                        wb.get().open_new(url + text)
                        print("You said : {}".format(text))
                    except sr.UnknownValueError:
                        print('Error')
                    except sr.RequestError as e:
                        print('failed'.format(e))

            if 'video 1' in r1.recognize_google(audio):
                r1 = sr.Recognizer()
                url = 'https://www.google.com.vn/search?q='
                with sr.Microphone() as source:
                    print('search your query')
                    audio = r1.listen(source)

                    try:
                        text = r1.recognize_google(audio, language='vi')
                        print(text)
                        wb.get().open_new(url + text)
                        print("You said : {}".format(text))
                    except sr.UnknownValueError:
                        print('Error')
                    except sr.RequestError as e:
                        print('failed'.format(e))

            if 'video 2' in r4.recognize_google(audio):
                r4 = sr.Recognizer()
                url = 'https://www.facebook.com/search/top/?q='
                with sr.Microphone() as source:
                    print('search your query')
                    audio = r4.listen(source)

                    try:
                        text = r4.recognize_google(audio, language='vi')
                        print(text)
                        wb.get().open_new(url + text)
                        print("You said : {}".format(text))
                    except sr.UnknownValueError:
                        print('Error')
                    except sr.RequestError as e:
                        print('failed'.format(e))

            try:
                text = r2.recognize_google(audio, language='vi')
            except:
                print("Sorry could not recognize what you said")


    # return render_template('speechrecognized.html', transcript = transcript)
# audio_path='static/upload/11.wav
    return render_template('speechrecognized.html', text=text, transcript = transcript)
    


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
