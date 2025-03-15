from poi_class import * #Trzeba tu zminic zeby tylko byly funkcje potrzebne
from rover_class import *

GENES = []

Best_time = 360000

def main():
    print("start")
    Amout_of_pois = 3
    POPULATION_SIZE = 100
    Max_time_for_task_in_poi = 3
    Max_X_bound = 10
    Max_Y_bound = 10
    Max_piority = 5
    global GENES
    GENES = Poi.gen_random_list_of_pois(Amout_of_pois, Max_time_for_task_in_poi, Max_X_bound, Max_Y_bound, Max_piority)
    global Best_time
    Last_best_time = 0
    loop_after_peak = 100000
    generation = 1
    found = False
    population = [] 

    for _ in range(POPULATION_SIZE): 
                gnome = Rover_individual.create_gnome(GENES) 
                population.append(Rover_individual(Position(0,0), gnome, Best_time, GENES)) 
  
    while not loop_after_peak == 0: 
        population = sorted(population, key = lambda x:x.fitness) 
  
        if population[0].fitness < Best_time:  #to tzeba przerobic zeby sprawdzalo czy jest progres
            Last_best_time = Best_time
            Best_time = population[0].time

        if Last_best_time != Best_time and found == True:
             found = False
             loop_after_peak = 10

        if Last_best_time == Best_time and found != True:
            found = True
            loop_after_peak -= 1
  
        new_generation = [] # od tego punktu nie dziala (nowe generacje sie zle tworza(sa takie same))
   
        s = int((10*POPULATION_SIZE)/100) 
        new_generation.extend(population[:s]) 
   
        s = int((90*POPULATION_SIZE)/100) 
        for _ in range(s): 
            parent1 = random.choice(population[:50]) 
            parent2 = random.choice(population[:50]) 
            child = parent1.mate(parent2, Best_time) 
            new_generation.append(child) 
  
        population = new_generation 
  
        #print(f"Generation: {generation} String: {population[0].chromosome} Fitness: {population[0].fitness}") # trzeba to na wizualizacje zmienic
        print(f"Best time{Best_time}, Last Time = {Last_best_time}, Geratiuon {generation}")
        loop_after_peak -= 1
        generation += 1

      
   # print(f"Generation: {generation} String: {population[0].chromosome} Fitness: {population[0].fitness}") 



if __name__ == "__main__":
    main()

    