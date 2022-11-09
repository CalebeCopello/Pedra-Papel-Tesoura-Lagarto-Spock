#importação dos modulos
import random
import time
#escolha das cores
col_r = '\033[0;31;40m'
col_g = '\033[0;32;40m'
col_y = '\033[0;33;40m'
col_d = '\033[0;37;40m'
#mensagens iniciais
print('Vamos jogar Pedra-papel-tesoura-lagarto-Spock')
print('Escolha a sua jogada:\n[0]Pedra\n[1]Papel\n[2]Tesoura\n[3]Lagarto\n[4]Spock')
#tracking das escolhas do jogador e da IA
choice_pl = int(input('Qual a sua jogada? {}'.format(col_y)))
choice_pc = int(random.randint(0,4))
#calculando os resultados
if choice_pc == choice_pl:
  game = str('{}EMPATE!{}'.format(col_y, col_d))
  game_res = 'empate'
else:
  game_res =''
  if choice_pl == 0 and choice_pc == 2 or choice_pl == 0 and choice_pc == 3:
    game = str('Você {}GANHOU!{}'.format(col_g, col_d))
    if choice_pc == 2:
      action = str('quebra')
    else:
      action = str('esmaga')
  elif choice_pl == 1 and choice_pc == 0 or choice_pl == 1 and choice_pc == 4:
    game = str('Você {}GANHOU!{}'.format(col_g, col_d))
    if choice_pc == 0:
      action = str('enrola')
    else:
      action = str('refuta')
  elif choice_pl == 2 and choice_pc == 1 or choice_pl == 2 and choice_pc ==3:
    game = str('Você {}GANHOU!{}'.format(col_g, col_d))
    if choice_pc == 1:
      action = str('corta')
    else:
      action = str('decapita')
  elif choice_pl == 3 and choice_pc == 1 or choice_pl == 3 and choice_pc == 4:
    game = str('Você {}GANHOU!{}'.format(col_g, col_d))
    if choice_pc == 1:
      action = str('come')
    else:
      action = str('envenena')
  elif choice_pl == 4 and choice_pc == 0 or choice_pl == 4 and choice_pc == 2:
    game = str('Você {}GANHOU!{}'.format(col_g, col_d))
    if choice_pc == 0:
      action = str('vaporiza')
    else:
      action = str('quebra')
  else:
    game_res = 'derrota'
    game = str('Você {}PERDEU!{}'.format(col_r, col_d))
    if choice_pl == 2 and choice_pc == 0:
      action = str('quebra')
    elif choice_pl == 3 and choice_pc == 0:
      action = action = str('esmaga')
    elif choice_pl == 0 and choice_pc == 1:
      action = str('enrola')
    elif choice_pl == 4 and choice_pc == 1:
      action = str('refuta')
    elif choice_pl == 1 and choice_pc == 2:
      action = str('corta')
    elif choice_pl == 3 and choice_pc == 2:
      action = str('decapita')
    elif choice_pl == 1 and choice_pc == 3:
      action = str('come')
    elif choice_pl == 4 and choice_pc == 3:
      action = str('envenena')
    elif choice_pl == 0 and choice_pc == 4:
      action = str('evapora')
    elif choice_pl == 2 and choice_pc == 4:
      action = str('quebra')
opções = ('Pedra', 'Papel', 'Tesoura', 'Lagarto', 'Spock')
time.sleep(0.3)
print('Pedra')
time.sleep(0.3)
print('Papel')
time.sleep(0.3)
print('Tesoura')
time.sleep(0.3)
print('Lagarto')
time.sleep(0.3)
print('Spock!')
time.sleep(0.3)
#mostrando os resultados
if game_res == 'empate':
  print('{}O computador jogou: {}{}{}\nVocê jogou: {}{}{}\nResultado {}'.format(col_d, col_y, opções[choice_pc], col_d, col_y, opções[choice_pl], col_d, game))
elif game_res == 'derrota':
  print('{}O computador jogou: {}{}{}\nVocê jogou: {}{}{}\nResultado {}\n{} {}{}{} {}'.format(col_d, col_y, opções[choice_pc], col_d, col_y, opções[choice_pl], col_d, game, opções[choice_pc], col_y, action.upper(), col_d, opções[choice_pl]))
else:
  print('{}O computador jogou: {}{}{}\nVocê jogou: {}{}{}\nResultado {}\n{} {}{}{} {}'.format(col_d, col_y, opções[choice_pc], col_d, col_y, opções[choice_pl], col_d, game, opções[choice_pl], col_y, action.upper(), col_d, opções[choice_pc]))
  