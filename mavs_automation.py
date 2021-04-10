import time
import speech_recognition as sr
import pyaudio
from selenium import webdriver


#check the status of the mavericks game

## take input argument (perhaps a speech intake)

r = sr.Recognizer()
mic = sr.Microphoe()

with mic as source:
	audio = r.listen(source)
	
r.recognize_google(audio)

## give commands without running script?

def get_inquiry():
	inq = ''
	while True:
		inq = input('What\'s your mavs question? (score, standings, injuries: ') 
		if inq == 'score' or 'standings' or 'injuries':
			return inq

		else:
			print("Input not valid! Please type score, standings or injuries")
			continue

inquiry = get_inquiry()

driver = webdriver.Chrome('/Users/dasay/website_login/chromedriver')
driver.get('http://www.google.com/');
time.sleep(1)
search_box = driver.find_element_by_name('q')
search_box.send_keys("mavs ",inquiry)
search_box.submit()















