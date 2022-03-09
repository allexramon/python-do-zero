print('audio.formatos.mp3:',__name__)

def converter(arquivo):
    """
    meuvideo.mp4 ==> meuvideo.mp3
    """
    #"meuvideo.mp4".split('.')
    #['meuvideo', 'mp4'][0]
    # 'meuvideo' + '.mp3'
    print(arquivo.split('.')[0] + '.mp3')
    print('Olá!')