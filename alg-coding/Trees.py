
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def do(node:TreeNode):
    print(node.val)


# 前序 递归
def pre_order_recursion(root:TreeNode):
    if not root: return
    do(root)
    pre_order_recursion(root.left)
    pre_order_recursion(root.right)

# 前序 迭代
def pre_order_iteration(root):
    res = []
    if not root:
        return res
    stack = [root]
    while stack:
        curr = stack.pop()
        if curr:
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
            stack.append(curr)
            stack.append(None)
        else:
            res.append(stack.pop().val)
    return res

# 中序 递归
def in_order_recursion(root):
    if not root: return
    in_order_recursion(root.right)
    do(root)
    in_order_recursion(root.right)

# 中序 迭代
def in_order_iteration(root):
    res = []
    if not root:
        return res
    stack = [root]
    while stack:
        curr = stack.pop()
        if curr:
            if curr.right:
                stack.append(curr.right)
            stack.append(curr)
            stack.append(None)
            if curr.left:
                stack.append(curr.left)
        else:
            res.append(stack.pop().val)
    return res

# 后序 递归
def post_order_recursion(root):
    if not root: return
    post_order_recursion(root.left)
    post_order_recursion(root.right)
    do(root)

# 后序 迭代
def post_order_iteration(root):
    res = []
    if not root: return res
    stack = [root]
    while stack:
        curr = stack.pop()
        if curr:
            stack.append(curr)
            stack.append(None)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        else:
            res.append(stack.pop().val)
    return res

# 层序 迭代
def layer_order_iteration(root):
    res = []
    if not root:
        return res
    queue = [root]
    while queue:
        temp = []
        layer_values = []
        for q in queue:
            layer_values.append(q.val)
            if q.left:
                temp.append(q.left)
            if q.right:
                temp.append(q.right)
        res.append(layer_values)
        queue = temp
    return res

class MultiTreeNode:
    def __init__(self, val=None, children = None):
        self.val = val
        self.children = children

# 层序遍历
def layer_order_iteration_muilttree(root: MultiTreeNode):
    res = []
    if not root:
        return res
    queue = [root]
    while queue:
        res.append(node.val for node in queue)
        queue = [child for node in queue for child in node.children]
    return res



















