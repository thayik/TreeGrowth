import numpy as np
from typing import Dict, Set, Tuple

# Global Variables / easily changable
STEMSEEDSCALE = 0.1
BUDGROWTHANGLE = (30, 90)
CURRENTSTEP = 0
GROWTHPERTS = 0.01
NUM_BRANCHES = 0
BUD_RADIUS = 0.1
NODEID = 0
SEEDUP = [0,0,1]
ENERGYCONSUMPTION = 0.1

# Generates numbered IDs for every node
def generateID():
    resp = f"node_{NODEID}"
    NODEID += 1
    return resp

# The nodes
class SplineNode:
    def __init__(self, location: np.array, radius: float, angle) -> None:
        self.id = generateID()
        self.location = location
        self.radius = radius
        self.angle = angle
        self.connectedNode = False
        self.neededEnergy = ENERGYCONSUMPTION

    def connectNode(self) -> bool:
        self.connectedNode = True
    
    def __str__(self):
        return f"{self.location} {self.radius} {self.angle}"

# During bud stage, the buds need activation energy which they give to a new apical meristem.
# When activated, they create a new AM and a new branch, connecting it to the node it came out of.
class BudStage:
    def __init__(self, connectedSpline: SplineNode, angle) -> None:
        self.connectedSpline = connectedSpline
        self.angle = angle

    def transitionBud():
        pass

# The growth of the tip of each branch. With every iteration, I think it should take energy to create new "grow cells"
class ShootApicalMeristem:
    def __init__(self, location: np.array, nutrients: float) -> None:
        self.location = location
        self.nutrients = nutrients

    def collectNutrients(self):
        pass

# The growth of the tip of each root. With every iteration, I think it should take energy to create new "grow cells"
class RootApicalMeristem:
    def __init__(self, location: np.array, waterLevel: float) -> None:
        self.location = location
        self.waterLevel = waterLevel

    def collectNutrients(self):
        pass

# This is where individual nodes become branches, many Nodes with a base, a head, and the buds (maybe no buds?)
class BranchSpline:
    def __init__(self, head: ShootApicalMeristem) -> None:
        self.head = head
        self.base = SplineNode(head.location, BUD_RADIUS)
        self.spline = [].append(self.base)
        self.branches = []
        self.buds = []

    def add_branch(self, splineNode: SplineNode):
        self.branches.append(splineNode)

    def add_splineNode(self, splineNode: SplineNode):
        self.spline.append(splineNode)

    def add_bud(self, bud: BudStage):
        self.buds.append(bud)

    # def add_spline(self, location, radius):
    #     spline = SplineNode(location, radius)
    #     self.spline.append(spline)

    def __str__(self):
        resp = "Spline:\n"
        for i,s in enumerate(self.spline):
            resp += f"{i} {str(s)}\n"
        return resp
    
# Initially the seed, it starts the growth, with an initial storage of nutrients inside the seed being used for energy.
# This might be where the timesteps are done? not sure
class RootBall:
    def __init__(self, location, nutrients, radius):
        self.location = location
        self.nutrients = nutrients
        self.radius = radius

    def beginGrowth(self) -> Tuple[ShootApicalMeristem, RootApicalMeristem]:
        seedDirection = SEEDUP * self.radius
        shootMeristem = ShootApicalMeristem(self.location + seedDirection)
        rootMeristem = RootApicalMeristem(self.location - seedDirection)
        return shootMeristem, rootMeristem
    
    def growRootBall(self, amt) -> float:
        self.radius += amt
        return self.radius
    
    def upgradeFromSeed(self):
        pass

    def __str__(self):
        return f"Seed: {self.location} {self.nutrients} {self.radius}"

