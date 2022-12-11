# Web Authentication & Authorisation.

## Theory

### What is Authentication?

Often confused with Authorization, Authentication is essentially verifying the true identity of an entity. It enables access control by proving that a user’s credentials match those in an authorized user’s database. Identity verification can ensure system security, process security, and corporate information security. Also known as Access Control, OWASP regard it as a serious security risk today.
Authentication helps ensure that only authorized users can gain access to protected resources on the network level. Limited access may include networks, ports, hosts, and other services.

### What is Authorization?

Authorization, not to be confused with Authentication, occurs after a system has successfully verified the identity of an entity. The system will then allow access to resources such as information, files, databases, or specific operations and capabilities. After a system authenticates a user, authorization verifies access to the required resources. It is the process of determining whether an authenticated user can access a particular resource or perform a specific action.
For example, after a file server authenticates a user, it can check which files or directories that can be read, written, or deleted. This is where authorization comes into play.

## Implementation
I have made a web service where you can create an account, log in using MFA, and use the provided services by sending requests to the server.

The server runs on `http://127.0.0.1:5000`

### TOTP Authentication (2FA)

For authentication, I have used TOTP.

One-time password (OTP) systems provide a mechanism for logging on to a network or service using a unique password that can only be used once, as the name suggests.

In my case, when registering, the user provides an email and a password, and a link with the QR code is sent back.

![alt text](https://github.com/eugencic/utm-cs-labs/blob/main/Screenshots/1.png)

The link provides a QR code which has to be scanned using Google Authenticator.

![alt text](https://github.com/eugencic/utm-cs-labs/blob/main/Screenshots/2.png)

After the code is scanned, an OTP will be generated in the Google Authenticator app, and it will be used for logging in.

![alt text](https://github.com/eugencic/utm-cs-labs/blob/main/Screenshots/3.jpg)

#### Code snippets (register endpoint)
```
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

Using `pyotp` library, a secret string is assigned to the user. After that, we use `TOTP` and create a specific URL for the QR code.

```secret_string = pyotp.random_base32()```

```totp = pyotp.TOTP(secret_string)```

```qr_uri = "https://chart.googleapis.com/chart?cht=qr&chs=500x500&chl=" + totp_uri```

When logging in, the user provides the email, the password, and the otp generated in Google Authenticator. The server checks if the data is correct, and sends a login success message and a token that has to be used when sending requests for using the services.

![alt text](https://github.com/eugencic/utm-cs-labs/blob/main/Screenshots/4.png)

#### Code snippets (login endpoint)
```
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

The server checks if the email, password and otp are correct, then logs the user in, by adding in an in-memory database, in this case a dictionary, the email and a random token, that will be used when sending requests. This will simulate a log in session. If the server goes down, the data from the dictionary will be deleted, by that the login session will be closed and the user will have to log in again.

After that, the user can use the services. In this case, these are the ciphers implemented in previous laboratory works.

#### Code snippets (caesar cipher service endpoint)

```
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

The server checks if the login token is correct, then returns the result.

![alt text](https://github.com/eugencic/utm-cs-labs/blob/main/Screenshots/5.png)

#### Other endpoints:

`/caesarpermutation`

```{"token": "Qr[*?Bdi", "message": "university", "key": "utm", "shift": "5"}```

`/vignere`

```{"token": "Qr[*?Bdi", "message": "university", "key": "utm"}```

`/playfair`

```{"token": "Qr[*?Bdi", "message": "university", "key": "utm"}```

### Authorization (RBAC)

For some services you don't have enough rights by default. It is because a default role user is given when registering. To use some services you need the admin role.

`/stream`

```{"token": "Qr[*?Bdi", "message": "university", "key": "utm"}```

```You don't have enough access rights.```

To get the admin role you need to create an admin account. It can be done by accessing the `/admin` endpoint and registering using the `4#17QZksEGi2` password.

![alt text](https://github.com/eugencic/utm-cs-labs/blob/main/Screenshots/4.png)

The role is assigned to the user when creating the account. It can be either user or admin.

```{"token": "#LRSxEJL", "message": "university", "key": "utm"}```

```The original message: UNIVERSITY, The encrypted message: 11000101010000011100010100110100010011111001010000111000111001011011011111011010, The decrypted message: UNIVERSITY```

#### Other endpoints that need the admin role:

`/asymmetric`

```{"token": "#LRSxEJL", "message": "university"}```

`/hashing`

```{"token": "#LRSxEJL", "message": "university"}```

### Database

Create initial database resources using sqlite.

```
def create_initial_db_resources():
    cur.execute(
        "CREATE TABLE IF NOT EXISTS Users(email varchar unique, password varchar, user_type varchar, totp varchar)")
    cur.execute("SELECT * FROM Users")
    print(cur.fetchall())
```

Creates the `Users` table.

```
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

Creates the user.

```
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

Gets the user by email.

## Implementations
1. [Main Server](https://github.com/eugencic/utm-cs-labs/blob/main/main.py)
2. [Database](https://github.com/eugencic/utm-cs-labs/blob/main/Code/Database.py)