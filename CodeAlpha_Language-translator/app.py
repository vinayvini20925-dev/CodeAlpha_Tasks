from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    translated_text = ""

    if request.method == "POST":
        text = request.form.get("text")
        language = request.form.get("language")

        try:
            translated_text = GoogleTranslator(source='auto', target=language).translate(text)
        except:
            translated_text = "Translation Error"

    return render_template("index.html", translated_text=translated_text)

if __name__ == "__main__":
    app.run(debug=True)