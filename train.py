from poi_class import * #Trzeba tu zminic zeby tylko byly funkcje potrzebne
from rover_class import *

def main():
    Amout_of_pois = 10
    Max_time_for_task_in_poi = 3
    Max_X_bound = 10
    Max_Y_bound = 10
    Max_piority = 5
    global GENES
    GENES = Poi.gen_random_list_of_pois(Amout_of_pois, Max_time_for_task_in_poi, Max_X_bound, Max_Y_bound, Max_piority)
    



if __name__ == "__main__":
    main()

    