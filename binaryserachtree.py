class Node:
  def __init__(self,val):
    self.left = None
    self.data = val
    self.right = None
    self.height = None
class bst:
  def create(self,val):
    return Node(val)
  def insert(self,node,data):
    if node is None:
      return self.create(data)
    if data < node.data:
      node.left = self.insert(node.left,data)
    else:
      node.right = self.insert(node.right,data)
    return node
  def inorder(self,root):
    if root is not None:
      self.inorder(root.left)
      print(root.data,end = " ")
      self.inorder(root.right)
  def preorder(self,root):
    if root is not None:
      print(root.data,end = " ")
      self.preorder(root.left)
      self.preorder(root.right)
  def postorder(self,root):
    if root is not None:
      self.postorder(root.left)
      self.postorder(root.right)
      print(root.data,end= " ")
  def topview(self,root):
    q = []
    d = dict()
    root.height = 0
    q.append(root)
    while len(q) != 0:
      temp = q.pop(0)        
      if temp.height not in d:
        d[temp.height] = temp.data
      if temp.left is not None:
        q.append(temp.left)
        temp.left.height=temp.height-1
      if temp.right is not None:
        q.append(temp.right)
        temp.right.height = temp.height+1 
    result = sorted(d.values())
    print(*result)
  def level(self,root):
    q=[]
    root.height=0
    q.append(root)
    while len(q)!= 0:
      temp = q.pop(0)
      print(temp.data,end=" ")
      if temp.left is not None:
        q.append(temp.left)
      if temp.right is not None:
        q.append(temp.right)
  def leftview(self,root):
    q=[]
    q.append(root)
    while len(q)!=0:
      size=len(q)
      for i in range(size):
        temp=q.pop(0)
        if i==0:
          print(temp.data,end=" ")
        if temp.left:
          q.append(temp.left)
        if temp.right:
          q.append(temp.right)
  def rightview(self,root):
    q=[]
    q.append(root)
    while len(q)!=0:
      size=len(q)
      for i in range(size):
        temp=q.pop(0)
        if i==size-1:
          print(temp.data,end=" ")
        if temp.left:
          q.append(temp.left)
        if temp.right:
          q.append(temp.right)
  
tree = bst()
n=int(input())
root = tree.create(n)
while True:
  k=int(input())
  if k==-1:
    break
  tree.insert(root,k)
print("inorder traversal:")
tree.inorder(root)
print()
print("preorder traversal:")
tree.preorder(root)
print()
print("postorder traversal:")
tree.postorder(root)
print()
print("top view")
tree.topview(root)
print("level order transversal")
tree.level(root)
print("\nleftview")
tree.leftview(root)
print("\nrightview")
tree.rightview(root)
print()

