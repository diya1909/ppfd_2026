# =========================
# METHODS OF DICTIONARY
# =========================

# CREATE
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# READ
print("Dictionary values:", car.values())

# UPDATE
car.update({"tyre": 4})
print("After update:", car)

# DELETE
# pop -> delete one item
car.pop("brand")
print("After pop:", car)

# clear -> empty dictionary
car.clear()
print("After clear:", car)

# del -> delete whole dictionary
del car
# print(car)  # this will give error if uncommented


# =========================
# METHODS OF SET
# =========================

# CREATE
myset = {"19", "09", "2005"}
set1 = ("parul", "university")

# READ
print("Original set:", myset)

# UPDATE
myset.update(set1)
print("After update:", myset)

# ADD
myset.add("diya")
print("After add:", myset)

# COPY
set2 = myset.copy()
set2.add("dobariya")
print("Copied set:", set2)

# DIFFERENCE
z = set2.difference(myset)
print("Difference:", z)

# INTERSECTION
print("Intersection:", set2.intersection(myset))

# DELETE
set2.discard("dobariya")
print("After discard:", set2)

set2.clear()
print("After clear:", set2)


# =========================
# METHODS OF LIST
# =========================

# CREATE
l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9]

# READ
print("Original list:", l1)

# UPDATE
print("Appending 0")
l1.append(0)
print(l1)

print("Copy list")
x = l1.copy()
print(x)

print("Count specific element (4)")
print(l1.count(4))

print("Extend l1 with l2")
l1.extend(l2)
print(l1)

print("Insert 'ten' at index 10")
l1.insert(10, "ten")
print(l1)

print("Reverse l1")
l1.reverse()
print(l1)

print("Sort l1")
l1.sort()
print(l1)

# DELETE
# pop -> remove last element
l1.pop()
print("After pop:", l1)

# remove -> remove specific element
l1.remove(4)
print("After remove 4:", l1)

# clear -> empty list
l1.clear()
print("After clear:", l1)

# del -> delete whole list
del l1
# print(l1)  # error if uncommented
