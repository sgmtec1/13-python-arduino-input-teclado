# INPUT ESTADO DO LED
from pyfirmata import Arduino, util, OUTPUT
import lcd
import time

board=Arduino ('COM5')

board.digital[7].mode = OUTPUT

while True:
    lcd.escrever(board, 0, 0, 'DIGITE 0 OU 1    ')
    estado = input('Digite 1 para ligar o LED ou 0 para desligar: ')
    if estado == '0' or estado =='1':
        board.digital[7].write(int(estado))
        lcd.escrever(board, 0, 1, f'{estado}            ')
    else:
        lcd.escrever(board, 0, 0, 'ERRO: 0 OU 1         ')
        print ('ERRO: Digite apenas 0 ou 1!     ')
        time.sleep(4.0)
time.sleep(10.0)
board.exit()