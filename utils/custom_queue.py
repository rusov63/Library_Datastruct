class Node:
    def __init__(self, data, next_node=None):
        """Класс активации узла"""
        self.data = data
        self.next_node = next_node #ссылка на следующий узел

class Queue:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    def enqueue(self, data):
        """Добавление данных в очередь"""
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node


queue = Queue()
queue.enqueue('data1')
queue.enqueue('data2')
queue.enqueue('data3')

print(queue.head.data)
print(queue.head.next_node.data)
print(queue.tail.data)
print(queue.tail.next_node)
#print(queue.tail.next_node.data)

# Результаты вывода в консоли
#data1
#data2
#data3
#None
#AttributeError: 'NoneType' object has no attribute 'data'