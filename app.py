from flask import Flask, url_for, redirect, render_template, request
import qrcode


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', image='logo.jpg')


@app.route('/qr', methods=['GET'])
def qr():
    return render_template('qr.html')


@app.route('/get_code', methods=['POST'])
def get_code():
    fio = request.form['fio']
    phone = request.form['phone']
    email = request.form['email']

    text = f'👤 {fio}\n☎ {phone}\n📧  {email}\n'

    img = qrcode.make(text)
    img.save('static/images/qr.png')

    return render_template('index.html', image='qr.png')


if __name__ == '__main__':
    app.run()
