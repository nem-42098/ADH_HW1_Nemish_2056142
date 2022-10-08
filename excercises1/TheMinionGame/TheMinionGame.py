def minion_game(string):
    # your code goes here
    vow=['A','E','I','O','U']
    dic1={}
    dic2={}
    sum_c=0
    sum_v=0
    for j,i in enumerate(string):
        try:
            if vow.index(i)>=0:
                sum_v=sum_v+len(string)-j
        except:
            sum_c=sum_c+len(string)-j
    if sum_c>sum_v:
        print('Stuart'+' '+str(sum_c))
    elif sum_c==sum_v:
         print('Draw')
    else:
         print('Kevin'+' '+str(sum_v))   
    # for j,i in enumerate(string):

    #     for k in range(j+1,len(string)+1):
    #         try:                              ### starting case of vowel
    #             if vow.index(i)>=0:
    #                 sub_string=string[j:k]
                   
    #                 list_keys=list(dic2.keys())
    #                 try:
    #                     if list_keys.index(sub_string)>=0:
    #                         count=dic2[sub_string]
    #                         dic2[sub_string]=count+1
    #                         #print(dic2)
    #                 except:
    #                         #print('no index')
    #                         dic2[sub_string]=1
    #                         #print(dic2)
                    
                    
    #         except:                       
    #                 sub_string=string[j:k]
                   
    #                 list_keys=list(dic1.keys())
    #                 try:
    #                     if list_keys.index(sub_string)>=0:
    #                         count=dic1[sub_string]
    #                         dic1[sub_string]=count+1
    #                         #print(dic1)
    #                 except:
    #                         #print('no index')
    #                         dic1[sub_string]=1
    #                         #print(dic1)    
    
    # sum_c=0
    # print(dic1,dic2)
    # for i in dic1.keys():
    #     sum_c=sum_c+dic1[i]
    # sum_v=0
    # for i in dic2.keys():
    #     sum_v=sum_v+dic2[i]
    # if sum_c>sum_v:
    #     print('Stuart'+' '+str(sum_c))
    # elif sum_c==sum_v:
    #     print('Draw')
    # else:
    #     print('Kevin'+' '+str(sum_v))
                
            
    

