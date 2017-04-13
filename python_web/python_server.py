from flask import Flask, jsonify
import time
import commands
import pylirc, time
import urllib2
import socket
import re


app = Flask(__name__)

CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.',
        }

DOT_LENGTH = 0.5  # seconds value for dot '.'


@app.route("/led/api/v1.0/morse/<string:message>", methods=['GET'])
def morse(message):
    """Return a JSON Object of the message converted to Morse Code"""
    morse_code = ""
    message = parse_message(message)
    for char in message:
        toggle_led(False)
        #time.sleep(DOT_LENGTH * 3)  # pause between characters
        if char == ' ':
            morse_code += char
            #time.sleep(DOT_LENGTH * 7)  # pause between words
        else:
            for code in CODE[char.upper()]:
                morse_code += code
                #time.sleep(DOT_LENGTH)  # pause between code elements
                if code == '.':
                    toggle_led(True)
                    #time.sleep(DOT_LENGTH)  # pause between dots
                else:
                    toggle_led(True)
                    #time.sleep(DOT_LENGTH * 3)  # pause between dashes
                toggle_led(False)
        morse_code += ' '
    if morse_code == "":
        morse_code = "error"

    return jsonify({'code': morse_code})


@app.route("/rasp/led/<string:message>", methods=['GET'])
def setled(message):
    """Return a JSON Object of the message converted to Morse Code"""
    result = led(message)
    return jsonify({'code': result})

@app.route("/rasp/digital/<string:message>", methods=['GET'])
def setdigital(message):
    """Return a JSON Object of the message converted to Morse Code"""
    result = digitalint(int(message))
    return jsonify({'code': result})

@app.route("/rasp/action/<string:message>", methods=['GET'])
def setaction(message):
    """Return a JSON Object of the message converted to Morse Code"""
    result = raspsend("type=%s" % message);   
    return jsonify({'code': result})


def parse_message(message):
    """Return a message that can be converted to Morse Code. Otherwise
        return an empty String"""
    if "%20" in message:
        message = message.replace("%20", " ")
    for char in message:
        if char.upper() not in CODE.keys() and char != ' ':
            return ""
    return message


def toggle_led(is_on):
    """Toggles the LED connected to GPIO pin 18 on the Raspberry Pi"""
    print "out put gpio 18 %s" % is_on
    #GPIO.output(18, is_on)


def is_num(num):
    if re.match('^[0-9]+$',num):
        return True
    else:
        return False
def formatint(num):
    return ("%4d" % num).replace(' ','#')

def led(num):
    return raspsend("type=led&num="+num)    

def digital(num):    
    return raspsend("type=digital&num="+num)
    
def digitalint(num):
    num = formatint(num);
    return raspsend("type=digital&num="+num)    

def beep(num):
    return raspsend("type=beep&num="+num);   

def wendu():
    return raspsend("type=wendu");   

def raspsend(data): 
    address = ('127.0.0.1', 9999)  
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    s.connect(address)    
    s.send(data)  
    rdata = s.recv(512)  
    print 'the data received is',rdata    
    s.close()  
    return rdata

if __name__ == "__main__":
    app.run(host='0.0.0.0')
