ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print(f"Min: {min_age}\nMax: {max_age}")
ages.append(min_age)
ages.append(max_age)
print(ages) # nambahin age 2 jadi total index 12

mid_idx = len(ages) // 2
print(mid_idx)

age1 = ages[mid_idx - 1]
age2 = ages[mid_idx]

median_age = (age1 + age2) / 2

print(f"The two middle ages are: {age1} & {age2}\nThe median of the ages is: {median_age}")


total_sum = sum(ages)
total_count = len(ages)
average_age = total_sum / total_count

print(f"Total of all gathered ages are: {total_sum}\nTotal count: {total_count}\nWith the average age of {average_age}")

age_range = max_age - min_age
print(f"Ages range is: {age_range}")

distance_min = abs(min_age - average_age)
distance_max = abs(max_age - average_age)

print(f"Distance from minimal age: {distance_min}\nDistance from maximum age: {distance_max}")

if distance_min > distance_max:
    print("Distance from minimum is more further")
elif distance_max > distance_min:
    print("Distance from maximum is further ")
else:
    print("Theyre the same")

print("LOL")