#import  audio.formatos.mp3 as mp3
#from audio.formatos import mp3
#mp3.converter('teste_conversao.mp4')
print('app:',__name__)

if __name__ == '__main__':
    import audio.formatos.mp3 as mp3
    mp3.converter('gatinhos_sorridentes.mp4')