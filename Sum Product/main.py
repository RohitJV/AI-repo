from BayesNet import BayesNet

network = BayesNet(5);

'''
Initialize the variable nodes
'''
burglary = network.createVariableNode("burglary")
earthquake = network.createVariableNode("earthquake")
alarm = network.createVariableNode("alarm")
johncalls = network.createVariableNode("johncalls")
marycalls = network.createVariableNode("marycalls")

'''
Create factor nodes
'''
B = network.createFactorNode("B", [burglary], [0.001])
E = network.createFactorNode("E", [earthquake], [0.002])
A = network.createFactorNode("A", [alarm, burglary, earthquake], [0.95, 0.94, 0.29, 0.001])
J = network.createFactorNode("J", [johncalls, alarm], [0.90, 0.05])
M = network.createFactorNode("M", [marycalls, alarm], [0.70, 0.01])

'''
# TestBed
'''
# for x in network.variable_nodes:
#     print(x.name)
#     for y in x.neighbours:
#         print(y.name)
#     print("\n")

# for x in network.factor_nodes:
#     print("Factor : ",x.name, x.cpt.conditionals_length)
#     for y in x.cpt.conditionals:
#     	print("Conditionals : ",y.name)
#     for y in x.neighbours:
#         print("Variable Neighbour : ",y.name)
#     print("\n")
#
# for x in A.neighbours_map:
#     print(x, A.neighbours_map[x])
#

network.runSumProduct()
