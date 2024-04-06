import google.generativeai as genai

genai.configure(api_key='AIzaSyDVARQqzmu_ozJUDoQkJCBQn-xMspoz40I')

model = genai.GenerativeModel('gemini-pro')

chat = model.start_chat()

while True:
    message = input("what you wanna say/ask : ")
    response= chat.send_message(message)

    print("gemini : " + response.text)