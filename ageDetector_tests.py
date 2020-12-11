import unittest
import ageDetector

class FirstTest(unittest.TestCase):

    def test_DetectAgeIfPersonIsAChild(self):
        ##Arrange
        age = int(16)
        ##Act
        receive = ageDetector.agerange(age)
        ##Assert
        self.assertEqual("Olet lapsi", receive)

    def test_DetectAgeIfPersonIsAnAdult(self):
        ##Arrange
        age = int(46)
        ##Act
        receive = ageDetector.agerange(age)
        ##Assert
        self.assertEqual("Olet aikuinen", receive)

    def test_DetectAgeIfPersonIsAPensioner(self):
        ##Arrange
        age = int(72)
        ##Act
        receive = ageDetector.agerange(age)
        ##Assert
        self.assertEqual("Olet eläkeläinen", receive)

## Nämä testitapaukset voivat olla myös hyödyllisiä

    ## Jos käyttäjä syöttääkin kirjaimia tai desimaaliluvun

    def test_DetectAgeIfNotIntType(self):
        ##Arrange
        age = "tgds"
        ##Act
        receive = ageDetector.agerange(age)
        ##Assert
        self.assertEqual("Virheellinen syöte", receive)

    ## Jos käyttäjä syöttääkin negatiivisen luvun

    def test_DetectAgeIfBelowZero(self):
        ##Arrange
        age = int(-1)
        ##Act
        receive = ageDetector.agerange(age)
        ##Assert
        self.assertEqual("Ikä ei voi olla negatiivinen luku", receive)

    ## Jos käyttäjä syöttää epätodellisen suuren iän, yli 120v

    def test_DetectAgeIfTooBig(self):
        ##Arrange
        age = int(129)
        ##Act
        receive = ageDetector.agerange(age)
        ##Assert
        self.assertEqual("Mahdatko olla noin iäkäs?", receive)
    

if __name__== '__main__':
    unittest.main()
