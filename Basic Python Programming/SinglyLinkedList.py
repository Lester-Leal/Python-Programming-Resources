class Node :
  def __init__(self, data):
    self.__data = data
    self.__next = None
  
  def getData(self):
    return self.__data
  
  def setData(self, data):
    self.__data = data
  
  def getNext(self):
    return self.__next
  
  def setNext(self, next):
    self.__next = next

class LinkedList:
  def __init__(self):
    self.__head = None
  
  def getHead():
    return self.__head
  
  def setHead(head):
    self.__head = head

  def addNode(self, data):
    if (self.__head == None):
      self.__head = Node(data)
    else:
      currentNode = self.__head
      while (currentNode.getNext() != None):
        currentNode = currentNode.getNext()
      currentNode.setNext(Node(data))

  def displayList(self):
    currentNode = self.__head
    while (currentNode != None):
      print(currentNode.getData())
      currentNode = currentNode.getNext()

lst = LinkedList()
lst.addNode(5)
lst.addNode(6)
lst.addNode(7)
lst.addNode(8)
lst.addNode(9)
lst.addNode(10)

lst.displayList()


    
