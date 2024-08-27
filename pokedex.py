import os
import random

def limpar_tela():
  os.system('cls')

limpar_tela()
inventario = [5, 0]
pokedex = []
menu = ["1- Iniciar jornada", "2- Inventario", "3- Pokedex", "4- Perfil", "5- Sair"]
pokemons_gerados = []
contador = 0
def zerou_o_game():
  for x in pokedex:
    contador += 1
  
  if contador == 50:
    limpar_tela()
    print('Parabéns, vc zerou o game!!')
    print('Espero que tenha se divertido!')
    input('Pressione enter para sair')
  
def criar_level():
  probabilidade = random.randint(0,10)

  if probabilidade in range(0,7):
    level_baixo = random.randint(1,20)
    return level_baixo
  elif probabilidade in range(7,10):
    level_medio = random.randint(21,40)
    return level_medio
  else:
    level_alto = random.randint(41,50)
    return level_alto

print('Bem vindo a uma pequena jornada de """pokémon"""')
nome_jogador = input(str('por favor, insira seu nome -> '))
limpar_tela()
player = {
    "nome": nome_jogador,
    "level": 1,
    "exp": 0,
    "exp_max": 30,
    "hp": 100,
    "hp_max": 100,
    "dano": 50,
}
def melhorar_atributos():
  if player["exp"] >= player["exp_max"]:
    player["level"] += 1
    player["exp"] = 0
    player["exp_max"] += 20 * player['level']
    player["dano"] += 25
    player["hp_max"] += 25
    player["hp"] == ["hp_max"] 
    print('Você subiu de nivel!')

def ganhou_pokebola():
  quantidade_pokebola_obtida = random.randint(0,3)
  print(f'você obteve {quantidade_pokebola_obtida} pokebolas')
  inventario[0] += quantidade_pokebola_obtida
  
def ganhou_potion():
  print('')
  quantidade_potion_obtida = random.randint(0,5)
  print(f'você obteve {quantidade_potion_obtida} poções')
  inventario[1] += quantidade_potion_obtida
  
print(f'Olá, {nome_jogador}! Você vai começar no lvl 1 e com cinco pokebolas')  
input('Pressione "Enter" para começar ')

def criar_pokemon():
    level = criar_level()

    novo_pokemon = {
        "nome": f"Pokemon #{level}",
        "level": level,
        "dano": 4 * level,
        "hp": 100 * level,
        "hp_max": 100 * level,
        "exp": 7 * level,
    }
    return novo_pokemon
    
def ganhar_xp():
  global player
  global criar_pokemon
  if novo_pokemon['level'] in range(0,19):
    print('vc ganhou 20 de xp')
    pouco_exp = 20
    player['exp'] += pouco_exp
  elif novo_pokemon['level'] in range(20,40):
    print('vc ganhou 50 de xp')
    medio_exp = 50
    player['exp'] += medio_exp
  else:
    print('vc ganhou 100 de xp')
    alto_exp = 100
    player['exp'] += alto_exp
  return ganhar_xp    
    
def ataque_do_pokemon():
  global novo_pokemon
  global player
  while player ['hp'] > 0:
    vida_atualizada = player['hp'] - novo_pokemon["dano"]
    vida_atualizada_sem_0 = max(vida_atualizada, 0)
    player['hp'] = vida_atualizada_sem_0
    print(f'o pokémon atacou e deu {novo_pokemon["dano"]} de dano, sua vida agora é {vida_atualizada_sem_0}')
    if player['hp'] <= 0:
      print('você morreu!')
    return

def atacar_e_capturar_pokemon():
  global novo_pokemon
  global quantidade_pokebola_obtida
  
  while novo_pokemon['hp'] >= 0:
    dano_do_jogador_sob_pokemon = player["dano"]
    print(f'pokémon # {novo_pokemon["level"]} está no nivel {novo_pokemon["level"]} e tem {novo_pokemon["hp"]} de vida')
    if novo_pokemon in pokedex:
      print('você já tem esse pokemon na pokedex')
    print('1- atacar')
    print('2- fugir')
    atacou = input('#')
    limpar_tela()
    
    if atacou == '1':
      vida_atualizada = novo_pokemon["hp"] - dano_do_jogador_sob_pokemon
      vida_atualizada_sem_0 = max(vida_atualizada, 0)
      print(f'você causou {dano_do_jogador_sob_pokemon} de dano')
      print(f'a vida do pokémon agora é {vida_atualizada_sem_0}')
      input('')
      limpar_tela()
      novo_pokemon["hp"] = vida_atualizada
      gerador_ataque_pokemon = random.randint(0,1)
      if gerador_ataque_pokemon == 1 and novo_pokemon["hp"] > 0:
        print('ele te atacou de volta!')
        ataque_do_pokemon()
        if player['hp'] <= 0:
          input('')
          limpar_tela()
          break
        input('')
        limpar_tela()
      
    elif atacou == '2':
      print('Você fugiu')
      input('')
      limpar_tela()
      break
    
    vida_para_capturar = 5 * novo_pokemon["level"]
    
    if novo_pokemon['hp'] <= vida_para_capturar:
      print('é possivel tentar captura-lo')
      print('')
      print('1- Capturar')
      print('2- Não capturar')
      tentativa_captura = input('#')
      limpar_tela()

      while True:
        tentativa_para_capturar = random.randint(0,5)
        
        if tentativa_captura == '1':
          print('vc gastou uma pokebola para tentar pega-lo')
          inventario[0] -= 1
          
          if tentativa_para_capturar in range(0,4):
            print('')
            print('pokemon capturado')
            print('')
            ganhar_xp()
            print('')
            melhorar_atributos()
            ganhou_pokebola()
            ganhou_potion()
            if novo_pokemon in pokedex:
              try:
                pass
              except:
                print('pokemon já adicionado')
                input('#')
            else:
              pokedex.append(novo_pokemon)
            input('#')
            limpar_tela()
            break
          
          elif tentativa_para_capturar in range (4,5):
            print('não foi possivel')
            print('tente novamente')
            input('#')
            limpar_tela()
          
          else:
            print('o pokemon fugiu!')
            ganhou_pokebola()
            ganhou_potion()
            input('')
            limpar_tela()
            break
        
        elif tentativa_captura == '2':
          ganhar_xp()
          print('')
          melhorar_atributos()
          print('')
          ganhou_pokebola()
          ganhou_potion()
          print('')
          print('pokemon desapareceu')
          input('')
          limpar_tela()
          break
        else:
          break
      break
    

