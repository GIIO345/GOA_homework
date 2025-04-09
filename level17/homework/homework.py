#შექმენით manul_remove ფუნქცია

listd=[2,3,43,432,3,4.3,3,3,3,3,3,3,]
res=[]
def func(listd,number):
    for i in listd:
        if i!=number:
            res.append(i)
    return res
print(func(listd,3))



#შექმენით manual_index ფუნქცია

listf=[2,3,4,54,7,5,243,]
def man_index(listf,num):
    count=0
    for i in listf:
        count+=1
        if num==i:
            res=count-1
    return res
print(man_index(listf,3))
            
            
#შექმენით manual_len ფუნქცია
listk=[32,32,34,2,42,432,]
def man_len(listk):
    count=0
    for i in listk:
        count+=1
    return count
print(man_len(listk))


#შექმენით manual_pop ფუნქცია
listg=[32,4,3,2,432,3,24332,54,3,64]
def man_pop(listg,item):
    for i in listg:
        if i==item:
            listg.remove(item)
            break
    return listg
print(man_pop(listg,3))



 
#შექმენით manual_reverse ფუნქცია
listr=[2,35,3454,2,3,54,21,2,55,4,76,5,]
def man_reverse(listr):
    result=listr[::-1]
    return result

print(man_reverse(listr))