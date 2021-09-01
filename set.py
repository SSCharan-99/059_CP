# limitedPowerSet(n, k)
# Write a function limitedPowerSets(n, k) that takes possibly 
# a non-negative integer n and k and returns the list that 
# contains k number of subsets from the power set as sets. 
# (The values in the set will range from 1 to n).
# Example:
# 	limitedPowerSet(5, 7) => 
# [ {}, {1}, {2}, {3}, {4}, {5}, {1, 2} ]

def limitedPowerSet(n, k):
    # Your code goes here...
    list=[]
    count=0
    list.append({})
    count+=1
    for j in range(1,n+1):
        #L=set()
        list.append({j})
        count+=1
        if(count>=k):
                return list
    
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            list.append({i,j})
            count+=1
            if(count>=k):
                return list
     
    
        
print(limitedPowerSet(5,10))