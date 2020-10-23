import re
from PIL import Image 
import os, glob
caminho = "mini"
formato = ".pgm"

#criando uma pasta para armazenar a roi
dir = './ROI'    
file = os.makedirs(dir)
names_duplicados = []
#--------------------Função que calcula o quadrado-----------------------
def calcula_quadrado(name_pasta, name, j, y, r):#(x,y) é o ponto 
    
    names_duplicados.append(name)

    imagem = Image.open(name_pasta)
    x = 1024 - j

    le = int((y - r))
    up = int((x - r))
    ri = int( (y + r))
    lo = int((x + r))
   
    #cortar a imagem 
    (left, upper, right, lower) = (le, up, ri, lo)
    corte = imagem.crop((left, upper, right, lower))
    cont = 0
    for k in range(len(names_duplicados)):
        if(names_duplicados[k] == name):
            cont = cont+1
            #name = names_duplicados[l] + "i"
        #print(cont)
        if(cont>1):
            name = name + "(" + str(cont) + ")"  
        
    print(name)
        

    #Salva o corte na pasta
    corte.save( dir + "/" + name +".PNG")


#----------------------------Separando os dados das imagens-----------------------------------------
filename = "info.txt"

#abrindo o arquivo 
with open(filename) as fp:
    arquivo = fp.readlines()

#transformando o arquivo em uma string 
sequencia = ' '.join(arquivo)

#dividindo as informações de cada imagem
dados = re.split("\n", sequencia)

#tirar os espaços em branco do inicio e do fim
for i in range(len(dados)):
    dados[i] = re.split(" ", dados[i])
    
for i in range(len(dados)):
    for j in range(len(dados[i])-1):
            if(dados[i][j] == ''):
                dados[i].pop(j)#deleta
   
lista_coordenadas = [] #criando uma lista para as coordenadas

#Escrevendo as coordenadas, nome e o raio em um vetor 
for i in range((len(dados))):
    if((len(dados[i])-1) == 6):
        linha = []
        linha.append( dados[i][0])#nome
        linha.append( dados[i][4])#x
        linha.append( dados[i][5])#y
        linha.append( dados[i][6])#raio
        #insere as linha na lista de coordernadas     
        lista_coordenadas.append(linha)

lista_imagem = []

#pega todos os nomes de arquivo .pgm e o nome da pasta 
lista_imagem = glob.glob(os.path.join(caminho , '*pgm'))

#-----------------------Chama a função calcula_quadrado--------------------------

for f in lista_imagem:
    for p in lista_coordenadas:
        aux = (caminho +"\\"+ p[0] + formato)#inserindo o nome da pasta e o formato da imagem
        if(f == aux):
            #arruamar nomes iguais**
            #chama a função calcula_quadrado para realizar o corte das imagens
            calcula_quadrado(aux, p[0], int(p[2]), int(p[1]), int(p[3]))
            #calcula_quadrado(aux,p[0], int(p[1]), int(p[2]), int(p[3]))

    





