def insert_dict(query, dict):
    dict[query[1]] = int(query[2])

# deleting from dictionary
def del_dict(query, dict):
    if query[1] in dict:
        del dict[query[1]]
        return True
    return False
    
    

# print marks of required name
def print_dict(key, dict):
    flag = False
    if(key in dict):
        flag = True
        print ("Marks of " + key + " is "+ str(dict[key]))
        
    return True if flag is True else False



