def smedSort(unsorted):
    # This line is necessary because we do pops from the list and it does damage to the original.
    unsorted_list = unsorted
    if len(unsorted_list)<=14:
        for i in range(1,len(unsorted_list)):
            value=unsorted_list[i]
            hole=i
            
            while hole>0 and value<unsorted_list[hole-1]:
                unsorted_list[hole]=unsorted_list[hole-1]
                hole-=1
            unsorted_list[hole]=value
        return unsorted_list
    
    pivot = smedSort([unsorted_list.pop(len(unsorted_list) / 2), unsorted_list.pop(0), unsorted_list.pop(-1)])
     
    less=[]
    firstMiddle=[]
    secondMiddle=[]
    greater=[]
    
    for x in unsorted_list:
        if x <= pivot[0]:
            less.append(x)
        elif x > pivot[0] and x < pivot[1]:
            firstMiddle.append(x)
        elif x >= pivot[1] and x < pivot[2]:
            secondMiddle.append(x)
        else:
            greater.append(x)
    
    less = smedSort(less)
    firstMiddle = smedSort(firstMiddle)
    secondMiddle = smedSort(secondMiddle)
    greater = smedSort(greater)

    return less + list([pivot[0]]) + firstMiddle + list([pivot[1]]) + secondMiddle + list([pivot[2]]) + greater