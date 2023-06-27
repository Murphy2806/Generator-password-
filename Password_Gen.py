'''A password of customize strength and length.'''
from copy import copy
from string import punctuation
from random import choices
import string
alphabet = list(string.ascii_letters)
numbers=list(string.digits) 

class Passeword():    
    INPUT_UNIVERSE  ={
        "numbers": list(range(10)),
        "letters": list(string.ascii_letters),
        "punctuation": list(punctuation)
        
    }

    DEFAULT_LENGTHS= {
        "low":8,
        "mid":12,
        "high":16
        
    }
    
    @classmethod
    def show_input_universe(cls):
        return cls.INPUT_UNIVERSE
    
    def __init__(self, strenght="mid", length=None):
        Passeword.strenght = strenght
        Passeword.length = length
        
        self._generate()

    def _generate(self):
        '''Generates the password according to the strength and legth specified at initialization
        
        :return: the randomly generated password
        :rtype: str
        
        '''
        
        population = copy(self.INPUT_UNIVERSE["letters"])
        length = self.length or self.DEFAULT_LENGTHS.get(self.strenght)
        
        if self.strenght == "high":
            population+= self.INPUT_UNIVERSE["numbers"] + self.INPUT_UNIVERSE["punctuation"]
        else: 
            population += self.INPUT_UNIVERSE["numbers"]
        
        self.Passeword =  "".join(list(map(str, choices(population, k=length))))

if __name__=="__main__":
    p_weak = Passeword(strenght="low")
    print("weak password: " + p_weak.Passeword)
    
    p_mid = Passeword(strenght="mid")
    print("mid password: " + p_mid.Passeword)
    
    p_high = Passeword(strenght="high")
    print("high password: " + p_high.Passeword)
