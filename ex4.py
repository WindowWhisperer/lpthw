dogs = 1000
dogs_in_cars = 5.0
humans = 2
cars = 37
average_dogs_in_cars = dogs / cars
dogs_still_needing_rides = dogs - dogs_in_cars * cars

print("There are" , humans, "people")
print("And those people have" , dogs, "dogs.")
print("They can't walk all those dogs, can they? No, they need dogs to go to daycare.")
print("The daycare has" , cars, "cars.")
print("They would need to be very big cards to hold" , average_dogs_in_cars, "dogs in each car.")
print("But they can only hold", dogs_in_cars, "dogs per car.")
print("How many dogs will still need a ride?")
print(dogs_still_needing_rides)