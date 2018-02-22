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
B = network.createFactorNode("B")
E = network.createFactorNode("E")
A = network.createFactorNode("A")
J = network.createFactorNode("J")
M = network.createFactorNode("M")

'''
Add edges
'''
network.addEdge(B, burglary)
network.addEdge(E, earthquake)
network.addEdge(A, alarm, burglary, earthquake)
network.addEdge(J, johncalls, alarm)
network.addEdge(M, marycalls, alarm)

'''
# TestBed
'''
# for x in network.variable_nodes:
#     print x.name
#     for y in x.neighbours:
#         print y.name
#     print "\n"
#
# for x in network.factor_nodes:
#     print x.name
#     for y in x.neighbours:
#         print y.name
#     print "\n"
#
# for x in A.neighbours_map:
#     print x, A.neighbours_map[x]
#

network.runSumProduct()
