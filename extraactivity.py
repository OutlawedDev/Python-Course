a = {1,2,3,4,5}
b = {4,5,6,7,8}

print("Set A:", a)
print("Set B:", b)

union_set = a.union(b)
print("\nUnion (A U B):", union_set)

intersection_set = a.intersection(b)
print("Intersection (A ∩ B):", intersection_set)

difference_set = a.difference(b)
print("Difference (A - B):", difference_set)

difference_set_b = b.difference(a)
print("Difference (B - A):", difference_set_b)

symmetric_diff_set = a.symmetric_difference(b)
print("Symmetric Difference (A Δ B):", symmetric_diff_set)

print("\nIs a subset of B?:", a.issubset(b))
print("is a superset of B?:", a.issuperset(b))

print("Are A and B disjoint?:", a.isdisjoint(b))



