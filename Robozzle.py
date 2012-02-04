import unittest

class Game():
    def __init__( self, starsPosition ):
        self.starsPosition = starsPosition

    def move( self, moves ):
        return len(self.starsPosition)

class RobozzleTest(unittest.TestCase):

    def test_true(self):
        self.assertEquals(True, True)

    def test_0_move_0_star(self):
        starsPosition=[]
        game = Game(starsPosition)
        numberOfStarGot = game.move("")
        self.assertEquals(len(starsPosition),numberOfStarGot)

    def test_1_move_1_star(self):
        starsPosition = [ (1,0) ]
        game = Game( starsPosition)
        numberOfStarGot = game.move("f")
        self.assertEquals( len(starsPosition), numberOfStarGot)

    def test_0_move_1_star( self ):
        starsPosition = [ (1,0) ]
        game = Game( starsPosition)
        numberOfStarGot = game.move("")
        self.assertEquals( 0, numberOfStarGot)


if __name__ == "__main__":
    unittest.main()
