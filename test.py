from poi_class import * #Trzeba tu zminic zeby tylko byly funkcje potrzebne
from rover_class import *



if __name__ == "__main__":
    print("Start")
    out = Poi.gen_random_list_of_pois(3,3, 3, 3, 5)
    for i in out:
        print(i)