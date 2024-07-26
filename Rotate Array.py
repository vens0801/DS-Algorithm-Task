get_space_separated_integers = input().split()
k = int(input())

converted_list = []

for i in get_space_separated_integers:
    i = int(i)
    converted_list.append(i)

first_part_condition = len(get_space_separated_integers) - k

first_part = converted_list[first_part_condition:]

second_part = converted_list[:first_part_condition]

result = first_part + second_part

print(result)
