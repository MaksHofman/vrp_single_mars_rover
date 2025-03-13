import random

class Rover_individual: # TO WSZYSTKO TRZEBA ZREWORKOWAC
    def __init__(self, chromosome): 
        self.chrmosome = chromosome
        self.fitness = self.cal_fitness() 
  
    @classmethod
    def mutated_genes(self): #moze szanas na mutacjie 0.1? tez jak mate trzeba zobaczyc jak najlepiej
        pass
  
    @classmethod
    def create_gnome(self):  #geny to beda randomowe poie
        pass
  
    def mate(self, par2): # chyba normalne przetasownie %3 chyba(do ustawienia)
        pass
  
    def cal_fitness(self): # zrobienie wszystkich taskow lub jak przez kilka generacji nic sie nie dzieje to max ilosc
        pass

    # trzeba tez zrobic cala logike obliczania odleglosci i dodawnia czasu po przejsciu drogi (chyba to w cal fitnes trzeba)