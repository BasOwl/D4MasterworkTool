
def get_current_stage():
    #get stage
    current_stage = input("Input Current Stage 0 - 12: ")
    return int(current_stage)

def get_wanted_stage():   
    #select stage
    wanted_stage = input("Input Desired Stage 0 - 12: ")
    return int(wanted_stage)
    
def forge_cost_table(stage):
    #stage lists 1, 2 or 3 ELSE full list
    data_stage_full = (0, 10, 20, 30, 40, 20, 40, 80, 120, 50, 100, 150, 250)
    data_stage_1 = (data_stage_full[slice(1,5)])
    data_stage_2 = (data_stage_full[slice(6,9)])
    data_stage_3 = (data_stage_full[slice(9,13)])
    
    if stage not in [1,2,3]:
        return data_stage_full 
    if stage == 1:
        return data_stage_1
    if stage == 2:
        return data_stage_2
    if stage == 3:
        return data_stage_3
        

def forge_cost_current(current):
    #
    table = forge_cost_table(0)    
    res = table[current]
    return res

def material_check(stage):
    #0 is error 
    material = 0
    if stage in [1,2,3,4]:
        material = 1
    if stage in [5,6,7,8]:
        material = 2
    if stage in [9,10,11,12]:
        material = 3
    return material

def forge_cost_TO_current(current, wanted):
    #if 1-4 obucite if 5-8 ingolith if 9-12 neathiron
    
    #if index is 4 and below obu, also check if current / desired is in 1 2 or 3
    table = forge_cost_table(0)
    current_cost = forge_cost_current(current)
    current_index = table.index(current_cost)
    wanted_cost = forge_cost_current(wanted)
    wanted_index = (table.index(wanted_cost))
    if wanted_index == current_index:
        wanted_index = table.index(wanted_cost, current_index +1)
    obucite_cost = 0
    ingolith_cost = 0
    neathiron_cost = 0
    
    stage_length = 4 #should be 4
    stage_lengthx2 = 8 #should be 8
    stage_length_total = 12 #should be 12
    
    #off by 1 bs
   
    index = current_index +1
    
    #print(f"index set to: {index}")
    
    #(0, 10, 20, 30, 40,||20, 40, 80, 120,||50, 100, 150, 250)
    #(0   1   2   3   4 ||5   6   7    8  || 9    10   11   12)
    
    #obucite
    while index <= stage_length and index < wanted_index:
        obucite_cost = obucite_cost + table[index]
        #print(f"obu: {index}")
        index += 1
    
    #ingolith      
    while index > stage_length and index <= stage_lengthx2 and index <= wanted_index:
        ingolith_cost = ingolith_cost + table[index]
        #print(f"ingo: {index}")
        index += 1
        
    #neathiron     
    while index >= (stage_lengthx2) and index <= wanted_index:
        neathiron_cost = neathiron_cost + table[index]
        #print(f"neath: {index}")
        index += 1
        
         
    print("Total Costs to Desired Stage: ")
    print(f"Obucite cost: {obucite_cost}")
    print(f"Ingolith cost: {ingolith_cost}")
    print(f"Neathiron cost: {neathiron_cost}")
    
    
    
        
def main():
    
    #get current and wanted and table
    current_stage = get_current_stage()
    wanted_stage = get_wanted_stage()
    
    #current stage and cost
    forge_cost_current(current_stage)
    
    #display costs to selected stage

    res = forge_cost_TO_current(current_stage, wanted_stage)
    if res == -1:
        print(f"Error: Input is out of range. 0 - 12 are valid. ")
    
    
    
    
    
if __name__ == '__main__':
    main()
        