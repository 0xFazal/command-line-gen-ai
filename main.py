from dotenv import load_dotenv
load_dotenv()

import os
import google.generativeai as genai
import getpass
import sys

user = getpass.getuser()

initial_prompt = f"You are configured to run on command line terminal, mostly for software development tasks. Don't use markdown syntax as it looks ugly in terminal. Use special characters like asterisk, at the rate, dollar, curly braces to decorate the response for appropriately rendering in terminal. Your initial response to this prompt should be 'Hello, {user}! How can I help?'."

def initialize_model():
    gemini_api_key=os.getenv('GEMINI_API_KEY')
    genai.configure(api_key=gemini_api_key)
    return genai.GenerativeModel('gemini-pro')

def print_response(response):
	print("***"*50)
	print('Response: ')
	print('')
	for chunk in response:
		print(chunk.text)
		
	print("***"*50)
        
def main():

	try: 
		temp = float(sys.argv[1])
	except IndexError:
		temp = 0.9
		
	model_gemini_pro = initialize_model()
	
	try:
		conversation = model_gemini_pro.start_chat(history=[])
		response = conversation.send_message(initial_prompt, stream=True, safety_settings={'HARASSMENT': 'block_none'})
	except Exception:
		print('Invalid Gemini API Key or missing key in .env file')
		sys.exit()
	
	print_response(response)
	while True:
		user_input = input('Prompt(type exit to quit): ')
		if user_input.lower() == 'exit':
			break
		response = conversation.send_message(user_input, stream=True, generation_config={'temperature': temp})
		print_response(response)

main()