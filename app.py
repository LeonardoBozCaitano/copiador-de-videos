import video_to_text
import chat_gpt

video_file = "./input/video.mp4"

chatGpt_Prompt = "Você vai receber uma transcrição de uma conversa importante, você vai formatar o texto recebido completo, sem deixar nada de fora, corrigindo possiveis erros de escrita e identificando as pessoas que falaram. Você não pode inventar informações que não estão claramente descritas no texto."

def main(): 
    print("Iniciando processamento do video.")
    video_to_text.convert_video(video_file)
    #chat_gpt.format_text(chatGpt_Prompt)

main();