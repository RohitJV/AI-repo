class FactorNode:
    def __init__(self, node_name):
        self.name = node_name
        self.neighbours = []
        self.no_of_neighbours = 0
        self.neighbours_map = {}

        # headache is coming
        self.conditionals = []
        self.cpt = [];

        # interaction parameters
        self.incoming = []
        self.incoming_temp = []
        self.outgoing = []

        self.incoming_cpt = []
        self.outgoing_cpt = []

    def addNeighbour(self, variable_node):
        self.neighbours.append(variable_node)
        neighbour_idx = self.no_of_neighbours
        self.neighbours_map[variable_node.name] = neighbour_idx
        self.no_of_neighbours = self.no_of_neighbours + 1

    def checkForIncomingMessages(self, idx):
        ready = True
        for i in range(0,self.no_of_neighbours):
            if i==idx:
                continue
            ready = ready & self.incoming[i]
        return ready

    def checkReadiness(self, neighbour_id):
        if self.outgoing[neighbour_id]==False:
            return self.checkForIncomingMessages(neighbour_id)
        return False

    def setIncomingMessage(self, id):
        idx = self.neighbours_map[id]
        self.incoming_temp[idx] = True

    def updateIncomingFlags(self):
        for i in range(0, self.no_of_neighbours):
            self.incoming[i] = self.incoming_temp[i]
