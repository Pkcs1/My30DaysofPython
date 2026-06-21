empty_list = []
five_list = ["Bankai", "Tensa Zangetsu", "Senbonzakura Kageyoshi", "Daiguren","Hyorinmaru","Indonesia","Japan"]
print(len(five_list)) 
first_item = five_list[0]
last_item = five_list[-1]
middle_index = len(five_list) // 2
middle_item = five_list[middle_index]
print(f"First item: {first_item}\nLast item: {last_item}\nMiddle item: {middle_item}")
mixed_data_types = ['Naufal', 18, 173, "Single", 'Indonesia']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(it_companies)
print(len(it_companies))
first_company = it_companies[0]
last_company = it_companies[-1]
midcompany_index = len(it_companies) // 2
"""
middlecom_item = it_companies[midcompany_index]
print(first_company, last_company, middlecom_item)
it_companies[0] = 'Meta'
print(it_companies)
it_companies.insert(midcompany_index, 'Anthropic')
print(it_companies)

it_companies[1] = it_companies[1].upper()
print(it_companies)

print('# '.join(it_companies))

print("Apple" in it_companies)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

mid = len(it_companies) // 2
midde_slice = it_companies[mid - 1 : mid + 1]
print(midde_slice)

it_companies.pop(0)
print(it_companies)

it_companies.pop(midcompany_index)
print(it_companies)

it_companies.pop(-1)
print(it_companies)

del it_companies[0:]
print(it_companies)

del it_companies
print(it_companies)
"""
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
full_stack = front_end
print(full_stack)

rdxindx = full_stack.index('Redux') + 1
full_stack = full_stack[:rdxindx] + ['Python', 'SQL'] + full_stack[rdxindx:]
print(full_stack)