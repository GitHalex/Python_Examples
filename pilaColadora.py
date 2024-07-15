from typing import List


class Stack:
    def __init__(self) -> None:
        """Initialize an empty stack."""
        self._stack_list: List[int] = []

    def push(self, val: int) -> None:
        """Push a value onto the stack."""
        self._stack_list.append(val)

    def pop(self) -> int:
        """Pop a value from the stack and return it. Raise an IndexError if the stack is empty."""
        if not self._stack_list:
            raise IndexError("pop from empty stack")
        return self._stack_list.pop()


class AddingStack(Stack):
    def __init__(self) -> None:
        """Initialize an AddingStack with a sum of zero."""
        super().__init__()
        self._sum: int = 0
        self._contador: int = 0
        self._contadorAgregados: int = 0

    def get_contador(self) -> int:
        return self._contador

    def get_add(self) -> int:
        return self._contadorAgregados

    def get_sum(self) -> int:
        """Return the sum of all values in the stack."""
        return self._sum

    def push(self, val: int) -> None:
        """Push a value onto the stack and add it to the sum."""
        self._sum += val
        super().push(val)
        self._contadorAgregados += 1

    def pop(self) -> int:
        """Pop a value from the stack and subtract it from the sum. Raise an IndexError if the stack is empty."""
        val = super().pop()
        self._sum -= val
        self._contador += 1

        return val


if __name__ == "__main__":
    stack_object = AddingStack()
    for i in range(3):
        stack_object.push(i)

    print(f"Sum of elements in stack: {stack_object.get_sum()}")
    print(
        f"Cantidad de elementos agregados: {stack_object.get_add()}")

    while True:
        try:
            print(stack_object.pop())
        except IndexError:
            print("Stack is empty.")
            break
    print(
        f"Cantidad de elementos sacados de la lista: {stack_object.get_contador()}")
