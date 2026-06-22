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
    result = np.column_stack((midterm, final, homework))
    return(result)

def definer(total = np.array([])):
    name_list = ["ali","mamad","hasan","reza","amir"]
    mark_list = {}
    index = 0
    for name in name_list:
        mark_list[name] = total[index]
        index + 1
    return mark_list
    
def claculator(mark_list = {},choose = ""):
    index = 0
    match choose:
        case "midterm":
            factor = 0.3
        case "final":
            factor = 0.5
        case "homework":
            factor = 0.2

    for key in mark_list:
        mark_list[key] = mark_list[key][index] * 0.3
        value = value[index] * factor
    return(mark_list)
          

total = total_mark(midterm,final,homework)
print(total)
print(definer(total))
print(claculator(definer(total)))