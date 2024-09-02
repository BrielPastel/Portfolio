import socket
import MyHashLib as HL
import time


ALICE = HL.CHARLES if HL.ativar_MiTM else HL.ALICE

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def fase1_Autenticacao():
    global senha, senha_salgada

    login = input('digite seu LOGIN: ')
    senha = input('digite sua SENHA: ')

#------------------------------------------------------------------------------------------------------------
# 1) BOB ENVIA UM HELLO PARA ALICE
# -- não precisa modificar essa seção.

    msg = HL.formataMensagem(['HELLO', login])
    s.sendto( msg, ALICE )  

#------------------------------------------------------------------------------------------------------------
# 2) BOB RECEBE UM CHALLENGE    
# -- não precisa modificar essa seção.
    try:
        data, addr = s.recvfrom(1024) 
    except:
        print('Alice não está sendo executada: aguardando 10 segundos ...')
        time.sleep(10)
        return False

    print('RECEBI: ', data)

    msg = HL.separaMensagem(data) 
    if len(msg) < 2 or msg[0] != "CHALLENGE": 
        print('recebi uma mensagem inválida')
        return False

    cs_ALICE = msg[1]
    salt = msg[2]

#------------------------------------------------------------------------------------------------------------
# 3) BOB responde ao CHALLENGE com um novo CHALLENGE e o HASH da sua senha 
# -- calcule a senha salgada usando o SALT recebido 
# -- troque string NONCE por um nonce em formato base64 convertido para string (decode) 
# -- troque o prova_para_ALICE pelo HASH da senha_salgada com o challenge da ALICE (cs_ALICE)

    _, senha_salgada = HL.calculaHASH(senha + salt)
    cs_BOB = 'NONCE' # TODO: modifique essa linha
    prova_para_ALICE = senha_salgada # TODO: modifique essa linha 

    data = HL.formataMensagem(['CHALLENGE_RESPONSE', cs_BOB, prova_para_ALICE ]) 

    s.sendto(data, addr )

#------------------------------------------------------------------------------------------------------------
# 4) BOB recebe o resultado da autenticaçao e a prova enviada por ALICE
# -- não precisa modificar essa seção.

    data, addr = s.recvfrom(1024)
    print('RECEBI: ', data)
    msg = HL.separaMensagem(data) 
    resultado = msg[0]
    prova_da_alice = msg[1]


#------------------------------------------------------------------------------------------------------------
# 5) BOB se a senha está correta
# -- é preciso substituir o local_hash pelo hash da senha pelo challenge enviado por BOB (cs_BOB)
    local_hash = senha_salgada # TODO: modifique essa linha
    print(f'BOB compara local_hash={local_hash} e prova_da_Alice={prova_da_alice}')
    if resultado == 'SUCCESS' and local_hash == prova_da_alice:
        print('Este servidor é ALICE')
        return True
    else:
        print('Este servidor não é ALICE')
        return False

def fase2_MensagensAssinadas():
    #------------------------------------------------------------------------------------------------------------    
    # 6) BOB recebe uma mensagem autenticada de ALICE

        print('Aguardando mensagens do Servidor')

        while True:
            data, addr = s.recvfrom(1024)
            print('RECEBI: ', data)

            msg = HL.separaMensagem(data) 
            if msg[0] == 'HMAC':
                resultado = HL.verificaMensagem(data, senha_salgada) 
                if resultado: 
                    print('Mensagem válida')
                else:
                    print('Mensagem inválida')
        
if __name__ == "__main__":

    while True:
        if fase1_Autenticacao():
            fase2_MensagensAssinadas()

