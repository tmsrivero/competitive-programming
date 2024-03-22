def create_key_value_array(input_list):
    key_value_dict = {}

    for key, value in input_list:
        if key in key_value_dict:
            key_value_dict[key] += value
        else:
            key_value_dict[key] = value

    return key_value_dict


q, k = map(int, input().split())
res = 0
sum = 0
for _ in range(q):
    s, e = input().split()

input_list = []
result = create_key_value_array(input_list)
print(result)
