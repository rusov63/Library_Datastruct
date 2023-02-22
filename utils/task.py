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

n1 = Node(5, None)
n2 = Node('a', n1)
print(n1.data) #5
print(n2.data) #a
print(n1)           #<__main__.Node object at 0x0000022803036050>
print(n2.next_node) #<__main__.Node object at 0x0000022803036050>

stack = Stack()
stack.push('data1')
stack.push('data2')
stack.push('data3')
print(stack.top.data)
print(stack.top.next_node.data)
print(stack.top.next_node.next_node.data)
print(stack.top.next_node.next_node.next_node)
#print(stack.top.next_node.next_node.next_node.data)

'''Структуры данных. Конспект
#https://skyengpublic.notion.site/ead128b268a247febb06b7a83652e1db#96ebfaa0c8854415a75a09178f4a29b5'''


