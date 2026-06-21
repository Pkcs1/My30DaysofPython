"""Set
Collection of items.
unordered, un-indexed
used to store unique items, and it is possible to find the 
union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.
set(), {}, Acces items by loops, .add(), .update(), .remove() & .pop(random), .clear()

We can join two sets using the union() or update() method or | symbol .
.intersection() Intersection returns a set of items which are in both the sets or using & symbol.
A set can be a subset or super set of other sets:
Subset: issubset()
Super set: issuperset

.difference() It returns the difference between two sets or using - symbol .

.symmetric_difference() It returns the symmetric difference between two sets. It means that it returns a set that contains all items from both sets, except items that are present in both sets, mathematically: (A\B) ∪ (B\A)
The symmetric difference between two sets represents all the elements that belong to either of the sets, but not to both at the same time.
It grabs everything unique to Set A and everything unique to Set B, while completely throwing away the overlapping middle section where they intersect.

If two sets do not have a common item or items we call them disjoint sets. We can check if two sets are joint or disjoint using isdisjoint() method.
"""

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Exercise 1
print(len(it_companies))
it_companies.add("Twitter")
multipleit = {"X", "Anthropic", "GPT"}
union = it_companies.union(multipleit)
print(union)
union.remove("Apple")
print(union)

#Exercise 2
unionAB = A.union(B)
print(unionAB)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
unionBA = B.union(A)
print(A.symmetric_difference(B))
del unionAB
del unionBA

#Exercise 3
age_set = set(age)
print(len(age_set))
print(len(age))

sentence = "I am a teacher and I love to inspire and teach people."
words_list = sentence.replace(".", " ").split()
unique_words = set(words_list)
print(unique_words)
print(len(unique_words))
