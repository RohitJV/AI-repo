from CPT import CPT

class FactorNode:
    def __init__(self, node_name):
        self.name = node_name
        self.neighbours = []
        self.no_of_neighbours = 0
        self.neighbours_map = {}
        
        self.conditionals = []

        # interaction parameters
        self.incoming = []
        self.incoming_temp = []
        self.outgoing = []

        self.incoming_cpt = {}        

    def setCPT(self, cpt_values):
        self.cpt = CPT(self.neighbours[0].name, self.neighbours[1:], cpt_values)

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

    def computeOutgoingCPT(self, idx):
        cpt_list = []
        for i in range(0,self.no_of_neighbours):
            if i==idx:
                continue
            partner_name = self.neighbours[i].name            
            current_cpt = self.incoming_cpt[partner_name]
            cpt_list.append(current_cpt)                
        resultant_cpt = self.cpt.factorMultiply(cpt_list)        
        outgoing_node_name = self.neighbours[idx].name
        summed_over_cpt = resultant_cpt.notSumOver(outgoing_node_name)        
        return summed_over_cpt

    def setIncomingCPT(self, neighbour_name, cpt):
        self.incoming_cpt[neighbour_name] = cpt