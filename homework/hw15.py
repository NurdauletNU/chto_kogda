# Пузырьковая сортиовка      clear time 0.00125s
import time


data=[329, 203, 325, 717, 211, 444, 66, 738, 86, 729, 729, 557, 318, 285, 14, 898, 870, 341, 827, 6, 355, 741, 820, 408, 679, 211, 957, 570, 182, 725, 114, 109, 544, 725, 855, 992, 499, 715, 389, 205, 410, 678, 356, 248, 444, 487, 977, 551, 106, 373, 247, 167, 444, 958, 234, 53, 771, 684, 933, 440, 696, 685, 37, 426, 297, 748, 919, 929, 850, 964, 621, 498, 968, 796, 746, 178, 957, 642, 876, 108, 184, 607, 178, 647, 558, 180, 296, 26, 172, 139, 193, 358, 709, 866, 17, 754, 843, 196, 317, 446]

def time_measure(func):
    def wrapper(*args,**kwargs):
        time_st=time.perf_counter()
        res=func(*args,**kwargs)
        time_end=time.perf_counter()
        print(round(time_end-time_st, 5))
        return res
    return wrapper





@time_measure
def bubble_sotr(array):
    for i in range(1,len(array)-1):
        for j in range(0,len(array)-i):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return array

# print(bubble_sotr(data))




# Сортировка выборам            clear time 0.00093s
@time_measure
def selection_sort(array):
    for i in range(len(array)-1):
        min_idx = i
        for idx in range(i + 1, len(array)-1):
            if array[idx] < array[min_idx]:
                min_idx = idx
        array[i], array[min_idx] = array[min_idx], array[i]
    return array

# print(selection_sort(data))





# Сортировка слиянием           clear time 0.00341s

def merge_two_list(a,b):
    c=[]
    i=j=0
    while i<len(a) and j <len(b):
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    if i<len(a):
        c+=a[i:]
    if j<len(b):
        c+=b[j:]
    return c

@time_measure
def merge_sort(array):
    if len(array)==1:
        return array
    middle=len(array)//2
    left=merge_sort(array[:middle])
    right=merge_sort(array[middle:])
    return merge_two_list(left,right)

# print(merge_sort(data))


# Быстрая сортировка                 clear time 0.00197s

@time_measure
def quick_sort(array):
    if len(array)<=1:
        return array

    elem=array[0]
    left=list(filter(lambda x: x<elem, array))
    center=[i for i in array if i==elem]
    right=list(filter(lambda x: x>elem,array))

    return quick_sort(left)+center+quick_sort(right)

# print(quick_sort(data))


# Сортировка вставками                      clear time 0.00035s
@time_measure
def insertion_sort(array):
    for index in range(1,len(array)):
        value=array[index]
        i=index-1
        while i>=0:
            if value<array[i]:
                array[i+1]=array[i]
                array[i]=value
                i-=1
            else:
                break
    return array


# print(insertion_sort(data))

