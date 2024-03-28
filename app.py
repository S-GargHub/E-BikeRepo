from flask import Flask, render_template, request, redirect, url_for
import boto3
from botocore.exceptions import ClientError
import hmac
import hashlib
import base64


app = Flask(__name__)

# Define your Amazon Cognito user pool settings
USER_POOL_ID = 'us-west-2_rlhygUorX'
CLIENT_ID = '3f8348it1q6ger71441ejre9nl'
REGION = 'us-west-2'
CLIENT_SECRET = '19c024sum9hp7tja539vm5n16ttmgbbjts2t0j5mrg51ec4j7q7t'

def calculate_secret_hash(client_id, client_secret, username):
    message = username + client_id
    dig = hmac.new(str(client_secret).encode('utf-8'), 
                   msg = str(message).encode('utf-8'), 
                   digestmod = hashlib.sha256).digest()
    secret_hash = base64.b64encode(dig).decode()
    return secret_hash
    
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    
    # Authenticate user with Amazon Cognito
    try:
        client = boto3.client('cognito-idp', region_name=REGION)
        response = client.initiate_auth(
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': username,
                'PASSWORD': password,
                'SECRET_HASH': calculate_secret_hash(CLIENT_ID, CLIENT_SECRET, username)
            },
            ClientId=CLIENT_ID
        )
        # Authentication successful, redirect to dashboard
        return redirect(url_for('dashboard'))
    except ClientError as e:
        # Authentication failed, display error message
        error_message = e.response['Error']['Message']
        return render_template('login.html', error=error_message)

@app.route('/index')
def dashboard():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
