class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
    
    def __repr__(self):
        return (f'User(username={self.username}, name={self.name}, email={self.email})')
    
    def __str__(self) -> str:
        return self.__repr__()


# 1 cách giải quyết nhanh bài toán với O(N)
class UserDatabase:
    def __init__(self):
        self.users = []
    
    def insert(self, user):
        i = 0
        while i < len(self.users):
            # Tìm vị trí đầu tiên mà usernamr của danh sách lớn hơn username của user thêm vào
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)
    
    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user
    
    def update(self, user):
        # Tìm user cần update
        target = self.find(user.username)
        target.name, target.email = user.name, user.email
    
    def list(self):
        return self.users

# Cây nhị phân
class TreeNode():
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None
    
    def hight(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.hight(self.left), TreeNode.hight(self.right))
    
    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)
    
    def traverse_in_order(self):
        if self is None:
            return []
        return (TreeNode.traverse_in_order(self.left)+
                [self.key] +
                TreeNode.traverse_in_order(self.right))

    def display_keys(self, space = '\t', level = 0):
        # Node là trống
        if self is None:
            print(space * level + '∅')
            return
        # Node là lá
        if self.left is None and self.right is None:
            print(space * level + str(self.key))
            return
        
        TreeNode.display_keys(self.left, space, level+1)
        print(space * level + str(self.key))
        TreeNode.display_keys(self.right, space, level+1)
    
    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left), self.key, TreeNode.to_tuple(self.right)
    
    def __str__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    
    def __repr__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    
    @staticmethod    
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node

def remove_none(nums):
    return [x for x in nums if x is not None]

def is_bst(node):
    if node is None:
        return True, None, None
    is_bst_l, max_l, min_l = is_bst(node.left)
    is_bst_r, max_r, min_r = is_bst(node.right)
    is_bst_node = (is_bst_l and is_bst_r and
                    (max_l is None or max_l < node.key) and
                    (min_r is None or min_r > node.key))
    max_node = max(remove_none([max_r, max_l, node.key]))
    min_node = min(remove_none([min_r, min_l, node.key]))
    return is_bst_node, max_node, min_node

class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

def insert(node, key, value):
    if node is None:
        node = BSTNode(key, value)
    if key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node.key
    if key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node.key
    return node

def find(node, key):
    if node is None:
        return None
    if node.key == key:
        return node
    if node.key < key:
        return find(node.right, key)
    if node.key > key:
        return find(node.left, key)

def update(node, key, value):
    target = find(node, key)
    if target is not None:
     target.key, target.value = key, value
    
def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)

def is_balance(node):
    if node is None:
        return True, 0
    is_balance_l , hight_l = is_balance(node.left)
    is_balance_r , hight_r = is_balance(node.right)
    is_balance_node = is_balance_l and is_balance_r and abs(hight_l - hight_r) <= 1
    hight_node = 1 + max(hight_l, hight_r)
    return is_balance_node, hight_node

def make_balanced_bst(data, lo=0, hi=None, parent=None):
    if hi is None:
        hi = len(data) - 1
    if lo > hi:
        return None
    
    mid = (lo + hi) // 2
    key, value = data[mid]

    root = BSTNode(key, value)
    root.parent = parent
    root.left = make_balanced_bst(data, lo, mid-1, root)
    root.right = make_balanced_bst(data, mid+1, hi, root)

    return root

def balance_bst(node):
    return make_balanced_bst(list_all(node))

def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)

def display_tree(node, space = '\t', level = 0):
    if node is None:
        print(space * level)
        return
    if node.left is None and node.right is None:
        print(space * level + str(node.key))
        return
    display_tree(node.left, space, level +1)
    print(space * level + str(node.key))
    display_tree(node.right, space, level +1)

class TreeMap():
    def __init__(self):
        self.root = None
        
    def __setitem__(self, key, value):
        node = find(self.root, key)
        if not node:
            self.root = insert(self.root, key, value)
            self.root = balance_bst(self.root)
        else:
            update(self.root, key, value)
            
        
    def __getitem__(self, key):
        node = find(self.root, key)
        return node.value if node else None
    
    def __iter__(self):
        return (x for x in list_all(self.root))
    
    def __len__(self):
        return tree_size(self.root)
    
    def display(self):
        return display_tree(self.root)