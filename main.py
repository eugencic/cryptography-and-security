from flask import Flask, request
import pyotp
import secrets

from Code.Caesar import *
from Code.CaesarPermutation import *
from Code.Vignere import *
from Code.Playfair import *
from Code.Stream import *
from Code.Hashing import *

from Code.Database import create_initial_db_resources, create_user, get_user, tokens

app = Flask(__name__)
app.config['SECRET_KEY'] = "LABORATORY_WORK_5"

admin_password = "4#17QZksEGi2"


@app.route('/')
def hello_world():
    return 'Laboratory Work Nr.5'


@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        register_data = {
            'email': data['email'],
            'password': data['password']
        }
        email = register_data['email']
        password = register_data['password']
        user_type = "user"
        secret_string = pyotp.random_base32()
        totp = pyotp.TOTP(secret_string)
        print("Creating user")
        create_user(email, password, user_type, secret_string)
        totp_uri = totp.provisioning_uri(name=email, issuer_name="Laboratory Work Nr.5")
        qr_uri = "https://chart.googleapis.com/chart?cht=qr&chs=500x500&chl=" + totp_uri
        return f'Access the link to get the Qr Code. Scan it using Google Authenticator: {qr_uri}'
    except Exception as e:
        print(str(e))
        return "Error occured! Please, check if you introduced the correct data, or ensure if you haven't registered " \
               "with this email already. "


@app.route('/admin', methods=['POST'])
def admin():
    try:
        data = request.get_json()
        register_data = {
            'email': data['email'],
            'password': data['password'],
            'secret': data['secret']
        }
        email = register_data['email']
        password = register_data['password']
        secret = register_data['secret']
        if secret != admin_password:
            return "Incorrect password to create admin."
        user_type = "admin"
        secret_string = pyotp.random_base32()
        totp = pyotp.TOTP(secret_string)
        print("Creating user")
        create_user(email, password, user_type, secret_string)
        totp_uri = totp.provisioning_uri(name=email, issuer_name="Laboratory Work Nr.5")
        qr_uri = "https://chart.googleapis.com/chart?cht=qr&chs=500x500&chl=" + totp_uri
        return f'Access the link to get the Qr Code. Scan it using Google Authenticator: {qr_uri}'
    except Exception as e:
        print(str(e))
        return "Error occured! Please, check if you introduced the correct data, or ensure if you haven't registered " \
               "with this email already. "


@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        login_data = {
            'email': data['email'],
            'password': data['password'],
            'otp': data['otp']
        }
        email = login_data['email']
        password = login_data['password']
        otp = login_data['otp']
        user = get_user(email)
        user_password = user[0][1]
        totp = user[0][3]
        totp = pyotp.TOTP(totp)
        if user_password != password:
            return "Incorrect password."
        if totp.now() != otp:
            return "Incorrect OTP code."
        alphabet = string.ascii_letters + string.digits
        if email not in tokens:
            token = ''.join(secrets.choice(alphabet) for i in range(8))
            tokens.update({email: token})
            return f'Login success! Use the token ({token}) to make requests.'
        token = tokens[email]
        print(tokens)
        return f'Already logged in! Use the token ({token}) to make requests.'
    except Exception as e:
        print(str(e))
        return "Something went wrong! Check if you introduced the correct data."


@app.route('/caesar', methods=['POST'])
def caesar():
    try:
        data = request.get_json()
        login_data = {
            'token': data['token'],
            'message': data['message'],
            'key': data['key']
        }
        token = login_data['token']
        user_message = login_data['message']
        user_key = login_data['key']
        if token not in tokens.values():
            return "Something went wrong! Check if you provided the correct token or if you are logged in."
        print("Caesar Cipher")
        caesarCipher = Caesar()
        message = user_message.upper()
        key = int(user_key)
        encrypted_message = caesarCipher.encrypt(message, key)
        decrypted_message = caesarCipher.decrypt(encrypted_message, key)
        return f'The original message: {message}, The encrypted message: {encrypted_message}, The decrypted message: ' \
               f'{decrypted_message}'
    except Exception as e:
        print(str(e))
        return "Error occurred!"


@app.route('/caesarpermutation', methods=['POST'])
def caesar_permutation():
    try:
        data = request.get_json()
        login_data = {
            'token': data['token'],
            'message': data['message'],
            'key': data['key'],
            'shift': data['shift']
        }
        token = login_data['token']
        user_message = login_data['message']
        user_key = login_data['key']
        user_shift = login_data['shift']
        if token not in tokens.values():
            return "Something went wrong! Check if you provided the correct token or if you are logged in."
        print("Caesar Permutation Cipher")
        caesarPermutationCipher = CaesarPermutation()
        message = user_message.upper()
        key = (user_key.upper()).replace(" ", "")
        shift = int(user_shift)
        new_alphabet = caesarPermutationCipher.alphabet_permutation(key)
        encrypted_message = caesarPermutationCipher.encrypt(message, new_alphabet, shift)
        decrypted_message = caesarPermutationCipher.decrypt(encrypted_message, new_alphabet, shift)
        return f'The original message: {message}, The new alphabet: {new_alphabet}, The encrypted message: ' \
               f'{encrypted_message}, The decrypted message: {decrypted_message}'
    except Exception as e:
        print(str(e))
        return "Error occurred!"


