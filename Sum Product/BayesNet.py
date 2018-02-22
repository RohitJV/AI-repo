from FactorNode import FactorNode
from VariableNode import VariableNode

class BayesNet:
    def __init__(self, num_of_nodes):
        self.num_of_nodes = num_of_nodes
        self.variable_nodes = []
        self.factor_nodes = []
        self.variable_nodes_map = {}
        self.factor_nodes_map = {}

    def createVariableNode(self, name):
        newNode = VariableNode(name)
        self.variable_nodes_map[name] = newNode
        self.variable_nodes.append(newNode)
        return newNode

    def createFactorNode(self, name):
        newNode = FactorNode(name)
        self.factor_nodes_map[name] = newNode
        self.factor_nodes.append(newNode)
        return newNode

    def addEdge(self, factor_node, *variable_nodes):
        for x in variable_nodes:
            factor_node.addNeighbour(x)
            x.addNeighbour(factor_node)

    def initializeNodeVariables(self):
        for x in self.variable_nodes:
            x.incoming = [False] * x.no_of_neighbours
            x.outgoing = [False] * x.no_of_neighbours
            x.incoming_temp = [False] * x.no_of_neighbours
        for x in self.factor_nodes:
            x.incoming = [False] * x.no_of_neighbours
            x.outgoing = [False] * x.no_of_neighbours
            x.incoming_temp = [False] * x.no_of_neighbours

    def passMessagesVariableNode(self, node):
        for idx in range(0,node.no_of_neighbours):
            '''
            Check here if we need and can pass a masseage to the current neighbour 'idx'
            '''
            if node.checkReadiness(idx):
                node.outgoing[idx] = True
                partner_node_name = node.neighbours[idx].name
                print node.name, partner_node_name
                partner_node = self.factor_nodes_map[partner_node_name]
                partner_node.setIncomingMessage(node.name)

    def passMessagesFactorNode(self, node):
        for idx in range(0,node.no_of_neighbours):
            '''
            Check here if we need and can pass a masseage to the current neighbour 'idx'
            '''
            if node.checkReadiness(idx):
                node.outgoing[idx] = True
                partner_node_name = node.neighbours[idx].name
                print node.name, partner_node_name
                partner_node = self.variable_nodes_map[partner_node_name]
                partner_node.setIncomingMessage(node.name)

    def runSumProduct(self):
        print self.num_of_nodes
        no_of_iterations = self.num_of_nodes

        self.initializeNodeVariables();

        for iter in range(0, no_of_iterations):
            print "iteration : ", iter

            '''
            iterate through variable nodes
            '''
            for x in self.variable_nodes:
                self.passMessagesVariableNode(x)

            print ""

            '''
            iterate through variable nodes
            '''
            for x in self.factor_nodes:
                self.passMessagesFactorNode(x)

            print "***"

            for x in self.variable_nodes:
                x.updateIncomingFlags()
            for x in self.factor_nodes:
                x.updateIncomingFlags()
