class Node:
  def __init__(self,val):
    self.left = None
    self.data = val
    self.right = None
  def binarysearchtree:
    def create (self,val):
      return Node(val)
    def insert(self,node,data):
      if Node is None:
        return self.create(val)
      if data < Node.data:
        Node.left = self.insert(Node.left,data)
      else:
        Node.right = self.insert(Node.right,data)
    return Node
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
      self.postorer(root.right)
      print(root.data,end = " ") 
