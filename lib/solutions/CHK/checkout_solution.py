

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sumItems = 0
    items = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    item_count = list()
    skus_list = list(skus)
    for i in items:
        item_count.append((i,skus_list.count(i)))
        sumItems+=skus_list.count(i)
    if (sumItems != len(skus_list)):
        return -1
    else:
        sumTotal = 0
        for item, count in item_count:
            print(item," ", count)
        
        # B = B - (E//2)
        # F = F - (F//3)
        # if(B<0):
        #     B = 0
        
        # return (((A//5)*200) + ((A%5)//3) * 130 + ((A%5)%3) * 50)+ ((B//2)*45+(B%2)*30) + C*20 + D*15 + E*40 + F * 10
    
checkout("ABDDEGREGHTHKYUGJHREYHYUK")
