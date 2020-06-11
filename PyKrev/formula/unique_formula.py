def unique_formula(*groups):
    
    """ 
	Docstring for function pyKrev.unique_formula
    
	====================
	This function compares n lists of molecular formula and outputs a dictionary containing the unique formula in each list.
    
	Use
	----
	unique_formula(list_1,..,list_n)
    
	Returns a dictionary in which each key corresponds to an input list (labelled "group 1...n") 
	and the corresponding value is a list containing the unique formula in that group.  
    
	Parameters
	----------
	*groups: n lists of molecular formula. Each item in the list should be a formula string. 
    
    """
    
    molecular_formula = dict()
    unique_molecular_formula = dict()
    
    #firstly read in all the groups 
    group_numbers = range(1,len(groups)+1)
    
    for i,g in zip(group_numbers,groups): 
        molecular_formula['group' + str(i)] = g 
    
    #now compare elements of the groups 
    for i in group_numbers:
        #create a shallow copy of the molecular formula dictionary 
        temp_molecular_formula = dict.copy(molecular_formula)
        #create a set out of the unique formulas in the current group 
        current_group = set(molecular_formula['group' + str(i)])
        #remove the current group from the shallow copy
        del temp_molecular_formula['group' + str(i)]
        #create a set out of the unique formulas in the shallow copy
        total = []
        temp_values = list(temp_molecular_formula.values())
        for f in temp_values:
            total += f #merge the sub lists
        other_groups = set(total)
        #compare current_group to the unique formulas in all other groups
        unique_formula  = []
        for formula in current_group:
            if formula in other_groups:
                pass
            else:
                unique_formula.append(formula)
        #add it to the unique_molecular_formula dict 
        unique_molecular_formula['group' + str(i)] = unique_formula
    
    
    return unique_molecular_formula