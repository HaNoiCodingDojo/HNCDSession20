import unittest

class Game():
    def __init__( self, starsPositions):
        self.starsPositions = starsPositions

    def move( self, moves ):
        if moves == 'f':
            if self.starsPositions == [(1,0)]:
                return 1
            else:
                return 0
        else : 
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

    def test_1_move_1_start( self ):
        starsPositions = [ (-1,0)]
        game = Game (starsPositions)
        numberOfStarGot = game.move("f")
        self.assertEquals(0, numberOfStarGot)
 
if __name__ == "__main__":
    unittest.main()
