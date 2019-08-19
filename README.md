# messageapi Django
*Requires Python 3 and pip3*
___

# Getting started
### 1. Cloning
```
git clone https://github.com/garywaller246/messageapi.git
```


### 2. Installing
Start by setting up a virtual environment to install the project’s dependencies in a clean manner.

```
cd messageapi
python3 virtualenv env 
```

Activate your virtual env:
```
source env/bin/activate
```

Install the project's requirements:
```
pip3 install -r requirements.txt
```


### 3. Migrations
The migration files are kept outside of source control. You will need to generate them:
```
./manage.py makemigrations
```

Then apply the migrations:
```
./manage.py migrate
```


### 4. Running the server
Once you run the server, it will auto reload at every change.
```
./manage.py runserver
```

This will run the server at:
```
http://127.0.0.1:8000/
```


### 5. Admin
You'll need an admin user (super user), it's just a command away:
```
./manage.py createsuperuser
```

The admin is available at:
```
http://127.0.0.1:8000/admin
```


# API Endpoints

## Auth Tokens
### Getting an auth token
`POST`
`/auth-token/`

##### Body & Headers
Body:
```json
{
  "username": "username",
  "password": "password"
}
```

##### Response
```json
{
  "token": "<auth_token>"
}
```
___

## Messages

### Creating message
`POST`
`/message/create/<int:receiver_pk>`

##### Body & Headers
Body:
```json
{
    "content": "message content",
    "subject": "message subject"
}
```

##### Response
```json
{
    "content": "message content",
    "subject": "message subject"
}
```
___

### Retrieving messages
`GET`
`/message/`

##### Response
```json
[
    {
        "id": "message_pk",
        "sender": "username",
        "receiver": "username",
        "subject": "message content",
        "content": "message subject",
        "timestamp": "2019-08-19T10:25:39.537840Z",
        "read": false
    },
    {
        "id": "message_pk",
        "sender": "username",
        "receiver": "username",
        "subject": "message content",
        "content": "message subject",
        "timestamp": "2019-08-19T10:29:00.050255Z",
        "read": true
    }
]
```
___
### Retrieving specific message
`GET`
`/message/<int:message_pk>`

If a message is accessed by the receiver and is currently in ```'read' : false``` by accessing the message it will be marked to ```true```.

##### Response
```json
{
  "id": "message_pk",
  "sender": "username",
  "receiver": "username",
  "subject": "message content",
  "content": "message subject",
  "timestamp": "2019-08-19T10:25:39.537840Z",
  "read": false
}
```
___

## Delete specific message
`DELETE`
`/message/delete/<int:message_pk>`

If a message is accessed by the receiver and is currently in ```'read' : false``` by accessing the message it will be marked to ```true```.

##### Response
```json
{
  "id": "message_pk",
  "sender": "username",
  "receiver": "username",
  "subject": "message content",
  "content": "message subject",
  "timestamp": "2019-08-19T10:25:39.537840Z",
  "read": false
}
```
___
