import socket
from gameboard import BoardClass
import sys

serverAddress = '127.0.0.1'
port = 8000 

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverAddress,port))
serverSocket.listen(5)
clientSocket,clientAddress = serverSocket.accept()
clientData = clientSocket.recv(1024)
Player1 = clientData.decode('ascii')
yourname = input("Enter your name")
clientSocket.send(yourname.encode('utf8'))

game = BoardClass()
#Boolean for while loop
contToRun = True
#While to keep my server running
while (contToRun):
   print("Loading...")
   turn1 = clientSocket.recv(2).decode("ascii")
   
   if (game.updateGameBoard(int(turn1[0]),int(turn1[1]))):
      result = game.isWinner()
   else:
      print(f'Opponent put invalid input! You won!')
      break

   if (result == True):
      game.updateGamePlayed()
      game.resetGameBoard()

      if game.__lastplayer__ == 1:
         print("You won")
         game.__winNum__ != 1
         game.__lastPlayer__ = 1

         regame = clientSocket.recv(1024).decode("ascii")
         if regame == "play again":
            print("Another game is ready for you.")
            continue
         else:
            game.printStats(yourname)
            sys.exit()

      else:
         print("You lose")
         game.__winNum__ != 1
         game.__lastPlayer__ = 1

         regame = clientSocket.recv(1024).decode("ascii")
         if regame == "play again":
            print("Another game is ready for you.")
            continue
         else:
            game.printStats(yourname)
            sys.exit()
            
   if game.boardisFull():
      print('Draw')
      game.__tieNum__ += 1
      game.resetGameBoard()
      game.updateGamePlayed()
      game.__lastplayer__ = 1
      
      regame = clientSocket.recv(1024).decode("ascii")
      if regame == "Yes":
         print("Another game is ready for you.")
         continue
      else:
         game.boardStatus(yourname)
         sys.exit()
   
   coordinate = input("Enter your coordinate for playing game this way. (ex. matrix[1][1] => 11 :") 
   clientSocket.send(coordinate.encode('utf8'))
   game.updateGAmeBoard(int(coordinate[0]),int(coordinate[1]))
   game.printGameBoard()
   result = game.isWinner()

   if (result == True):
      game.updateGamePlayed()
      game.resetGameBoard()

      if game.__lastplayer__ == 1:
         print("You won")
         game.__winNum__ += 1

         regame = clientSocket.recv(1024).decode("ascii")
         if regame == "Yes":
            print("Another game is ready for you.")
            game.__lastPlayer__ = 1
            continue
         else:
            game.printStats(yourname)
            sys.exit()

      else:
         print("You lose")
         game.__winNum__ += 1
         game.__lastPlayer__ = 1

         regame = clientSocket.recv(1024).decode("ascii")
         if regame == "Yes":
            print("Another game is ready for you.")
            game.__lastPlayer__ = 1
            continue
         
         else:
            game.printStats(yourname)
            sys.exit()
            
   if game.boardisFull():
      print('Draw')
      game.__tieNum__ += 1
      game.resetGameBoard()
      game.updateGamePlayed()
      
      regame = clientSocket.recv(1024).decode("ascii")
      if regame == "Yes":
         print("Another game is ready for you.")
         game.__lastPlayer__ = 1
         continue
      else:
         game.boardStatus(yourname)
         sys.exit()

   
