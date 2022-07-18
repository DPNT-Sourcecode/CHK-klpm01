

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
            "price":70,
            "calc": lambda v: ((v//2)*120+(v%2)*70) 
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
            "price":40,
            "calc": lambda v: v*40
        },
        'O':{
            "price":10,
            "calc": lambda v: v*10
        },
        'P':{
            "price":50,
            "calc": lambda v: ((v//5)*200+(v%5)*50) 
        },
        'Q':{
            "price":30,
            "calc": lambda v: ((v//3)*80+(v%3)*30) 
        },
        'R':{
            "price":50,
            "calc": lambda v: v*50
        },
        'S':{
            "price":20,
            "calc": lambda v: v*20
        },
        'T':{
            "price":20,
            "calc": lambda v: v*20
        },
        'U':{
            "price":40,
            "calc": lambda v: (v - (v//4)) * 40
        },
        'V':{
            "price":50,
            "calc": lambda v: (((v//3)*130) + ((v%3)//2) * 90 + ((v%3)%2) * 50)
        },
        'W':{
            "price":20,
            "calc": lambda v: v*20
        },
        'X':{
            "price":17,
            "calc": lambda v: v*17
        },
        'Y':{
            "price":20,
            "calc": lambda v: v*20
        },
        'Z':{
            "price":21,
            "calc": lambda v: v*21
        },
        'Promo1':{
            'price': 45,
            'calc': lambda v: v*45
        }
        
    }
    sumItems = 0
    items = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    item_count = dict()
    skus_list = list(skus)
    for i in items:
        if i not in item_count.keys():
            item_count[i] = skus_list.count(i)
            sumItems+=skus_list.count(i)
    
    if (sumItems != len(skus_list)):
        return -1
    else:
        sumTotal = 0
        
        for item in item_count.keys():
            if item=='E':
                item_count['B'] = item_count['B'] - (item_count['E']//2)
                if(item_count['B']<0):
                    item_count['B'] = 0
            if item=='N':
                item_count['M'] = item_count['M'] - (item_count['N']//3)
                if(item_count['M']<0):
                    item_count['M'] = 0
            if item=='R':
                item_count['Q'] = item_count['Q'] - (item_count['R']//3)
                if(item_count['Q']<0):
                    item_count['Q'] = 0
            
            # new group promotion
            s = item_count['S'] + item_count['T'] + item_count['X'] +item_count['Y'] +item_count['Z']
            if s>=3:
                sumTotal += item_table['Promo1']['calc'](s//3)
                while s>=3 and item_count['Z']!=0: 
                    s-=1
                    item_count['Z']-=1
                    print("Z",s,item_count['Z'])                 
                while s>=3 and item_count['S']!=0: 
                    s-=1
                    item_count['S']-=1
                    print("S",s,item_count['S'])                 
                    
                if item_count['T']>0 and s>=3: 
                    s-=item_count['T']
                    item_count['T']=s%3
                
                if item_count['Y']>0 and s>=3: 
                    s-=item_count['Y']
                    item_count['Y']=s%3
                
                if item_count['X']>0 and s>=3: 
                    s-=item_count['X']
                    item_count['X']=s%3
                                
        for item in item_count.keys():
            sumTotal+= item_table[item]['calc'](item_count[item])

        return sumTotal
    
print(checkout('SSSZ'))