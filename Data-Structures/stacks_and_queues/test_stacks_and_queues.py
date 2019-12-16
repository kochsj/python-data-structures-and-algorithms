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

@pytest.fixture()
def queue_of_one():
    new_queue = Queue()
    new_queue.enqueue('One')
    return new_queue

@pytest.fixture()
def queue_of_four():
    new_queue = Queue()
    new_queue.enqueue('One')
    new_queue.enqueue(2)
    new_queue.enqueue('Three')
    new_queue.enqueue(4)
    return new_queue

@pytest.fixture()
def queue_of_eight():
    new_queue = Queue()
    new_queue.enqueue('One')
    new_queue.enqueue(2)
    new_queue.enqueue('Three')
    new_queue.enqueue(4)
    new_queue.enqueue('Five')
    new_queue.enqueue(6)
    new_queue.enqueue('Seven')
    new_queue.enqueue(8)
    return new_queue
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
def test_dequeue_one(queue_of_one):
    assert queue_of_one.dequeue() == 'One'

def test_dequeue_four(queue_of_four):
    queue_of_four.dequeue() # One
    queue_of_four.dequeue() # 2
    queue_of_four.dequeue() # Three
    assert queue_of_four.dequeue() == 4

def test_dequeue_eight(queue_of_eight):
    queue_of_eight.dequeue() # One
    queue_of_eight.dequeue() # 2
    queue_of_eight.dequeue() # Three
    queue_of_eight.dequeue() # 4
    queue_of_eight.dequeue() # Five
    queue_of_eight.dequeue() # 6
    queue_of_eight.dequeue() # Seven
    assert queue_of_eight.dequeue() == 8
##################################################################
# Can successfully peek into a queue, seeing the expected value
##################################################################
def test_peek_none():
    new_queue = Queue()
    assert new_queue.peek() == None

def test_peek_third(queue_of_four):
    queue_of_four.dequeue() # One
    queue_of_four.dequeue() # 2
    assert queue_of_four.peek() == 'Three'
    
def test_peek_remove_four(queue_of_eight):
    queue_of_eight.dequeue() #one
    queue_of_eight.dequeue() # 2
    queue_of_eight.dequeue() # Three
    queue_of_eight.dequeue() # 4
    assert queue_of_eight.peek() == 'Five'
##################################################################
# Can successfully empty a queue after multiple dequeues
##################################################################
def test_is_empty_dequeue_none():
    new_queue = Queue()
    new_queue.dequeue()
    assert new_queue.is_empty() == True

def test_is_empty_dequeue_one(queue_of_one):
    assert queue_of_one.is_empty() == False
    queue_of_one.dequeue() # One
    assert queue_of_one.is_empty() == True

def test_is_empty_dequeue_eight(queue_of_eight):
    assert queue_of_eight.is_empty() == False
    queue_of_eight.dequeue() # One
    queue_of_eight.dequeue() # 2
    queue_of_eight.dequeue() # Three
    queue_of_eight.dequeue() # 4
    assert queue_of_eight.is_empty() == False
    queue_of_eight.dequeue() # Five
    queue_of_eight.dequeue() # 6
    queue_of_eight.dequeue() # Seven
    queue_of_eight.dequeue() # 8
    assert queue_of_eight.is_empty() == True
##################################################################
# Can successfully instantiate an empty queue
##################################################################
def test_none():
    new_queue = Queue()
    assert isinstance(new_queue, Queue)