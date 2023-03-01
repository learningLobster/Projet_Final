def Game_Board(board,n):
  
  '''
    Cette fonction a pour but de retourner un plateau de jeu à deux dimensions remplis de points
  '''
    # Création d'une liste à deux dimensions de n lignes et n colonnes, remplie de '.'

  board = [[' . '] * n for i in range(n)]
  # Affichage du plateau
  for i in range(n):
        print('\n'+ ' ', end='')
        for j in range(n):
          print(board[i][j], end='')

  return board




def place_pawn(a,b,board):

  '''
  Cette fonction a pour but de placer les pions sur le plateau de jeu en prenant en compte les coordonnées des pions des joueurs
  '''
  # Déclaration des variables où sont stockées les pions

  player1_pawn = 'x'
  player2_pawn = 'o'

  # Demande aux joueurs de saisir les coordonnées d'une case où il veut poser un pion
  
  i, j = map(int, input(f"{a}, entrez les coordonnées d'une case où vous voulez poser un pion (ligne, colonne) :").split(','))
  i, j = int(i) , int(j)

  # Place le pion du joueur 'a' sur le plateau de jeu

  board[i][j] = player1_pawn

  # Affiche le nouveau plateau de jeu avec le pion du joueur 'a' placé dessus

  for i in range(len(board)):
        print('\n' + ' ', end='')
        for j in range(len(board)):
            print(board[i][j], end='')

  i, j = map(int, input(f"{b}, entrez les coordonnées d'une case où vous voulez poser un pion (ligne, colonne) :").split(','))
  i, j = int(i) , int(j) 

  # Place le pion du joueur 'b' sur le plateau de jeu

  board[i][j] = player2_pawn

  # Affiche le nouveau plateau de jeu avec le pion du joueur 'b' placé dessus

  for i in range(len(board)):
        print('\n' + ' ', end='')
        for j in range(len(board)):
            print(board[i][j], end='')




def place_barriers(a,b,board):
  
  '''
  Cette fonction a pour but de placer les pions sur le plateau de jeu en prenant en compte les coordonnées des pions des joueurs
  '''
  # Déclaration de la variable où seront stockés les barrières

  barriers = '|'

  # Demande aux joueurs de saisir les coordonnées d'une case où il veut poser une barrière
  
  i, j = map(int, input(f"{a}, entrez les coordonnées d'une case où vous voulez poser une barrière (ligne, colonne) :").split(','))
  i, j = int(i) , int(j)

  # Place la barrière  du joueur 'a' sur le plateau de jeu

  board[i][j] = barriers

  # Affiche le nouveau plateau de jeu avec la barrière du joueur 'a' placé dessus

  for i in range(len(board)):
        print('\n' + ' ', end='')
        for j in range(len(board)):
            print(board[i][j], end='')
  
  i, j = map(int, input(f"{b}, entrez les coordonnées d'une case où vous voulez poser une barrière (ligne, colonne) :").split(','))
  i, j = int(i) , int(j) 

  # Place la barrière du joueur 'b' sur le plateau de jeu

  board[i][j] = barriers

  # Affiche le nouveau plateau de jeu avec la barrière  du joueur 'b' placé dessus

  for i in range(len(board)):
        print('\n' + ' ', end='')
        for j in range(len(board)):
            print(board[i][j], end='')