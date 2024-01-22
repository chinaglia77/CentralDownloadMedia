from pytube import YouTube
import os

def baixar_video():
    try:
        url_video = input("Insira a URL do vídeo do YouTube: ")
        video = YouTube(url_video)
        stream = video.streams.get_highest_resolution()
        caminho_destino = os.path.join(os.path.expanduser("~"), 'Desktop')
        caminho_completo = os.path.join(caminho_destino, f"{video.title}.mp4")
        stream.download(output_path=caminho_destino)
        print(f"O vídeo foi baixado com sucesso em: {caminho_completo}")
    except Exception as e:
        print("Por favor inserir uma URL valida !, tente novamente...")

def baixar_audio():
    try:
        url_video = input("Insira a URL do vídeo do YouTube: ")
        video = YouTube(url_video)
        stream = video.streams.filter(only_audio=True, file_extension='mp4').first()
        caminho_destino = os.path.join(os.path.expanduser("~"), 'Desktop')
        caminho_completo = os.path.join(caminho_destino, f"{video.title}.mp3")
        stream.download(output_path=caminho_destino)
        os.rename(os.path.join(caminho_destino, f"{video.title}.mp4"), caminho_completo)
        print(f"O áudio foi baixado com sucesso em: {caminho_completo}")
    except Exception as e:
        print("Por favor inserir uma URL valida !, tente novamente...")

opWhile = 1  # Inicializando opWhile para entrar no loop

while opWhile == 1:
    try:
        print("-----OPÇÕES DOWNLOAD-----")
        print("Escolha o tipo de download:")
        print("1 - Baixar como MP4")
        print("2 - Baixar como MP3")

        opcao = input("Digite o número correspondente à sua escolha: ")

        if opcao not in ['1', '2']:
            print("Por favor, digite os valores corretamente")
        else:
            if opcao == '1':
                print("Você selecionou MP4")
                baixar_video()
            elif opcao == '2':
                print("Você selecionou MP3")
                baixar_audio()
    except ValueError:
        print("Oops, por favor, digite um valor correto")
    
    try:
        opWhile = int(input("Você deseja continuar (1) ou Sair (2): "))
    except ValueError:
        print("Oops, por favor, digite um valor correto")

print("Fechando programa...")
