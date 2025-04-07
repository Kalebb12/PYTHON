import random
import my_module

random_int = random.randint(1, 10)
print(random_int)
print(my_module.pi)

random_float = random.random() * 6
print(random_float)

states_of_america = ["Delaware", "Pennsylvania", "New Jersey"]
fruits = ["Apple", "Peach", "Pear"]
vegetables = ["Carrot", "Potato", "Cucumber"]
dirty_dozens = [fruits, vegetables]
print(dirty_dozens)

states_of_america.append("CalebLand")
# print(states_of_america[1])
# print(states_of_america)