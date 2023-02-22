class Node:
    def __init__(self, data, next_node=None):
        """Класс активации узла"""
        self.data = data
        self.next_node = next_node #ссылка на следующий узел

class Stack:
    '''Стэк (Stack) — структура данных, представляющая из себя упорядоченный набор элементов,
    в которой добавление новых элементов и удаление существующих производится с одного конца,
    называемого вершиной стека. Притом первым из стека удаляется элемент, который был помещен
     туда последним, то есть в стеке реализуется стратегия «последним вошел — первым вышел» '''
    def __init__(self):
        '''Инициализация пустого стэка'''
        self.top = None

    def push(self, data):
        '''Добавляет элемент в стэк'''
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        pop_node = self.top
        pop_data = pop_node.data
        self.top = pop_node.next_node
        return pop_data

stack = Stack()
stack.push('data1')
data = stack.pop()

# стэк стал пустой
print(stack.top)
None

# pop() удаляет элемент и возвращает данные удаленного элемента
print(data)
'data1'


stack = Stack()
stack.push('data1')
stack.push('data2')
data = stack.pop()

# теперь последний элемента содержит данные data1
print(stack.top.data)
'data1'

# данные удаленного элемента
print(data)
'data2'
