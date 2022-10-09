
def forca1():
    lista_imagens_forca = [f'''
 _______
|       |
|
|
|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
|
>>> Palavra: ''', 
'''
 _______
|       |O
|       
|       
|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
|
>>> Palavra: ''',
'''
 _______
|       |O
|        T
|       
|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
|
>>> Palavra: ''',
'''
 _______
|       |O
|        T
|       /
|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾    
|
>>> Palavra: ''',
'''
 _______
|       |O
|        T
|       / \ 
|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾        
|
>>> Palavra: ''',
'''
 _______
|       |O
|       /T 
|       / \ 
|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾       
|
>>> Palavra: ''', 
'''
 _______
|       |
|       O
|      /T\ 
|‾‾‾‾\ / \ /‾‾‾‾‾‾‾
|    /     \ 
>>> Palavra: '''
]
    lista_imagens_forca.reverse()
    return lista_imagens_forca

if __name__ == '__main__':
    forca1()
