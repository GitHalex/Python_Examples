class Stack:

  def __init__(self) -> None:
    self.__stack_list: list = []

  def push(self, val: int):
    self.__stack_list.append(val)

  def pop(self) -> int:
    val = self.__stack_list[-1]
    del self.__stack_list[-1]
    return val
  


class AddingStack(Stack):

  def __init__(self) -> None:
    Stack.__init__(self)
    self.__sum = 0

  def get_sum(self) -> int:
    return self.__sum

  def push(self, val: int):
    self.__sum += val
    Stack.push(self, val)

  def pop(self):
    val = Stack.pop(self)
    self.__sum -= val
    return val
  
stack_object = AddingStack()
for i in range(5):
  stack_object.push(i)

print(stack_object.get_sum())

for j in range(5):
  print(stack_object.pop())