import unittest



class RobozzleTest(unittest.TestCase):

    def test_true(self):
        self.assertEquals(True, True)

    def test_0_move_0_star(self):
        starsPosition=[]
        game = Game(starsPosition)
        numberOfStarGot = game.move("")
        self.assertEquals(len(starsPosition),numberOfStarGot)

if __name__ == "__main__":
    unittest.main()
