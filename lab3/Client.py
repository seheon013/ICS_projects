import socket
from gameboard import BoardClass
import sys

serverAddress = '127.0.0.1' #input("Please enter ip address:")
port = 8000 #int(input("Please enter port number:"))

name =input("Please enter your name:")

connectionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connectionSocket.connect((serverAddress,serverPort))
connectionSocket.send(hostname.encode('utf8'))
serverData = connectionSocket.recv(1024)
Player2 = serverData.decode('ascii')


game = BoardClass()

contToRun = True
while (contToRun):
    
    coordinate = input("Enter your coordinate for playing game this way. (ex. matrix[1][1] => 11 :") 
    clientSocket.send(coordinate.encode('utf8'))
    game.updateGAmeBoard(int(coordinate[0]),int(coordinate[1]))
    game.printGameBoard()
    result = game.isWinner()
    
    if (result == True):
        game.updateGamePlayed()
        game.resetGameBoard()
        
        if game.__lastplayer__ == 1:
            print('You lose')
            game.__losenum__ += 1
            game.__lastplayer__ = 1
            
            while True:
                ask = input("Another game? type y/Y or n/N")
                if ask == 'y' or ask == 'Y':
                    ans = 'Yes'
                    connectionSocket.send(ans.encode('utf8'))
                    break
                elif ask == 'n' or ask == 'N':
                    ans = 'No'
                    connectionSocket.send(ans.encode('utf8'))
                    game.printStats(name)
                    sys.exit()

                else:
                    print('Not valid input')

    if game.boardisFull():
        print('Draw')
        game.__tieNum__ += 1
        game.resetGameBoard()
        game.updateGamePlayed()
        
        while True:
            ask = input("Another game? type y/Y or n/N")
            if ask == 'y' or ask == 'Y':
                ans = 'Yes'
                connectionSocket.send(ans.encode('utf8'))
                break
            elif ask == 'n' or ask == 'N':
                ans = 'No'
                connectionSocket.send(ans.encode('utf8'))
                game.printStats(name)
                sys.exit()

            else:
                print('Not valid input')
                
    print("Loading...")
    turn2 = clientSocket.recv(2).decode("ascii")

    if (game.updateGameBoard(int(turn2[0]),int(turn2[1]))):
        result = game.isWinner()

      
                    
                
                    
                
                  

connectionSocket.close()

