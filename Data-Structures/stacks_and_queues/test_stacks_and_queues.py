import pytest
from stacks_and_queues import Stack, Queue, Node

##################################################################
# Pytest Fixtures - One and Many
##################################################################
@pytest.fixture()
def stack_of_one():
    new_stack = Stack()
    new_stack.push('One')
    return new_stack

@pytest.fixture()
def stack_of_four():
    new_stack = Stack()
    new_stack.push('One')
    new_stack.push('Two')
    new_stack.push('Three')
    new_stack.push('Four')   
    return new_stack

@pytest.fixture()
def stack_of_seven():
    new_stack = Stack()
    new_stack.push('One')
    new_stack.push('Two')
    new_stack.push('Three')
    new_stack.push('Four')
    new_stack.push('Five')
    new_stack.push('Six')
    new_stack.push('Seven')
    return new_stack

##################################################################
# Can successfully push onto a stack
##################################################################
def test_one_push():
    new_stack = Stack()
    new_stack.push('One')
    assert new_stack.top.value == 'One'
##################################################################
# Can successfully push multiple values onto a stack
##################################################################
def test_many_push():
    new_stack = Stack()
    new_stack.push('One')
    new_stack.push('Two')
    new_stack.push('Three')
    new_stack.push('Four')   
    assert new_stack.top.value == 'Four'

def test_more_push():
    new_stack = Stack()
    new_stack.push('One')
    new_stack.push('Two')
    new_stack.push('Three')
    new_stack.push('Four')
    new_stack.push('Five')
    new_stack.push('Six')
    new_stack.push('Seven')
    assert new_stack.top.value == 'Seven'
##################################################################
# Can successfully pop off the stack
##################################################################
def test_none_pop():
    new_stack = Stack()  
    assert new_stack.pop() == None

def test_one_pop(stack_of_one):
    assert stack_of_one.pop() == 'One'

def test_many_pop(stack_of_seven):
    assert stack_of_seven.pop() == 'Seven'
##################################################################
# Can successfully empty a stack after multiple pops
##################################################################
def test_empty_the_stack(stack_of_seven):
    stack_of_seven.pop() # 7 popped off
    stack_of_seven.pop() # 6 popped off
    stack_of_seven.pop() # 5 popped off
    stack_of_seven.pop() # 4 popped off
    stack_of_seven.pop() # 3 popped off
    stack_of_seven.pop() # 2 popped off
    stack_of_seven.pop() # 1 popped off
    assert stack_of_seven.is_empty() == True
##################################################################
# Can successfully peek the next item on the stack
##################################################################
def test_none_peek():
    new_stack = Stack()
    assert new_stack.peek() == None

def test_one_peek(stack_of_one):
    assert stack_of_one.peek() == 'One'

def test_many_peek(stack_of_four):
    assert stack_of_four.peek() == 'Four'
##################################################################
# Can successfully instantiate an empty stack
##################################################################
def test_empty_stack():
    new_stack = Stack()
    assert new_stack.top == None

##################################################################
# Can successfully enqueue into a queue
##################################################################
def test_enqueue_one():
    new_queue = Queue()
    new_queue.enqueue('One')
    assert new_queue.front.value == 'One'
##################################################################
# Can successfully enqueue multiple values into a queue
##################################################################
def test_add_four():
    new_queue = Queue()
    new_queue.enqueue('One')
    new_queue.enqueue(2)
    new_queue.enqueue('Three')
    new_queue.enqueue(4)
    assert new_queue.front.value == 'One'
    assert new_queue.end.value == 4

def test_add_eight():
    new_queue = Queue()
    new_queue.enqueue('One')
    new_queue.enqueue(2)
    new_queue.enqueue('Three')
    new_queue.enqueue(4)
    new_queue.enqueue('Five')
    new_queue.enqueue(6)
    new_queue.enqueue('Seven')
    new_queue.enqueue(8)
    assert new_queue.front.value == 'One'
    assert new_queue.end.value == 8

##################################################################
# Can successfully dequeue out of a queue the expected value
##################################################################
def test_none():
    pass
##################################################################
# Can successfully peek into a queue, seeing the expected value
##################################################################
def test_none():
    pass
##################################################################
# Can successfully empty a queue after multiple dequeues
##################################################################
def test_none():
    pass
##################################################################
# Can successfully instantiate an empty queue
##################################################################
def test_none():
    pass