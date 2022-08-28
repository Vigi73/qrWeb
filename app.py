from flask import Flask, url_for,  render_template, request
import qrcode

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    with open('download.txt') as f:
        download = int(f.readline().strip())
    return render_template('index.html', image='logo.png', download=download)


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

    with open('download.txt') as fr:
        fl = int(fr.read().strip())
        fl += 1
    with open('download.txt', 'w') as fw:
        fw.write(str(fl))

    return render_template('index.html', image='qr.png', download=fl)


if __name__ == '__main__':
    app.run(debug=True)
