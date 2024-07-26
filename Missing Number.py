list_of_numbers = [1,3,4,5,6,7,8,9,10]

n = list_of_numbers[-1]

sum_of_n_numbers = (n * (n + 1)) / 2

sum_of_list = sum(list_of_numbers)

missing_number = sum_of_n_numbers - sum_of_list

print(int(missing_number))
