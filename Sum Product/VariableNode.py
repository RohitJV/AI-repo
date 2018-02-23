from CPT import CPT

class VariableNode:
    def __init__(self, node_name):
        self.name = node_name
        self.neighbours = []
        self.no_of_neighbours = 0
        self.neighbours_map = {}

        # interaction parameters
        self.incoming = []
        self.incoming_temp = []
        self.outgoing = []

        self.incoming_cpt = {}        

    def addNeighbour(self, factor_node):
        self.neighbours.append(factor_node)
        neighbour_idx = self.no_of_neighbours
        self.neighbours_map[factor_node.name] = neighbour_idx
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

    '''
    All incoming CPTs are factors as a function of only one variable
    Outgoing CPT should also be a factor of the same variable
    So, the factor/CPT has only 1 entry
    '''
    def computeOutgoingCPT(self, idx):
        prob = 1.0
        for i in range(0,self.no_of_neighbours):
            if i==idx:
                continue
            partner_name = self.neighbours[i].name
            current_cpt = self.incoming_cpt[partner_name]
            if current_cpt.is_unity_cpt:
                continue
            if (current_cpt.node_name != self.name) or (current_cpt.conditionals_length != 0):
                print("Kuch toh jhol he")
                break
            prob = prob * current_cpt.cpt_values[0]
        outgoing_neighbour_name = self.neighbours[idx].neighbours[0].name
        return_cpt = CPT(self.name, [], [prob])        
        return return_cpt

    def setIncomingCPT(self, neighbour_name, cpt):
        self.incoming_cpt[neighbour_name] = cpt
