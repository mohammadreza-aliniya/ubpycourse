import csv
import time
timebefore=time.time()
u=0
q=0
c=0
j=0
i=0
k=0
v=0
z=0
r=0
llist=[]
avglist=[]
maxx=0
maxid=0
least=1000000000000
leastid=0
with open('E:\\python\\New folder\\instacart_2017_05_01\\order_products__prior.csv') as csvfile:
    readproductprior = csv.reader(csvfile)
    for row in readproductprior:
        if(i>1):
            m=int(row[1])
            llist.append(m)
            #c=c+1
            
           
        #if(c==10000):
         #   break
        i=i+1


with open('E:\\python\\New folder\\instacart_2017_05_01\\order_products__train.csv') as csvfile:
    readproducttrain = csv.reader(csvfile)
    for row in readproducttrain:
        if(u>1):
            m=int(row[1])
            llist.append(m)
            #v=v+1
            
           
        #if(v==10000):
         #   break
        u=i+1
      

    for j in llist:
        p=llist.count(llist[k])
        
        if(p>maxx):
            maxx=p
            maxid=llist[k]
        if(p<least):
            least=p
            leastid=llist[k]
        
        #k=k+1
        #if(k==10000):
         #   break


with open('E:\\python\\New folder\\instacart_2017_05_01\\products.csv') as csvfile:
    readproduct = csv.reader(csvfile)
    for row in readproduct:
        if(q>1):
            p=int(row[0])
            if(p==maxid):
               print("maximum sold product name:",row[1],"     id:",maxid,"     number:",maxx)
               break
        q=q+1
    q=0
    for row in readproduct:
        if(q>1):
            p=int(row[0])
            if(p==leastid):
               print("minimum sold product name:",row[1],"     id:",leastid,"     number:",least,"\n")
               break
        q=q+1

q=0

with open('E:\\python\\New folder\\instacart_2017_05_01\\orders.csv') as csvfile:
    readorders = csv.reader(csvfile)
    for row in readorders:
        if(q>1):
            m=int(row[5])
            avglist.append(m)
            
            
           
        q=q+1
        #if(q==100000):
         #   break

    avglist.sort()
 
    for row in avglist:
        
        r=avglist.count(z)
        r=float(r)
        hod=r/7
        hod=round(hod,2)
        print("avarage soled product per week in",z," o'oclock is: ",hod)
        z=z+1
        if(z==24):
            break




timeafter=time.time()
timet=timeafter-timebefore
print("\n","time of calculation:",timet)

            
    
    
    
        






