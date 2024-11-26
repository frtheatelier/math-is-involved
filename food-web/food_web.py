"""
Data for food web
Based on: https://sl.bing.net/gPzuX4LXHRk
"""

from dataclasses import dataclass


@dataclass
class Beings:
    """Dataclass for animals.

    rel: producer/omnivore/herbivore/carnivore
    """
    id: int
    name: str
    rel: str
    apex: bool


@dataclass
class Question:
    """Dataclass for questions. Preconditions: self.conj in ["eats", "doesn't eat", "is"]"""
    animal_1: Beings
    animal_2: Beings
    conj: str


# THINGS (WRT The food web)
berries = Beings(1, "berries", "producer", False)
plantain = Beings(2, "plantain", "producer", False)
greenfly = Beings(3, "greenfly", "herbivore", False)
butterfly = Beings(4, "butterfly", "herbivore", False)
titmouse = Beings(5, "titmouse", "omnivore", False)
grasshopper = Beings(6, "grasshopper", "herbivore", False)
mouse = Beings(7, "mouse", "herbivore", False)
rabbit = Beings(8, "rabbit", "herbivore", False)
ladybird = Beings(9, "ladybird", "carnivore", False)
dragonfly = Beings(10, "dragonfly", "carnivore", False)
frog = Beings(11, "frog", "carnivore", False)
snake = Beings(12, "snake", "carnivore", False)
buzzard = Beings(13, "buzzard", "carnivore", True)
fox = Beings(14, "fox", "carnivore", True)


# MAP (prey: predator)
EATEN_BY = {
    "berries": ["grasshopper", "titmouse", "butterfly", "greenfly"],
    "plantain": ["grasshopper", "mouse", "rabbit"],
    "greenfly": ["ladybird"],
    "butterfly": ["frog"],
    "titmouse": ["snake", "buzzard", "fox"],
    "grasshopper": ["frog"],
    "mouse": ["buzzard", "fox"],
    "rabbit": ["buzzard", "fox"],
    "ladybird": ["titmouse", "dragonfly"],
    "dragonfly": ["frog"],
    "frog": ["snake"],
    "snake": ["buzzard"]
}

# QUESTIONS
QUESTIONS = {
    Question()
}