def iniciar_jornada():
  while True:
    if player['hp'] <= 0:
      print('você não tem vida para continuar, por favor, use uma poção')
      input('#')
      limpar_tela()
      break
    print('durante sua jornada você encontra um pokemón, vamos batalhar! ') 
    print('')
    global novo_pokemon
    novo_pokemon = criar_pokemon()
    print(f'um pokémon level {novo_pokemon["level"]} apareceu. ele tem {novo_pokemon['hp']} de vida')
    print('')
    print('1- continuar')
    print('2- voltar')
    print('')
    print('pressione enter caso queira pular para o proximo pokémon!')
    print(' ')

    escolha_atacar = input('o que deseja fazer? ')
    limpar_tela()
    
    if escolha_atacar == '1':
      atacar_e_capturar_pokemon()
    elif escolha_atacar == '2':
      break 

def mostrar_infos_jogador():
    global player
    nome = player["nome"]
    level = player["level"]
    exp = player["exp"]
    exp_max = player["exp_max"]
    hp = player["hp"]
    hp_max = player["hp_max"]
    dano = player["dano"]

    print(f'Olá {nome}! Você está no lvl {level} com {exp} de exp. Você subirá de nível ao alcançar {exp_max}.')
    print(f'Você pode causar {dano} de dano. Sua vida está em {hp} e seu HP máximo é {hp_max}.')
    print('')
    deseja_cura = input(f'deseja usar uma potion[{inventario[1]}] para recuperar sua vida?[1-Sim/2-Não] #')
    if deseja_cura == '1' and inventario[1] > 0:
      inventario[1] -= 1
      player['hp'] = player['hp_max']
    elif deseja_cura == '2':
      pass
    
    else:
      print('escolha uma opção valida')
      print('')
    
    input('Pressione enter para sair -> ')


def mostrar_inventario():
  print(f'Inventário atual: Pokébolas: {inventario[0]}, Poções: {inventario[1]}')
  input('Pressione enter para sair -> ')

def exibir_pokemons_capturados():
  pokedex.sort(key=lambda pokemon: pokemon["level"])
    
  for pokemon in pokedex:
    nome = pokemon["nome"]
    level = pokemon["level"]
    print(f"{nome}, Level: {level}")
    
  input('pressione enter para sair -> ')


def zerou_o_game():
  contador = 0
  for item in pokedex:
    contador += 1
  
  if contador == 50:
    limpar_tela()
    print('Parabéns, vc zerou o game!!')
    print('Espero que tenha se divertido!')
    input('Pressione enter para sair')

while True:
  limpar_tela()
  zerou_o_game()
  for x in menu:
    print(x)

  zerou_o_game()  
  escolha_menu = input('escolha uma das opções #')
  limpar_tela()

  try:
    if escolha_menu == "1":
      iniciar_jornada()

    elif escolha_menu == "2":
      mostrar_inventario()

    elif escolha_menu == "3":
      exibir_pokemons_capturados()

    elif escolha_menu == "4":
      
      mostrar_infos_jogador()

    elif escolha_menu == "5":
      print('saindo do jogo...')
      break

    elif escolha_menu == "6":
      criar_pokemon()

    elif escolha_menu == "7":
      inventario[1] += 1
      print('poção adicionada, secrets secrets hehehe')
      input('pressione enter para sair -> ')
    
    else:
      print('escolha uma opção válida!')

  except SyntaxError:
    print('Por favor, tente novamente')
  
contador = 0
def zerou_o_game():
  for x in pokedex:
    contador += 1
  
  if contador == 50:
    limpar_tela()
    print('Parabéns, vc zerou o game!!')
    print('Espero que tenha se divertido!')
    input('Pressione enter para sair')
