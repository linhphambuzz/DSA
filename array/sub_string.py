'''
Given a string s, find the length of the longest 
substring
 without repeating characters.
e.g: s = "abcabcbb"  -> output=3 

'''
from heapq import heappop, heappush
def sub_string(given_string:str)->list: 
    q=list()
    pair=[(indx,s) for indx,s in enumerate(given_string)]
    for p in pair:
        heappush(q,p)
    sub=[]
    indx,s=0,given_string[0]
    ans=[]
    while q:
        n_indx,n_s=heappop(q)
        if (n_indx==indx+1 and n_s!=s and n_s not in sub) or len(sub)==0:
            sub.append(n_s)
            indx,s=n_indx,n_s
        else:
            ans.append(sub)
            sub=[n_s]
            indx,s=n_indx,n_s
        if not q and len(sub)!=0: ans.append(sub)
    return ans

#answer= max(len(sub) for sub in sub_string("abcabcbb"))
#print(answer)

# [97, 98, 100, 101, 116, 101, 98, 100]
s='abdetebd'
s2='abcabcbb'
def sstring(s:str)->int: 
    ss=[ord(i) for i in s]
    longest,idx=0,0
    while True:
        find,lfind,cnt=set(),0,0
        if idx+longest>=len(ss) or idx==len(ss)-1 : return longest
        debug=[]
        for s in ss[idx:]:
            find.add(s)
            if len(find)>lfind:cnt+=1; lfind=len(find)
            else: break
        longest=max(longest,cnt)
        idx+=1

assert sstring(s)==5 
assert sstring(s2)==3


    
            

        


        

