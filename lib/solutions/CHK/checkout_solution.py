

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # Items = {'A':0 ,'B':0,'C':0,'D':0}
    # for item in skus:
    #     if i == 'A':
    #         Items['A']
    skus = skus.upper()
    skus_list = list(skus)
    A = skus_list.count('A')
    B = skus_list.count('B')
    C = skus_list.count('C')
    D = skus_list.count('D')
    if (A+B+C+D != len(skus_list)):
        return -1
    else:
        return ((A//3)*130+(A%3)*50)+((B//2)*45+(A%2)*30)+C*20+D*15
    
    
