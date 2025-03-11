import random

class rover_individual(object):
    def __init__(self, chromosome):
        self.chrmosome = chromosome
        self.fitness = self.cal_fitness() 
  
    @classmethod
    def mutated_genes(self): 
        global GENES 
        gene = random.choice(GENES) 
        return gene 
  
    @classmethod
    def create_gnome(self): 
        global TARGET 
        gnome_len = len(TARGET) 
        return [self.mutated_genes() for _ in range(gnome_len)] 
  
    def mate(self, par2): 
        # chromosome for offspring 
        child_chromosome = [] 
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):     
            prob = random.random() 
            if prob < 0.45: 
                child_chromosome.append(gp1) 
            elif prob < 0.90: 
                child_chromosome.append(gp2) 
            else: 
                child_chromosome.append(self.mutated_genes()) 
        return rover_individual(child_chromosome) 
  
    def cal_fitness(self): 
        global TARGET 
        fitness = 0
        for gs, gt in zip(self.chromosome, TARGET): 
            if gs != gt: fitness+= 1
        return fitness