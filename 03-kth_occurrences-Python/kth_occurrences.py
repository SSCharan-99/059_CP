# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.



def fun_kth_occurrences(n, k):
    n=list(n)
    n.sort()
    
    dic={}
    for i in n:
        if i  in dic:
            dic[i]=dic[i]+1
        else:
            dic[i]=1
    
    res=[]

    ans=dict(sorted(dic.items(), key=lambda item: item[1]))
    li=[]

    for i,j in ans.items():
        li.append([i,j])
    return li[-k][0]

