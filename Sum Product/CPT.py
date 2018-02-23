import copy

class CPT:
	def __init__(self, node_name, conditionals, cpt_values):
		self.is_unity_cpt = False
		self.node_name = node_name
		self.conditionals = conditionals
		self.conditionals_length = len(conditionals)
		self.cpt_values = cpt_values
		self.cond_var_to_index_map = {}
		for i in range(0,self.conditionals_length):
			self.cond_var_to_index_map[conditionals[i].name] = i

	def createUnityCPT(self):
		self.is_unity_cpt = True
		self.cpt_values = [1.0]

	def factorMultiply(self, cpt_list):
		resultant_cpt = copy.deepcopy(self)
		for cpt in cpt_list:
			'''
			All incoming CPTs must be factors with functions of just 1 variable - sanity check that
			'''
			if cpt.conditionals_length!=0:
				print("Kuch toh jhol he")
				break	

			'''
			If the CPT has non-evidence variable same as the current factor's non evidence
			'''			
			if cpt.node_name==self.node_name:
				for i in range(0, len(self.cpt_values)):
					resultant_cpt.cpt_values[i] = resultant_cpt.cpt_values[i] * cpt.cpt_values[0]
			else:
				col_idx = self.cond_var_to_index_map[cpt.node_name]				
				mask = 1<<(self.conditionals_length - col_idx - 1);				
				for i in range(0, len(self.cpt_values)):
					if (mask & i):
						resultant_cpt.cpt_values[i] = resultant_cpt.cpt_values[i] * (1-cpt.cpt_values[0])
					else:
						resultant_cpt.cpt_values[i] = resultant_cpt.cpt_values[i] * cpt.cpt_values[0]
		return resultant_cpt

	def notSumOver(self, outgoing_node_name):
		return_cpt = CPT(outgoing_node_name, [], [])
		'''
		If it is not not-summed over the non-evidence variable, return "unity_cpt"
		'''		
		if outgoing_node_name != self.node_name:
			return_cpt.createUnityCPT()
			return return_cpt
		resultant_prob = 0.0
		for x in self.cpt_values:
			resultant_prob = resultant_prob + x
		return_cpt.cpt_values.append(resultant_prob)
		return return_cpt

	def printCPT(self):
		print("CPT values on non-evidence variable : ", self.node_name)
		for x in self.cpt_values:
			print(x)