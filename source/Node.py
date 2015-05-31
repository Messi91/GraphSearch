# __author__ = 'mesfinmebrate'
#
# class Node:
#
#     def __init__(self,initdata):
#         self.__data = initdata
#         self.__next = None
#
#     def getData(self):
#         return self.__data
#
#     def getNext(self):
#         return self.__next
#
#     def setData(self,newdata):
#         self.__data = newdata
#
#     def setNext(self,newnext):
#         self.__next = newnext
#
#     def __str__(self):
#         return self.__data
#
#
# class UnorderedList:
#
#     def __init__(self):
#         self.head = None
#         self.__currentSize = 0
#
#     def isEmpty(self):
#         return self.head is None
#
#     def add(self,item):
#         temp = Node(item)
#         temp.setNext(self.head)
#         self.head = temp
#         self.__currentSize += 1
#
#     def size(self):
#         return self.__currentSize
#
#
# def printList(node):
#     while node:
#         print node,
#         node = node.getNext()
#     print
#
#
# if __name__ == "__main__":
#
#     list = UnorderedList()
#     list.add("Brian")
#     list.add("Dean")
#     list.add("Buddy")
#
#     printList(list.head)
#     print list.size()