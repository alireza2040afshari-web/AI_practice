import numpy as np
import matplotlib.pylab as plt


#x = np.random.normal(3 , 0.1 ,100)
#y = np.random.normal(5 , 0.1 ,100)


#plt.scatter(x, y)
#plt.axis([0, 10, 0, 12])
#plt.show()


#a = np.random.randint(10 , 50 ,(17,12))
#a = a.ndim
#print(a)
#a = np.arange(1, 13)
#a = a.reshape((3, 4))
#print(a)
#first_array = np.random.randint(1, 100 , (3,2))
#second_array = np.random.randint(1, 7 , (3,2))
#print(first_array , "*\n" , second_array)
#third_array = np.concatenate([first_array,second_array] , axis= 1)
#print(third_array)

#1
#final_mark_calculator

midterm = np.array([14, 18, 12, 16, 10])
final   = np.array([15, 17, 14, 18, 13])
homework = np.array([20, 15, 18, 17, 16])

def total_mark(first,socond,third):
    
    total = np.concatenate([first,socond,third],axis=0)
    for number in total:

    
print(total_mark(midterm,final,homework))