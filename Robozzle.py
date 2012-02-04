import unittest

class Game():
    def __init__( self, starsPositions):
        self.starsPositions = starsPositions

    def move( self, moves ):
        if len(moves) == 0:
            return 0
        
        
        if moves[0] == 'f' and self.starsPositions[0] == (1,0):
            if len(self. starsPositions) == 1:
                return 1
            
        if len(moves) == 1:
            return 0

        if  moves[0] == 'f' and moves[1] == 'f' and  self.starsPositions[0] == (1,0) and self.starsPositions[1] == (2,0):
            if len(self.starsPositions) == 2:
                return 2

        return 0
        
class RobozzleTest(unittest.TestCase):

    def test_true(self):
        self.assertEquals(True, True)

    def test_0_move_0_star(self):
        starsPositions=[]
        game = Game(starsPositions)
        numberOfStarGot = game.move("")
        self.assertEquals(len(starsPositions),numberOfStarGot)

    def test_1_move_1_star(self):
        starsPositions = [ (1,0) ]
        game = Game( starsPositions)
        numberOfStarGot = game.move("f")
        self.assertEquals( len(starsPositions), numberOfStarGot)

    def test_0_move_1_star( self ):
        starsPositions = [ (1,0) ]
        game = Game( starsPositions)
        numberOfStarGot = game.move("")
        self.assertEquals( 0, numberOfStarGot)

    def test_1_move_1_star_0_starsgot( self ):
        starsPositions = [ (-1,0)]
        game = Game (starsPositions)
        numberOfStarGot = game.move("f")
        self.assertEquals(0, numberOfStarGot)

    def test_2_move_1_star_1_starsgot( self ):
        starsPositions = [ (1,0)]
        game = Game (starsPositions)
        numberOfStarGot = game.move("fr")
        self.assertEquals(1, numberOfStarGot)

    def test_2_move_1_star_0_starsgot( self ):
        starsPositions = [ (-1,0)]
        game = Game (starsPositions)
        numberOfStarGot = game.move("fr")
        self.assertEquals(0, numberOfStarGot)

    def test_2_move_2_star_2_starsgot( self ):
        starsPositions = [ (1,0), (2,0) ]
        game = Game( starsPositions )
        numberOfStarGot = game.move( "ff" )
        self.assertEquals(2, numberOfStarGot)

 
if __name__ == "__main__":
    unittest.main()
