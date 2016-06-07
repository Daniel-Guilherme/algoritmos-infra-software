cont = 0
references = []
hit = []
miss = []
frames = []

ref = input("Digite a quantidade de referencias: ")

for i in range (0,ref):
    dado = input("Digite o valor desejado: ")
    references.append(dado)
#references = [7, 0, 1, 2...]

n = input("Digite o tamanho da frame de memoria: ")

for j in range (0,ref):
    if (references[j] in frames):
        print("Hit")
        hit.append(j)
        
    else:
        print("Miss")
        #se a lista de frames estiver com espaço vazio entra no if
        if(len(frames)!=n):
            frames.append(references[j])
            miss.append(references[j])
		
        #n eh tamanho do frame de memoria
        #j eh o ponteiro que está realizando a leitura do vetor references
        #pont eh o ponteiro que ira percorrer references da presente posição ate o inicio

        
        #lista frames não possui espaços vazios
        else:        
            pont = j-1
            framestemp=[]
            while(len(framestemp)<n):
                if((references[pont] in framestemp) == False): ##testa se o valor anterior ao j não está na lista framestemp
                    framestemp.append(references[pont])
                pont-=1
			
            num = frames.index(framestemp[-1]) #armazena em num o valor do indice na lista do valor a ser retirado, que se encontra na ultima posicao da lista temporaria
            del frames[num] #apaga o valor que é pra sair da lista para não aumentar o tamanho da lista
            frames.insert(num,references[j]) #insere o novo valor na lista na posição em que estava o antigo 
            del framestemp #deleta a lista temporaria
            
			
    print frames
    
    
print hit
print len(hit)
print miss
print len(miss)
