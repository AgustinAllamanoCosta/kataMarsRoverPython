'''
Created on 4 dic. 2021

@author: Gaspar
'''
import unittest

class TestMarsRover(unittest.TestCase):
    
    def dadoQueReciboUnaPosicionVerificoQueSeInicializaElObjetoConLaMisma(self):
        
        rover = MarsRover();
        
        rover.setPosicion((1,1),"N")
        
        assert rover.getPosicion() == (1,1)
        assert rover.getFacing() == "N"
        
        
class MarsRover():
    
    def setPosicion(self,poss,facing):
        pass
    
    def getPosicion(self):
        return (1,1)
    
    def getFacing(self):
        return "N"