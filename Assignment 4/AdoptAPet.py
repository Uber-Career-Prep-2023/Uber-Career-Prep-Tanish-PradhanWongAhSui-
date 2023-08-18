# Technique: Maintain two queues
# Time complexity: O(1) for each adoption, O(1) for each addition of pet
# Space complexity: O(n), where n is the number of pets

from collections import deque

class AnimalShelter:
    def __init__(self, animals):
        self.dogs = deque()
        self.cats = deque()
        for animal in animals:
            if animal[1] == "dog":
                self.dogs.append(animal)
            else:
                self.cats.append(animal)
    
    def adopt(self, person, preference):
        if preference == "dog":
            if self.dogs:
                return self.dogs.popleft()[:2]
            elif self.cats:
                return self.cats.popleft()[:2]
        else:
            if self.cats:
                return self.cats.popleft()[:2]
            elif self.dogs:
                return self.dogs.popleft()[:2]
        return None

    def add(self, name, species, days):
        if species == "dog":
            self.dogs.append((name, species, days))
        else:
            self.cats.append((name, species, days))

shelter = AnimalShelter([
    ("Sadie", "dog", "4 days"),
    ("Woof", "cat", "7 days"),
    ("Chirpy", "dog", "2 days"),
    ("Lola", "dog", "1 day")
])

assert shelter.adopt("Bob", "dog") == ("Sadie", "dog")
shelter.add("Floofy", "cat", "1 day")
assert shelter.adopt("Sally", "cat") == ("Woof", "cat")
assert shelter.adopt("Ji", "cat") == ("Floofy", "cat")
assert shelter.adopt("Ali", "cat") == ("Chirpy", "dog")

shelter2 = AnimalShelter([("Luna", "cat", "5 days"), ("Bella", "cat", "6 days")])
assert shelter2.adopt("John", "dog") == ("Luna", "cat")
assert shelter2.adopt("Jane", "dog") == ("Bella", "cat")

empty_shelter = AnimalShelter([])
assert empty_shelter.adopt("Emma", "dog") is None

shelter3 = AnimalShelter([])
shelter3.add("Simba", "cat", "2 days")
shelter3.add("Leo", "dog", "3 days")
assert shelter3.adopt("Paul", "cat") == ("Simba", "cat")
assert shelter3.adopt("Ruth", "dog") == ("Leo", "dog")

shelter4 = AnimalShelter([("Coco", "dog", "7 days"), ("Max", "dog", "3 days")])
assert shelter4.adopt("Eve", "cat") == ("Coco", "dog")
assert shelter4.adopt("Adam", "dog") == ("Max", "dog")

# Approximate time taken: 35 minutes.