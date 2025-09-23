import random

InvisibleHandFile = open("InvisibleHand.csv","r")
InvisibleHandScenarios = InvisibleHandFile.readlines() #Holds the scenarios for the Invisible Hand Games.
InvisibleHandFile.close()

PrisonersDilemmaFile = open("PrisonersDilemma.csv")
PrisonersDilemmaScenarios = PrisonersDilemmaFile.readlines() #Holds the scenarios for the Prisoners' Dilemma Games.
PrisonersDilemmaFile.close()

PNEquilibriumFile = open("PureNashEquilibrium.csv")
PureNashScenarios = PNEquilibriumFile.readlines() #Holds the scenarios for Pure Nash Equilibria Games.
PNEquilibriumFile.close()

MNEquilibriumFile = open("MixedNashEquilibrium.csv")
MixedNashScenarios = MNEquilibriumFile.readlines() #Holds the scenarios for Mixed Nash Equilibria Games. 
MNEquilibriumFile.close()

#Extracting data from the Invisible Hand Scenario

RandomScenario = random.randint(1,25)
