import re
import time 
import sys
import cv2 as cv
import pyttsx3 as tts
from voice import input_voice 
import speech_recognition as sr
from serial import Serial,SerialException
import threading


tts_model = tts.init()
sr_model = sr.Recognizer()
# <------------ PORT -----------> 
arduino_port = '/dev/ttyACM0'
arduino = None

try:
    arduino = Serial(arduino_port,9600)
    time.sleep(2) 
    print("arduino: conneted :) successfully ")
except:
    print(" <- Error: while conneting arduino -> ")
    sys.exit(1) 


tts_model.setProperty('rate', 150)
voice_input_result = None
string_output = ""
num = -1


def speak(text):
    tts_model.say(text)
    tts_model.runAndWait()

def announceTemperature(text):
    number = re.findall(r'\d+', text)
    if number:
        print("Temperature detected:", number[0])
        announce_text = "Your temperature is set to " + str(number[0])
        tts_model.say(announce_text)
        tts_model.runAndWait()
        return int(number[0])
    return 10

def get_voice_input():
    global voice_input_result
    voice_input_result = input_voice()

# Load the Haar Cascade classifier
harCascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

# Video capture
cap = cv.VideoCapture(0)
voice_thread = None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    rgb_image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    gray_image = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = harCascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=6, minSize=(100, 100))

    for x, y, w, h in faces:
        cv.rectangle(rgb_image, (x, y), (x + w, y + h), (255, 0, 0), 5, cv.LINE_AA)

    number_of_people = len(faces)
    rgb_image = cv.flip(rgb_image, 1)
    cv.putText(rgb_image, str(number_of_people), (100, 100), cv.FONT_HERSHEY_COMPLEX, 3, (255, 0, 0), 5)
    

    # --------------------- Number Of People Is Greater Than 2 ---------------------
    if number_of_people >= 2:
        if string_output!="AC ON":
            string_output = "AC ON"
            arduino.write("OPEN\n".encode())
            cv.putText(rgb_image, string_output, (300, 100), cv.FONT_HERSHEY_COMPLEX, 3, (255, 0, 0), 5)
    elif number_of_people<2:
        string_output=""
        arduino.write("CLOSE\n".encode())

    # Check for voice input result
    if voice_input_result:
        num = announceTemperature(voice_input_result) 
        voice_input_result=None
    if(num>30):
        if string_output != "AC ON":
            string_output = "AC ON"
            arduino.write("OPEN\n".encode())
            cv.putText(rgb_image, string_output, (100, 200), cv.FONT_HERSHEY_COMPLEX, 3, (255, 0, 0), 5)
    elif num<30:
        string_output = ""
        arduino.write("CLOSE\n".encode())
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    
    
    cv.imshow("People Count Window", rgb_image)

    key = cv.waitKey(1) & 0xFF

    if key == ord('g'):
        # Start a new thread for voice input if not already running
        if voice_thread is None or not voice_thread.is_alive():
            voice_thread = threading.Thread(target=get_voice_input)
            voice_thread.start()

    if key == ord('q'):
        print("<-..End..->")
        break

cv.destroyAllWindows()
cap.release()



'''ino
include<Servo.h>
int servoPin = 8;
Servo myservo;

void setup() {
  Serial.begin(9600);
  myservo.attach(servoPin);
  myservo.write(10);
  delay(100);
}

void loop() {
  if(Serial.available()){
    String command = Serial.readStringUntil('\n');
    Serial.println(command);
      if(command.startsWith("OPEN")){
        myservo.write(180);
        delay(500);
      }
      if(command.startsWith("CLOSE")){
        myservo.write(10);
        delay(500);
      }
  }
}

'''

