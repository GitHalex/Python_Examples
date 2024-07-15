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
        self._sum = 0

    def get_sum(self) -> int:
        """Return the sum of all values in the stack."""
        return self._sum

    def push(self, val: int) -> None:
        """Push a value onto the stack and add it to the sum."""
        self._sum += val
        super().push(val)

    def pop(self) -> int:
        """Pop a value from the stack and subtract it from the sum. Raise an IndexError if the stack is empty."""
        val = super().pop()
        self._sum -= val
        return val


if __name__ == "__main__":
    stack_object = AddingStack()
    for i in range(5):
        stack_object.push(i)

    print(f"Sum of elements in stack: {stack_object.get_sum()}")

    while True:
        try:
            print(stack_object.pop())
        except IndexError:
            print("Stack is empty.")
            break
