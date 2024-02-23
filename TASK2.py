from array import *
def f_calc_cos(a,b):
   #print (a)
   #print (b)
    
    N=len(a);
   
    T=0
    AA=0
    BB=0
    
    for i in range(N):
        try :
            T=T+a[i]*b[i]
            AA=AA+a[i]**2
            BB=BB+b[i]**2
        except:
            print('Массивы разной длинны!!!')
        i += 1
    AA=AA**(1/2)
    BB=BB**(1/2)
    REZ=T/(AA*BB)

    print (REZ)
    
    
f_calc_cos([3,5,6,0],[3,5,6,0])
    