# Linear Search in Staring
def linear_search_string(str, target):
    for i in str:
        if i == target:
            return True
    return False


print(linear_search_string("Sajib", 'a')) # True
print(linear_search_string("", 'a')) # False



def linear_search_string1(str):
    new_array = []
    for i in str:
        new_array.append(i)
    return new_array


print(linear_search_string1("sajib")) # ['s', 'a', 'j', 'i', 'b']
