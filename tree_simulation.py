from tree_classes import *


# Changable starting parameters
STARTING_NUTRIENTS = 100
SEED_RADIUS = 2
LENGTH_GROWTH = 0.01
DIAMETER_GROWTH = 0.01
MAX_HEIGHT = 100
ORIGIN = [0, 0, 0]
SOILWATER = 100
NEWNODER = 0.01

# Calculates the nutrients needed for basic survival of all "nodes"
def nutrients_needed():
    pass

def calcEnvVector():
    pass

# Get currrent directional vector using L2-L1, then normalize, then generate growth vector by adding and normalizing again
def calculateNextMeristem(apicalMeristem: ShootApicalMeristem, previousNode: SplineNode, envVector: np.array) -> ShootApicalMeristem:
    pointDiff = apicalMeristem.location - previousNode.location
    mag = np.linalg.norm(pointDiff)
    direction = pointDiff / mag

    combined_vector = direction + envVector

    magnitude = np.linalg.norm(combined_vector)
    normalized_combined_vector = combined_vector / magnitude

    shootMeristem = shootMeristem(apicalMeristem.location + normalized_combined_vector)
    return shootMeristem


# creates a bud and adds it to the list, also changing current Node.connectedNode to True
def create_bud(meristem) -> BudStage:
    return BudStage(meristem)

# Go through the leaves, and add up the nutrients collected during that cycle
def collect_above_nutrients():
    pass

# Go through the roots, and add up water and soil nutrients collected during that cycle
def collect_below_nutrients():
    pass

# Go through all the leaves and calculate how much energy they all need.
def needed_Nutrients(branch: BranchSpline):
    pass

# using the nutrients above and below, use some algorithm and calculate how much energy is created
def calculate_Nutrients(shootNutrients, rootNutrients):
    pass

# Grow radius of all nodes, making sure they do not intertouch
def WidenSpreadBranches(): 
    pass

# Takes in the main branch and recursively writes the data to a file
def ExportSim():
    pass

def main():
    seedLocation = np.array(ORIGIN)
    starting_seed = RootBall(seedLocation, STARTING_NUTRIENTS, SEED_RADIUS)
    shootMeristem, rootMeristem = starting_seed.beginGrowth()
    pointDiff = shootMeristem.location - starting_seed.location
    mag = np.linalg.norm(pointDiff)
    direction = pointDiff / mag
    previousNode = SplineNode(shootMeristem.location, NEWNODER, direction)
    mainBranch = BranchSpline(previousNode)
    all_buds = []
    while True:
        shootNutrients = collect_above_nutrients() # shootMeristem.collectNutrients()
        rootNutrients = collect_below_nutrients() # rootMeristem.collectNutrients()
        neededNuts = needed_Nutrients(mainBranch)
        nuts = calculate_Nutrients(shootNutrients, rootNutrients)
        WidenSpreadBranches(mainBranch)
        growthVector = calculateGrowthVector()
        if nuts > neededNuts:
            all_buds.append(create_bud(shootMeristem))



if __name__ == "__main__":
    main()
