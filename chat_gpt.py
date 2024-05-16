import openai
import textwrap

openai.api_key = 'INSERT YOUR KEY HERE'

def format_text(prompt):
    with open('output/transcricao.txt', 'r') as infile:
        text = infile.read()

        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            temperature=0.5,
            messages=[
                {
                    "role": "system",
                    "content": prompt
                },
                {
                    "role": "user",
                    "content": text,
                }
            ],
        )
        print("Retorno do chatgpt")
        print(response)
        textResponse = response.choices[0].message.content
        print(textResponse)
        
        print("Formatação concluída")
        with open('./output/formatted.txt', 'w') as file:
            file.write(textResponse)

        print("Transcrição salva com sucesso!")
