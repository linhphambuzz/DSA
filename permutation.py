''' 
given a list of letters, find all possible permutation aka replicate 
the permutation library in python itertools 
this is an implementation of simple Depth First Search 
with tree of each node being neighbor with the entire list but itself
'''
def shuffle(given_list): 
    tree=dict()
    length=len(given_list)
    for indx,l in enumerate(given_list):
        tree[l]=given_list[:indx]+given_list[indx+1:]
    
    def dfs(path,v,node):
        if node not in v and  node not in path: 
            v.add(node)
            path.append(node)
            if len(path)==length: print(path)

            for nb in tree[node]:
                dfs(path[:],v.copy(),nb) 

    for letter in given_list:
        dfs([],set(),letter)

if __name__=="__main__":
    shuffle(['a','b','c','d'])