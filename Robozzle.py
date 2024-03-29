import unittest

class Game():
    def __init__( self, starsPositions):
        self.starsPositions = starsPositions

    def newPosition( self, currentPosition, move ):
        pos = currentPosition
        if move == 'f':
            pos = ( pos[0] + 1, pos[1])
        return pos

    def move( self, moves ):
        numberOfStars = 0

        interestingStarPosition = (0,0)

        for i in range( len(moves) ): # 0, 1
            interestingStarPosition = self.newPosition( interestingStarPosition, moves[i] )
            if moves[i] == 'f':
                if interestingStarPosition in self.starsPositions:
                    numberOfStars += 1


        return numberOfStars
        
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

    def test_2_move_2_star_reversed_2_starsgot( self ):
        starsPositions = [ (2,0), (1,0) ]
        game = Game( starsPositions )
        numberOfStarGot = game.move( "ff" )
        self.assertEquals(2, numberOfStarGot)

 
if __name__ == "__main__":
    unittest.main()
