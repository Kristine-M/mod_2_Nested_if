#task 1.1
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")
    
#task 1.2 (expanding from above)
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
    action_2 = input("light a torch or proceed in the dark")
    if action_2 == "light a torch":
        print("You found the dragon's cave")
    else:
        print("You got eaten by the dragon")

#task 1.3 (expanding from above)
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
    action_2 = input("light a torch or proceed in the dark")
    if action_2 == "light a torch":
        pass
    else:
        print("You did not light a torch")
        
#task 2.1

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

#task 2.2

additional = "audio system" if attendees > 150 else "projector"
print(additional)

#task 2.3

want_vegetarian = True

caterers = "Veggie Delight Caterers" if want_vegetarian else "Gourmet Meals Caterers"
print(caterers)


# task 3.1

try:
    x = 1 / 0
except ZeroDivisionError:
    pass

# task 3.2
try:
    result = 6 / "2"
except ValueError:
    pass

print("continue")

# task 3.3
import os.path
filename = input("Enter a filename: ")

if os.path.exists(filename):
    pass
else:
    print("file exists")
    
print("continue with file")

# task 4.1

weather = input("Enter the weather: sunny, rainy, or cold: ")
clothing = "sunglasses" if weather == "sunny" else "umbrella" if weather == "rainy" else "sweater"
print(clothing)

# task 4.2
weather = input("Enter the weather: sunny, rainy, or cold: ")
additional_clothing = "baseball cap" if weather == "sunny" else "boots" if weather == "rainy" else "bring a cardigan just in case"
print(additional_clothing)

# task 4.3
accessory = "sunscreen" if clothing == "sunglasses" else "raincoat" if clothing == "umbrella" else "sneakers"
print(accessory)


# task 5.1
import random

cpu_usage = random.randint(0, 100)
if cpu_usage > 90:
    print("High CPU usage!")
elif cpu_usage > 80 and cpu_usage <= 90:
    pass

# task 5.2

ram_usage = random.randint(0, 100)
disk_usage = random.randint(0, 100)
if ram_usage > 90:
    print("High Ram usage")
    if disk_usage > 90:
        print("Overloading")
    else:
        print("Check memory")
elif ram_usage <= 75:
    print("Normal ram usage")
    
# task 5.3 (using input from above)
if ram_usage > 90:
    print("High Ram usage")
    if disk_usage > 90:
        print("WARNING Overloading")
    else:
        print("Check memory")
elif ram_usage <= 75:
    print("gray zone")
    pass

print("all systems check")