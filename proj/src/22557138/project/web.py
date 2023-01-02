from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from cipher import decrypt
from key_guess import key_guess
import os

indexpage = "index_en.html"
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.abspath(os.path.dirname(__file__))+'\\upload\\'


@app.route('/json', methods=['GET', 'POST'])
def jsonreply():
    jsonfile = request.json
    if list(jsonfile['properties'].keys())[0] == 'scret_msg':
        str_raw = jsonfile['properties']['scret_msg']['description']
        retdata = decrypt(str_raw, key_guess(str_raw))
        retfunc = 'decrypted_text'
    else:
        retfunc = 'format_error'
        retdata = 'request format error'
    retschema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "title": "Caesar Cipher Cracker Reply",
        "type": "object",
        "properties":
        {
            retfunc:
            {
                "type": "string",
                "description": retdata
            }
        },
        "required": [retfunc]
    }
    return jsonify(retschema)


@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        print(request.files)
        f.save(os.path.join(
            app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        file = open(os.path.join(
                app.config['UPLOAD_FOLDER']+secure_filename(f.filename)), "r", encoding="utf-8")
        t = file.read()
        file.close()
        if request.form['steps'] == "":
            s = key_guess(t)
            ps = "possible key is: " + str(s) + "\n"
        else:
            s = int(request.form['steps'])
            ps = ""
        func = request.form['func']
        if func == 'decrypt':
            return render_template(indexpage, data=ps+decrypt(t, s), fdecode="checked", fencode="")
        elif func == 'encrypt':
            return render_template(indexpage, data=ps+decrypt(t, -s), fdecode="", fencode="checked")
    else:
        return 'file uploaded failed\n<a href="/index">Back to Index</a>'


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        t = request.form['tarea']
        if request.form['steps'] == "":
            s = key_guess(t)
            ps = "possible key is: " + str(s) + "\n"
        else:
            s = int(request.form['steps'])
            ps = ""
        func = request.form['func']
        if func == 'decrypt':
            return render_template(indexpage, data=ps+decrypt(t, s), fdecode="checked", fencode="")
        elif func == 'encrypt':
            return render_template(indexpage, data=ps+decrypt(t, -s), fdecode="", fencode="checked")
    else:
        return render_template(indexpage)


if __name__ == '__main__':
    app.run()
