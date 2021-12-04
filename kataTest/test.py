'''
Created on 4 dic. 2021

@author: Gaspar
'''
import unittest

class TestMarsRover(unittest.TestCase):
    
    def test_dadoQueReciboUnaPosicionUnoUnoVerificoQueSeInicializaElObjetoConLaMisma(self):
        
        rover = MarsRover();
        
        rover.setPosicion((1,1),"N")
        
        assert rover.getPosicion() == (1,1)
        assert rover.getFacing() == "N"
        
    def test_dadoQueReciboUnaPosicionDosDosVerificoQueSeInicializaElObjetoConLaMism(self):
        
        rover = MarsRover();
        
        rover.setPosicion((2,2),"S")
        
        assert rover.getPosicion() == (2,2)
        assert rover.getFacing() == "S"
        
class MarsRover():
    
    def setPosicion(self,poss,facing):
        self.poss = poss
        self.facing = facing
    
    def getPosicion(self):
        return self.poss
    
    def getFacing(self):
        return self.facing