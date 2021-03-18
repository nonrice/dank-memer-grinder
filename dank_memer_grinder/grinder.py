from http.client import HTTPSConnection
from sys import stderr
from json import dumps
from time import sleep
from datetime import datetime
from random import random

file = open("info.txt")
text = file.read().splitlines()

if len(text) != 4 or input("Configure bot? (y/n)") == "y":
    if len(text) != 4:
        print("An error was found inside the info file (possibly your first time using?), reconfiguring is required.")
    print("Refer to Google if some of these parameters are unfamiliar.")
    file.close()
    file = open("info.txt", "w")
    text = []
    text.append(input("User agent: "))
    text.append(input("Discord token: "))
    text.append(input("Discord channel URL: "))
    text.append(input("Discord channel ID: "))

    for parameter in text:
        file.write(parameter + "\n")

    file.close()

header_data = {
    "content-type": "application/json",
    "user-agent": text[0],
    "authorization": text[1],
    "host": "discordapp.com",
    "referrer": text[2]
}

print("Messages will be sent to " + header_data["referrer"] + ".")

def connect():
    return HTTPSConnection("discordapp.com", 443)

def send_message(conn, channel_id, message):
    message_data = {
        "content": message,
        "tts": False
    }

    try:
        conn.request("POST", f"/api/v6/channels/{channel_id}/messages", dumps(message_data), header_data)
        resp = conn.getresponse()
        if 199 < resp.status < 300:
            pass
        else:
            stderr.write(f"While sending message, received HTTP {resp.status}: {resp.reason}\n")
            pass
    except:
        stderr.write("Failed to send_message\n")

def get_embed(conn, channel_id):

    channel = conn.request("GET", f"/api/v6/channels/{channel_id}/messages", headers=header_data)
    resp = conn.getresponse()

    if 199 < resp.status < 300:
        resp_string = str(resp.read(600))

        return resp_string

    else:
        stderr.write(f"While checking message, received HTTP {resp.status}: {resp.reason}\n")
        pass

def copy_text():
    response = get_embed(connect(), text[3])
    response = response.replace("\\ufeff", "")
    response = response.replace("\\", "")
    front_back_tick = -1
    end_back_tick = -1
    for i in range(0, len(response)):
        if response[i] == "`" and front_back_tick == -1:
            front_back_tick = i
        elif response[i] == "`" and front_back_tick != -1:
            end_back_tick = i
            break

    if front_back_tick != -1 and end_back_tick != -1:
        send_message(connect(), text[3], response[front_back_tick + 1:end_back_tick])
        print("Activated text copy " + (datetime.now()).strftime("%H:%M:%S"))

def cycle(period):
    send_message(connect(), text[3], "pls fish")
    sleep(3)
    copy_text()
    sleep(period)
    sleep(random() * 7)

    send_message(connect(), text[3], "pls hunt")
    sleep(3)
    copy_text()
    sleep(period)
    sleep(random() * 7)

    send_message(connect(), text[3], "pls beg")
    sleep(3)
    copy_text()
    sleep(period)
    sleep(random() * 7)

def main():
    period = int(input("Seconds between each command (minimum 15): "))
    if period < 15:
        print("Error: please provide a valid period that is 15 seconds or more.")
        return

    print("Grinding the bot... " + (datetime.now()).strftime("%H:%M:%S"))
    while True:
        cycle(period)

main()


