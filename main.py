#Game of Game Theory: NEA Coursework. 
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

#This function retrieves a particular feature from a scenario
def ScenarioSplitter(someScenarios,fieldName):
    indexDictionary = {"scenarioNumber":0,"scenarioText":1,"ChoiceA":2,"ChoiceB":3,"ChoiceC":4,"ChoiceD":5,"Payoff1":6,"Payoff2":7,"Payoff3":8,"Payoff4":9,"Payoff5":10,"Payoff6":11,"Payoff7":12,"Payoff8":13}
    index = indexDictionary.get(fieldName)
    RandomScenario = random.randint(1,26)
    someScenario = someScenarios[RandomScenario].split(",")  
    return someScenario[index]

#Tests for ScenarioSplitter
#print(ScenarioSplitter(InvisibleHandScenarios,"scenarioNumber"))
#print(ScenarioSplitter(InvisibleHandScenarios,"scenarioText"))
#print(ScenarioSplitter(InvisibleHandScenarios,"ChoiceB"))
