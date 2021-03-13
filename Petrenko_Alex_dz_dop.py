test_list = ['Hello', 42.00000014, True, [1, 2, 3], 1, 2, 'Basil']
for i in test_list:
    if i == [1, 2, 3]:
        del test_list[3]
        test_list.insert(3, 1)
        test_list.insert(4, 2)
        test_list.insert(5, 3)
print(test_list)