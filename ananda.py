# Importacao das libs
import time
import os

from selenium import webdriver
from selenium.webdriver.common.keys import keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

# Instanciate the chatbot
chatbot = ChatBot('Ananda')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.portuguese')
trainerer = ListTrainer(chatbot)

# Set the main path into a variable
dir_path = os.getcwd()

# Start the application
driver = webdriver.Chrome(dir_path + 'chromedriver.exe')
driver.get('https://web.whatsapp.com/')
driver.implicity_wait(15)

# Basic communication functions
def getTalk():
	try:
		post = driver.find_elements_by_class_name("_12pGw")
		last = len(post) - 1
		text = post[last].find_elements_by_css_selector("span.selectable-text").text
		return text
	except:
		pass

def sendMessage(message):
	textbox = driver.find_elements_by_class_name("_3u328")
	value = "*Ananda:* " + str(mensagem)

	for part in value.split("\n"):
		textbox.send_keys(part)
		ActionChains(driver).key_down(keys.SHIFT).key_down(keys.ENTER).key_up(keys.SHIFT).perform()

	time.sleep(0.5)
	sendButton = driver.find_elements_by_class_name("_3M-N-")
	sendButton.click()

def train(message):
	response = 'Como respondo isso? Me ensina por favor? Utilize ; "' + str(mensagem) + '"'
	sendMessage(response)
	new = []
	try:
		while True:
			last = getTalk()
			if last == "!":
				sendMessage("Você desativou meu aprendizado.")
				break
			elif last.replace(';', '') != '' and last != message and last[0] == ';':
				aux = last
				print(message.lower().strip())
				print(last.replace(';', '').lower().strip())
				new.append(message.lower().strip())
				new.append(last.replace(';', '').lower().strip())
				trainerer.train(novo)
				sendMessage("Pronto, aprendi! Obrigada...")
				break
	except:
		pass

# WIKIPEDIA
import wikipedia
wikipedia.set_lang('pt')

def wiki():
	try:
		search = str(getTalk().lower().strip()[2:])
		message = '{}'.format(wikipedia.summary(search))
		sendMessage(message)
	except:
		sendMessage("Nada encontrado para {} na Wikipedia Brasil.".format(search))