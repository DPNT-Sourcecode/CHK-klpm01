

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    
    skus_list = list(skus)
    A = skus_list.count('A')
    B = skus_list.count('B')
    C = skus_list.count('C')
    D = skus_list.count('D')
    E = skus_list.count('E')
    if (A+B+C+D != len(skus_list)):
        return -1
    else:
        # return ((A//3)*130+(A%3)*50)+((B//2)*45+(B%2)*30)+C*20+D*15
        
    

