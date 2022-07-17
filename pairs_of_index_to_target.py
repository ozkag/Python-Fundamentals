def pairs_sum_to_target(list1, list2, target):
    my_list = []

    for i in range(len(list1)):
        for j in range(len(list2)):
            lst = []
            if list1[i] + list2[j] == target:
                lst.append(i)
                lst.append(j)
                my_list.append(lst)

    return my_list

#test case

list1 = [1, -2, 4, 5, 9]
list2 = [4, 2, -4, -4, 0]
target = 5

a = pairs_sum_to_target(list1, list2, target)
print(a)








 