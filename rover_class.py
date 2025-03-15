import random
from poi_class import Position, Poi
class Rover_individual:
    def __init__(self, position: Position, chromosome: list): 
        self.position = position
        self.chrmosome = chromosome
        self.fitness = self.cal_fitness() 
  
    @classmethod
    def mutated_genes(self):
        global GENES 
        gene = random.choice(GENES) 
        return gene 
    
    @classmethod
    def create_gnome(self):
        global GENES 
        gnome_len = len(GENES) 
        return [self.mutated_genes() for _ in range(gnome_len)] 
    
    def cal_path_cost(self, end_point, hour_per_distance_unit):
        return Position.check_distance(self, end_point) * hour_per_distance_unit

    def mate(self, par2): 
        child_chromosome = []
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):  
            prob = random.random()  
            if prob < 0.45: 
                child_chromosome.append(gp1)  
            elif prob < 0.90:  # zmniejszajac to zwiekszamy szanse na mutacje(narazie jest tylko 10%)
                child_chromosome.append(gp2) 

            else: 
                child_chromosome.append(self.mutated_genes()) 
        return Rover_individual(child_chromosome) 
  
    def cal_fitness(self):
        time = 0
        for i in self.chrmosome:
            time += (Position.check_distance(self.position, i.position) + i.time_of_task) #tu oblicznamy czas dla kazdego poia + czas dojechania tam
            self.position = i.position #tu zmnieniamy pozycje lazika
        
        global Best_time

        return time - Best_time

