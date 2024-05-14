# Код двійкового дерева пошуку з конспекта
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

# Завдання 1 - знаходження найбільшого значення
def find_max(root):
    current = root
    while current.right is not None:
        current = current.right
    return current.val

# Завдання 2 - знаходження найменшого значення
def find_min(root):
    current = root
    while current.left is not None:
        current = current.left
    return current.val

# Завдання 3 - знаходження суми всіх значень
def find_sum(root):
    if root is None:
        return 0
    return root.val + find_sum(root.left) + find_sum(root.right)

# Test
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)

# Пошук значення
val =  4
result = search(root, val)
if result:
    print(f"У дереві знайдено значення {result.val}")
else:
    print(f"У дереві не знайдено значення {val}")

# Найбільше значення
print(f"Найбільше значення у дереві: {find_max(root)}")

# Найменше значення
print(f"Найменше значення у дереві: {find_min(root)}")

# Сума всіх значень
print(f"Сума всіх значень у дереві: {find_sum(root)}")
