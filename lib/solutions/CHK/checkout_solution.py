

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    
    skus_list = list(skus)
    A = skus_list.count('A')
    B = skus_list.count('B')
    C = skus_list.count('C')
    D = skus_list.count('D')
    E = skus_list.count('E')
    F = skus_list.count('F')
    
    if (A+B+C+D+E+F != len(skus_list)):
        return -1
    else:
        B = B - (E//2)
        F = F - (F//2)
        if(B<0):
            B = 0
        
        return (((A//5)*200) + ((A%5)//3) * 130 + ((A%5)%3) * 50)+ ((B//2)*45+(B%2)*30) + C*20 + D*15 + E*40 + F * 10
    

