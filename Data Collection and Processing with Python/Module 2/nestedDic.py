d = {'key1': {'a': 5, 'c': 90, 5: 50}, 'key2':{'b': 3, 'c': "yes"}}
value = d['key2']['b']
print(value) #  3


'''
📘 Nested Lists vs Nested Dictionaries in Python

Lists use **numeric indexes** to access elements.
Dictionaries use **keys** to access values.

Let's explore both with simple examples.
'''

# --------------------
# 🔹 Nested List Example
# --------------------
animals = [['cat', 'dog'], ['horse', 'cow'], ['lion', 'tiger']]

'''
Accessing using numeric positions:
- animals[0] → ['cat', 'dog']
- animals[0][1] → 'dog'
'''

print(animals[0])      # ['cat', 'dog']
print(animals[0][1])   # 'dog'

# Replace an element
animals[1][0] = 'unicorn'
print(animals)         # [['cat', 'dog'], ['unicorn', 'cow'], ['lion', 'tiger']]

# Add a new animal to the first group
animals[0].append('mouse')
print(animals)         # [['cat', 'dog', 'mouse'], ['unicorn', 'cow'], ['lion', 'tiger']]

# -----------------------------
# 🔹 Nested Dictionary Example
# -----------------------------
d = {
    'key1': {'a': 5, 'c': 90, 5: 50},
    'key2': {'b': 3, 'c': "yes"}
}

'''
Accessing using keys:
- d['key1'] → {'a': 5, 'c': 90, 5: 50}
- d['key1']['a'] → 5
- d['key1'][5] → 50 (5 is a number used as a key)
- d['key2']['c'] → "yes"
'''

print(d['key1'])       # {'a': 5, 'c': 90, 5: 50}
print(d['key1']['a'])  # 5
print(d['key1'][5])    # 50
print(d['key2']['c'])  # "yes"

# Replace a value
d['key1']['a'] = 100
print(d['key1']['a'])  # 100

# Add a new key-value pair
d['key2']['new_key'] = 'hello'
print(d['key2'])       # {'b': 3, 'c': 'yes', 'new_key': 'hello'}

# -----------------------------
# 🔚 Summary
# -----------------------------
'''
✅ List:
- Ordered
- Access using indexes: list[0][1]
- Supports append(), remove(), etc.

✅ Dictionary:
- Unordered (uses keys)
- Access using keys: dict['key1']['a']
- Use keys to add, update, or delete values
'''
