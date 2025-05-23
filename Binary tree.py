class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

   def PrintTree ( self ) :
       if self.left :
           self.left.PrintTree ()
       print ( self.data, end= ' ' ) ,
       if self.right : 
           self.right.PrintTree ()

class Solution:
    '''
    Function to invert the tree
    '''
    def invertTree(self, root):
        if not root :
            return
        stack = [ root ]

        while stack :
            node = stack.pop()
            node.left , node.right = node.right , node.left
            if node.left : stack.append ( node.left )
            if node.right : stack.append ( node.right )

        return root

if __name__ == '__main__':
    '''
                10                                              10
              /    \                                          /    \         
            20      30              ========>>              30      20           
           /         \                                      /        \
          40          50                                  50          40 
    '''
    Tree = Node(10)
    Tree.left = Node(20)
    Tree.right = Node(30)
    Tree.left.left = Node(40)
    Tree.right.right = Node(50)
    print('Initial Tree :',end = ' ' )
    Tree.PrintTree()
    Solution().invertTree(root=Tree)
    print('\nInverted Tree :', end=' ')
    Tree.PrintTree()