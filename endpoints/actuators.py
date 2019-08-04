import datetime

from flask import request

DUMMY = {
        "message": "blabla",
        "timestamp": datetime.datetime.now()
}


def motor_handle_input():
    body = request.json

    print(body.get("id"))

    return DUMMY

