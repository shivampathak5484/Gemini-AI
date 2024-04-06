import google.generativeai as genai

genai.configure(api_key='AIzaSyDVARQqzmu_ozJUDoQkJCBQn-xMspoz40I')

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("What is python?")

print(response.text)