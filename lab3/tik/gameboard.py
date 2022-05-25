class BoardClass():

    def __init__(self):
        self.gameboardMatrix = [[0, 0, 0],
                                [0, 0, 0],
                                [0, 0, 0]]
        self.__userName__ = 0
        self.__lastPlayer__ = 0
        self.__winNum__ = 0
        self.__tieNum__ = 0
        self.__loseNum__ = 0
        self.__totalGameNum__ = 0
        self.__turn__ = 0

    def updateGamesPlayed(self):
        
        self.__totalGameNum__ += 1

        
    def resetGameBoard(self):
        self.gameboardMatrix =[[0, 0, 0],
                               [0, 0, 0],
                               [0, 0, 0]]
        
    def updateGameBoard(self, x:int , y:int):
        if (0 <= x <= 3) and (0 <= y <= 3) and (self.gameboardMatrix[x][y] == 0):
            if self.__lastPlayer__ == 1:
                self.gameboardMatrix[x][y] = 'O'
                self.__lastPlayer__ = 2
            else:
                self.gameboardMatrix[x][y] = 'X'
                self.__lastPlayer__ = 1
            return self.gameboardMatrix
        else:
            return False
            

    def isWinner(self):
        for u in range(3):
            if (self.gameboardMatrix[0][u] !=0 ) and (self.gameboardMatrix[0][u] == self.gameboardMatrix[1][u]==self.gameboardMatrix[2][u]):
                return True
        for i in range(3):
            if (self.gameboardMatrix[i][0] != 0) and (self.gameboardMatrix[i][0] == self.gameboardMatrix[i][1]==self.gameboardMatrix[i][2]):
                return True
        if self.gameboardMatrix[0][0] == self.gameboardMatrix[1][1] == self.gameboardMatrix[2][2] != 0:
            return True
        if self.gameboardMatrix[0][2] == self.gameboardMatrix[1][1] == self.gameboardMatrix[2][0] != 0:
            return True
        else:
            return False
    def boardlsFull(self):
        for i in self.gameboardMatrix:
            for u in i:
                if u == 0:
                    return False 
        
        return True
    def printGameBoard(self):
        for i in self.gameboardMatrix:
            print(i)
        
    def printStats(self,name):
        print('Player name: ', name)
        print("Game Played Number: ", self.__totalGameNum__)
        print('Wins: ', self.__winNum__)
        print('Loses: ', self.__loseNum__)
        print('Ties: ', self.__tieNum__)

if __name__ == "__main__":
    game = BoardClass()
    #a = game.updateGameBoard(1,2)
    #print(a)
    #game.updateGameBoard(2,2,1)
    
    #game.updateGameBoard(0,0,1)
    #c= game.updateGameBoard(1,1,1)p
    #print(c)
    for i in range(3):
        for u in range(3):
            game.updateGameBoard(i,u)
    game.__userName__ = "Sean"
    print(game.__userName__)
    game.printStats()
    game.updateGamesPlayed()
    game.printStats()
    
    print(game.gameboardMatrix)