@app.route('/vignere', methods=['POST'])
def vignere():
    try:
        data = request.get_json()
        login_data = {
            'token': data['token'],
            'message': data['message'],
            'key': data['key'],
        }
        token = login_data['token']
        user_message = login_data['message']
        user_key = login_data['key']
        if token not in tokens.values():
            return "Something went wrong! Check if you provided the correct token or if you are logged in."
        print("Vignere Cipher")
        vignereCipher = Vignere()
        message = user_message.upper()
        keyword = (user_key.upper()).replace(" ", "")
        key = vignereCipher.generateKey(message, keyword)
        encrypted_message = vignereCipher.encrypt(message, key)
        decrypted_message = vignereCipher.decrypt(encrypted_message, key)
        return f'The original message: {message}, The encrypted message: {encrypted_message}, The decrypted message: ' \
               f'{decrypted_message}'
    except Exception as e:
        print(str(e))
        return "Error occurred!"


@app.route('/playfair', methods=['POST'])
def playfair():
    try:
        data = request.get_json()
        login_data = {
            'token': data['token'],
            'message': data['message'],
            'key': data['key'],
        }
        token = login_data['token']
        user_message = login_data['message']
        user_key = login_data['key']
        if token not in tokens.values():
            return "Something went wrong! Check if you provided the correct token or if you are logged in."
        print("Playfair Cipher")
        playfairCipher = Playfair()
        message = (user_message).upper().replace(" ", "")
        key = (user_key.upper()).replace(" ", "")
        encrypted_message = playfairCipher.playfair(message, key)
        decrypted_message = playfairCipher.playfair(encrypted_message, key, False)
        return f'The original message: {message}, The encrypted message: {encrypted_message}, The decrypted message: ' \
               f'{decrypted_message}'
    except Exception as e:
        print(str(e))
        return "Error occurred!"


@app.route('/stream', methods=['POST'])
def stream():
    try:
        data = request.get_json()
        login_data = {
            'token': data['token'],
            'message': data['message'],
            'key': data['key'],
        }
        user_token = login_data['token']
        user_message = login_data['message']
        user_key = login_data['key']
        if user_token not in tokens.values():
            return "Something went wrong! Check if you provided the correct token or if you are logged in."
        user_email = ''
        for email, token in tokens.items():
            if token == user_token:
                user_email = email
        user = get_user(user_email)
        user_type = user[0][2]
        if user_type != "admin":
            return "You don't have enough access rights."
        print("RC4 Stream Cipher")
        streamCipher = Stream()
        message = (user_message.upper()).replace(" ", "")
        key = (user_key.upper()).replace(" ", "")
        encrypted_message = streamCipher.encrypt(message, key)
        decrypted_message = streamCipher.decrypt(encrypted_message, key)
        return f'The original message: {message}, The encrypted message: {encrypted_message}, The decrypted message: ' \
               f'{decrypted_message}'
    except Exception as e:
        print(str(e))
        return "Error occurred!"


@app.route('/asymmetric', methods=['POST'])
def asymmetric():
    try:
        data = request.get_json()
        login_data = {
            'token': data['token'],
            'message': data['message'],
        }
        user_token = login_data['token']
        user_message = login_data['message']
        if user_token not in tokens.values():
            return "Something went wrong! Check if you provided the correct token or if you are logged in."
        user_email = ''
        for email, token in tokens.items():
            if token == user_token:
                user_email = email
        user = get_user(user_email)
        user_type = user[0][2]
        if user_type != "admin":
            return "You don't have enough access rights."
        print("RSA Asymmetric Cipher")
        asymmetricCipher = Asymmetric()
        private_key, public_key = asymmetricCipher.generate_rsa_keys()
        message = str(user_message)
        cipher = asymmetricCipher.encrypt(public_key, message)
        plain = asymmetricCipher.decrypt(private_key, cipher)
        return f'The original message: {message}, The encrypted message: {str(cipher)}, The decrypted message: {plain}'
    except Exception as e:
        print(str(e))
        return "Error occurred!"


@app.route('/hashing', methods=['POST'])
def hashing():
    try:
        data = request.get_json()
        login_data = {
            'token': data['token'],
            'message': data['message'],
        }
        user_token = login_data['token']
        user_message = login_data['message']
        if user_token not in tokens.values():
            return "Something went wrong! Check if you provided the correct token or if you are logged in."
        user_email = ''
        for email, token in tokens.items():
            if token == user_token:
                user_email = email
        user = get_user(user_email)
        user_type = user[0][2]
        if user_type != "admin":
            return "You don't have enough access rights."
        print("SHA-2 Hashing Algorithm")
        hashing = Hashing()
        message = str(user_message)
        result = hashing.SHA_256(message)
        asymmetricCipher = Asymmetric()
        private_key, public_key = asymmetricCipher.generate_rsa_keys()
        cipher = asymmetricCipher.encrypt(public_key, result)
        plain = asymmetricCipher.decrypt(private_key, cipher)
        if (plain == result):
            print("Digital signature checked successfully!")
        else:
            print("Error!")
        return f'The original message: {message}, The hashing result: {result}, The encrypted message: {str(cipher)}, ' \
               f'The decrypted message: {plain}'
    except Exception as e:
        print(str(e))
        return "Error occurred!"


if __name__ == "__main__":
    create_initial_db_resources()
    app.run(debug=True)


def start_app():
    return app
