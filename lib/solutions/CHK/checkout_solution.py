

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    item_table = {
        'A':{
            "price":50,
            "calc": lambda v: (((v//5)*200) + ((v%5)//3) * 130 + ((v%5)%3) * 50)
        },
        'B':{
            "price":30,
            "calc": lambda v: ((v//2)*45+(v%2)*30) 
        },
        'C':{
            "price":20,
            "calc": lambda v: v*20
        },
        'D':{
            "price":15,
            "calc": lambda v: v*15
        },
        'E':{
            "price":40,
            "calc": lambda v: v*40
        },
        'F':{
            "price":10,
            "calc": lambda v: (v - (v//3)) * 10
        },
        'G':{
            "price":20,
            "calc": lambda v: v*20
        },
        'H':{
            "price":10,
            "calc": lambda v: (((v//10)*80) + ((v%10)//5) * 45 + ((v%10)%5) * 10)
        },
        'I':{
            "price":35,
            "calc": lambda v: v*35
        },
        'J':{
            "price":60,
            "calc": lambda v: v*60
        },
        'K':{
            "price":80,
            "calc": lambda v: ((v//2)*150+(v%2)*80) 
        },
        'L':{
            "price":90,
            "calc": lambda v: v*90
        },
        'M':{
            "price":15,
            "calc": lambda v: v*15
        },
        'N':{
            "price":15,
            "calc": lambda v: v*15
        },
        'O':{
            "price":15,
            "calc": lambda v: v*15
        },
        'P':{
            "price":15,
            "calc": lambda v: v*15
        },
        'Q':{
            "price":15,
            "calc": lambda v: v*15
        },
        'R':{
            "price":15,
            "calc": lambda v: v*15
        },
        'S':{
            "price":15,
            "calc": lambda v: v*15
        },
        'T':{
            "price":15,
            "calc": lambda v: v*15
        },
        'U':{
            "price":15,
            "calc": lambda v: v*15
        },
        'V':{
            "price":15,
            "calc": lambda v: v*15
        },
        'W':{
            "price":15,
            "calc": lambda v: v*15
        },
        'X':{
            "price":15,
            "calc": lambda v: v*15
        },
        'Y':{
            "price":15,
            "calc": lambda v: v*15
        },
        'Z':{
            "price":15,
            "calc": lambda v: v*15
        },
        
        
    }
    
    
    
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
            
        
        # B = B - (E//2)
        # F = F - (F//3)
        # if(B<0):
        #     B = 0
        
        # (B//2)*45+(B%2)*30) + C*20 + D*15 + E*40 + F * 10
    
checkout("ABDDEGREGHTHKYUGJHREYHYUK")

