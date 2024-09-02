import socket
import MyHashLib as HL


# Crie uma estratégia para que ALICE receba a autenticação de usuários pela rede.
# A solução deve ser imune a ataques de REPETIÇÃO (REPLAY)

#------------------------------------------------------------------------------------------------------------
# 0) ALICE tem uma base de senhas cadastradas
# -- Utilize o conceito de senha salgada para esconder as senhas dos usuários
# -- OBS. Suponha que o cadastro da senha foi feito anteriormente, pois ele não está neste código
# BOB = SEGREDO
# MOE = SENHA
# LARRY = OPA
# CURLY = YAHOO


# TODO: coloque as senhas salgadas no dicionário
senhas = {
    'BOB' : '4bb99ac369555debf405001df922f9e7',
    'MOE' : 'a2bbe857922500b6c6103e1f3bda9895',
    'LARRY' : '94e9ed6ecbd577addc67078800abf540',
    'CURLY' : '60abe267ddf5074bab63c33773e89ec1'
}

# TODO: coloque os salts nesse dicionário
salts = { 
    'BOB' : b'/Mn9pcVH3mlxH5duomY6yQ==',
    'MOE' : b'F+JTvhJSQEG1t0e2JnqS+A==',
    'LARRY' : b'iAG3PHcG4JGnUeOMMWSCpA==',
    'CURLY' : b'9xe/UwDVV4d2FgktTPe9kA=='    
}


print('ESTA TELA PERTENCE A ALICE')

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(HL.ALICE)

def fase1_Autenticacao():
    global user, addr

    #------------------------------------------------------------------------------------------------------------
    # 1) ALICE AGUARDA UM PEDIDO DE LOGIN
    # -- não precisa modificar essa seção

    print('Aguardando solicitação de LOGIN ...')
    
    data, addr = s.recvfrom(1024) 
    print('RECEBI: ', data)
    msg = HL.separaMensagem(data)  # mensagem esperada: [ 'HELLO', 'USUARIO' ]

    if len(msg) < 2 or msg[0] != 'HELLO': 
        print('recebi uma mensagem inválida')
        return False
    else:
        user = msg[1]
        user_addr = addr
        if user not in senhas.keys():
            print('Usuario desconhecido')
            return False

    #------------------------------------------------------------------------------------------------------------
    # 2) ALICE responde ao HELLO com um CHALLENGE 
    # -- troque string NONCE por um nonce em formato base64 convertido para string (decode)
    # -- troque SALT pelo salt de bob em formato base64 convertido para string (decode)

    salt = salts[user].decode()

    data = HL.formataMensagem(['CHALLENGE', 'NONCE', salt]) # TODO: modifique essa linha
    s.sendto(data, addr )


    #------------------------------------------------------------------------------------------------------------
    # 3) ALICE recebe a resposta do CHALLENGE
    # -- não precisa modificar essa seção.

    data, addr = s.recvfrom(1024) # mensagem esperada: ['CHALLENGE_RESPONSE', 'NONCE', 'HASH_SENHA' ]
    print('RECEBI: ', data)

    if addr != user_addr:
        print('mensagem de origem desconhecida')
        return False

    msg = HL.separaMensagem(data) 

    if len(msg) < 3 or msg[0] != 'CHALLENGE_RESPONSE': 
        print('recebi uma mensagem inválida')
        return False
    else:
        cs_BOB = msg[1]
        prova_do_bob = msg[2]

    #------------------------------------------------------------------------------------------------------------    
    # 4) ALICE verifica se a senha está correta
    # -- e preciso calcular o local_HASH usando a CHALLENGE da Alice
    # -- substitua PROVA_PARA_BOB pelo hash calculado com a senha de BOB e o challenge enviado por BOB

    local_HASH = senhas[user]   # TODO: modifique essa linha
    print(f'ALICE compara local_hash={local_HASH} e prova_do_bob={prova_do_bob}')

    if prova_do_bob == local_HASH:
        resposta = 'SUCCESS'
        print(f'Este usuário é {user}')       
        prova_para_bob = senhas[user] # TODO: modifique essa linha
        msg = HL.formataMensagem([ resposta, prova_para_bob ])
        s.sendto(msg, addr )
        return True 

    else:
        resposta = 'FAILURE'
        print(f'Ataque detectado: Pedido de LOGIN NEGADO!!!')
        msg = HL.formataMensagem([ resposta, 'SAI FORA, CHARLES ...' ])
        s.sendto(msg, addr )
        return False 
 
    

def fase2_MensagensAssinadas():
        
    #------------------------------------------------------------------------------------------------------------
    # 5) ALICE envia uma mensagem assinada para BOB
    # -- não precisa modificar essa seção.


        if HL.ativar_MiTM:
            msg = f'Ola {user}, voce esta autenticado na Alice'
            data = HL.assinaMensagem(msg, senhas[user]) 
            s.sendto(data, addr )
        else:
            while True:
                msg = input('Digite a mensagem: ')
                data = HL.assinaMensagem(msg, senhas[user]) 
                s.sendto(data, addr )


if __name__ == "__main__":

    while True:
        if fase1_Autenticacao():
            fase2_MensagensAssinadas()

