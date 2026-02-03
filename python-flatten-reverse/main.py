from src.flatten import flatten
from src.deep_reverse import deep_reverse

input_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
input_list2 = [[1, 2], [3, 4], [5, 6, 7]]

print("Flatten result:")
print(flatten(input_list))

print("\nDeep reverse result:")
print(deep_reverse(input_list2))