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

    def dequeue(self):
        """Удаляет из очереди крайний левый элемент"""
        deqeueued_node = self.head
        if self.head == None:
            return None
        else:
            self.head = self.head.next_node
            return deqeueued_node.data


queue = Queue()
queue.enqueue('data1')
queue.enqueue('data2')
queue.enqueue('data3')

print(queue.dequeue()) # data1.
print(queue.dequeue()) # data2.
print(queue.dequeue()) # data3
print(queue.dequeue()) # None