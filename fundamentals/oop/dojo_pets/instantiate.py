from models import ninja, pet

ninja_data = {
    "first_name": "Grandma",
    "last_name": "Gumpers",
    "pet": {
        "name": "shelly",
        "type": "parrot",
        "tricks": "taunting",
        "health": 100,
        "energy": 100,
        "sound": "squawk"
    },
    "treats": "peanuts",
    "pet_food": "seeds"
}

ninja1 = ninja.Ninja( ninja_data )


print(ninja1.__dict__)
print(ninja1.pet.__dict__)

ninja1.walk().feed().bathe()

print(ninja1.pet.__dict__)
