
from flask import Flask, render_template, request
import hashlib
import base64
from Crypto.Cipher import AES
from Crypto import Random

app = Flask(__name__)
size = 32
pad = lambda s: s.decode('utf-8') + ((size - len(s) % size) * chr(size - len(s) % size))
unpad = lambda s : s[:-ord(s[len(s)-1:])]


@app.route('/')
def hello_world():
    return render_template('test.html')

@app.route('/encrypt', methods=['POST', 'GET'])
def encryptdata():
    data_json = request.json
    data = data_json['data'].encode('utf-8')
    password = data_json['password'].encode('utf-8')
    key = hashlib.sha256(password).digest()
    padded_data = pad(data)
    vector = Random.new().read( AES.block_size )
    cipher = AES.new( key, AES.MODE_CBC, vector )
    return base64.b64encode( vector + cipher.encrypt( padded_data ) )


@app.route('/decrypt', methods=['POST', 'GET'])
def decryptdata():
    data_json = request.json
    data = data_json['data'].encode('utf-8')
    password = data_json['password'].encode('utf-8')
    key = hashlib.sha256(password).digest()
    data_decoded = base64.b64decode(data)
    vector = data_decoded[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, vector)
    return unpad(cipher.decrypt(data_decoded[AES.block_size:]))

