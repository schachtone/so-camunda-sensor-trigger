import datetime

from controller.motorController import MotorController

from flask import request

TEMPLATE = {
        "result": "unknown command given"
}


motorController = MotorController();

def motor_handle_input():
    body = request.json

    print(body.get("id"))

    if body.get("action") == "start":
        TEMPLATE["result"] = "starting"

    elif body.get("action") == "stop":
        TEMPLATE["result"] = "stopping"

    TEMPLATE["timestamp"] = str(datetime.datetime.now())

    return TEMPLATE

