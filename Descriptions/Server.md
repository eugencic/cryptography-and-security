# Web Authentication & Authorisation.

## Theory

### What is Authentication?

Often confused with Authorization, Authentication is essentially verifying the true identity of an entity. It enables access control by proving that a user’s credentials match those in an authorized user’s database. Identity verification can ensure system security, process security, and corporate information security. Also known as Access Control, OWASP regard it as a serious security risk today.
Authentication helps ensure that only authorized users can gain access to protected resources on the network level. Limited access may include networks, ports, hosts, and other services.

### What is Authorization?

Authorization, not to be confused with Authentication, occurs after a system has successfully verified the identity of an entity. The system will then allow access to resources such as information, files, databases, or specific operations and capabilities. After a system authenticates a user, authorization verifies access to the required resources. It is the process of determining whether an authenticated user can access a particular resource or perform a specific action.
For example, after a file server authenticates a user, it can check which files or directories that can be read, written, or deleted. This is where authorization comes into play.

## Implementation
I have created a web service where you can register, log in using 2FA, and use the encryption/decryption services by sending requests to endpoints.

The server runs on `http://127.0.0.1:5000`

### TOTP Authentication (2FA)

For authentication, TOTP is used.

One-time password (OTP) systems provide a mechanism for logging on to a network or service using a unique password that can only be used once, as the name suggests.

TOTP stands for Time-based One-Time Passwords and is a common form of two factor authentication (2FA). Unique numeric passwords are generated with a standardized algorithm that uses the current time as an input. The time-based passwords are available offline and provide user friendly, increased account security when used as a second factor.

When registering, the user has to provide an email and a password, then a link with the QR code will be sent back. It has to be scanned using Google Authenticator.

#### /register

Request

```json
    {"email": "user1@gmail.com", "password": "11111111"}
```

Response

```
Access the link to get the Qr Code. Scan it using Google Authenticator:
https://chart.googleapis.com/chart?cht=qr&chs=500x500&chl=otpauth://totp/Laboratory%20Work%20Nr.5:user1%40gmail.com?secret=MEEQ2R6V4S7HL5PDEO2SGWUTDCWZ4DBZ&issuer=Laboratory%20Work%20Nr.5
```

An OTP will be generated in the Google Authenticator app, and it will be used for logging in.

#### Code snippets (register endpoint)
```python
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
               "with this email already.
```

With `pyotp` library, a secret string is assigned to the user. After that, `TOTP` is used and create a specific URL for the QR code.

```python
secret_string = pyotp.random_base32()
```

```python
totp = pyotp.TOTP(secret_string)
```

```python
qr_uri = "https://chart.googleapis.com/chart?cht=qr&chs=500x500&chl=" + totp_uri
```

When logging in, the user provides email, password, and the otp generated in Google Authenticator. The server checks if the data is correct, and sends a success message with a token that has to be used when sending requests to service endpoints.

#### Code snippets (login endpoint)
```python
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
        alphabet = string.ascii_letters + string.punctuation
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
```

The server checks if the email, password and otp are correct, then logs the user in, by adding in a in-memory database, in this case a dictionary, the email and a random token, which will be used when sending requests.

#### Code snippets (caesar cipher endpoint)

```python
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
```

#### Other endpoints:

#### /caesarpermutation

```python
{"token": "Qr[*?Bdi", "message": "university", "key": "utm", "shift": "5"}
```

#### /vignere

#### /playfair

```python
{"token": "Qr[*?Bdi", "message": "university", "key": "utm"}
```

### Authorization (RBAC)

By default, there can be not enough rights for some services, because a role `user` is given when registering. In this case the `admin` role is required.

#### /stream

Request

```python
{"token": "Qr[*?Bdi", "message": "university", "key": "utm"}
```

Response

```
You don't have enough access rights.
```

To get the admin role, an admin account has to be created. It can be done by accessing `/admin` endpoint and registering using `4#17QZksEGi2` password.

#### /admin

Request

```json
    {"email": "admin@gmail.com", "password": "11111111", "secret": "4#17QZksEGi2"}
```

Response

```
Access the link to get the Qr Code. Scan it using Google Authenticator:
https://chart.googleapis.com/chart?cht=qr&chs=500x500&chl=otpauth://totp/Laboratory%20Work%20Nr.5:admin%40gmail.com?secret=J7UWQBYLGII3A4A53VGSZN5QWAOUPKNR&issuer=Laboratory%20Work%20Nr.5
```

#### /stream

Request

```python
{"token": "#LRSxEJL", "message": "university", "key": "utm"}
```

Response

```
The original message: UNIVERSITY, The encrypted message: 11000101010000011100010100110100010011111001010000111000111001011011011111011010, The decrypted message: UNIVERSITY
```

#### Other endpoints that need admin role

#### /asymmetric

### /hashing

```
{"token": "#LRSxEJL", "message": "university"}
```

### Database

Creates initial database resources using `sqlite`, the `Users` table.

```python
def create_initial_db_resources():
    cur.execute(
        "CREATE TABLE IF NOT EXISTS Users(email varchar unique, password varchar, user_type varchar, totp varchar)")
    cur.execute("SELECT * FROM Users")
    print(cur.fetchall())
```

Creates the user.

```python
def create_user(email, password, user_type, totp):
    cur.execute("INSERT INTO Users(email, password, user_type, totp) values(:email, :password, :user_type, :totp)", {
        'email': email,
        'password': password,
        'user_type': user_type,
        'totp': totp
    })
    print("Created user successfully")
    con.commit()
```

Gets the user by email.

```python
def get_user(email):
    try:
        cur.execute("SELECT email, password, user_type, totp FROM Users WHERE email = :email", {
            'email': email
        })
        print("User found successfully")
        return cur.fetchall()
    except Exception as e:
        print("Exception occurred while checking for the user")
        raise e
```

## Implementations
1. [Main Server](https://github.com/eugencic/utm-cs/blob/main/main.py)
2. [Database](https://github.com/eugencic/utm-cs/blob/main/Code/Database.py)
