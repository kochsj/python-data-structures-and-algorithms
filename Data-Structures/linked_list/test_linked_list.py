import pytest
from linked_list import Node, LinkedList



@pytest.fixture
def node():
    return Node(42)


@pytest.fixture
def ll():
    return LinkedList()


@pytest.fixture
def filled_ll():
    ll = LinkedList()
    ll.insert(42)
    ll.insert(14)
    ll.insert('October')
    return ll


def test_exists():
    assert LinkedList
    assert Node


def test_node_next(node):
    assert node.next_node == None


def test_node_value(node):
    assert node.value == 42


def test_ll_head(ll):
    assert ll.head == None


def test_ll_insert_one(ll):
    ll.insert(42)
    assert ll.head.value == 42


def test_ll_insert_two(ll):
    ll.insert(42)
    ll.insert(14)
    assert ll.head.value == 14
    assert ll.head.next_node.value == 42


def test_ll_insert_three(ll):
    ll.insert(42)
    ll.insert(14)
    ll.insert('October')
    assert ll.head.value == 'October'
    assert ll.head.next_node.value == 14
    assert ll.head.next_node.next_node.value == 42


def test_ll_includes(filled_ll):
    assert filled_ll.includes('October') == True
    assert filled_ll.includes(2001) == False
    # Edge Case: Checking an empty linked list
    assert LinkedList().includes('Towel') == False


def test_ll_append(ll, filled_ll):
    # Append Once
    ll.append(2)
    assert ll.head.value == 2

    # Append Multiple
    ll.append(4)
    assert ll.head.next_node.value == 4

    filled_ll.append(2)
    assert filled_ll.head.next_node.next_node.next_node.value == 2


def test_ll_insert_before(ll, filled_ll):
    assert ll.head == None
    # Empty List
    ll.insert_before(2, 6)
    assert ll.head == None

    # Single Item List
    ll.append(2)
    ll.insert_before(2, 1)
    assert ll.head.value == 1

    # Target Not Present
    ll.insert_before(1, 3)
    assert ll.head.value == 3

    # Filled List
    filled_ll.insert_before(14, 'howdy')
    assert filled_ll.head.next_node.value == 'howdy'


def test_ll_insert_after(ll, filled_ll):
    # Empty List
    ll.insert_after(2, 6)
    assert ll.head == None

    # Single Item List
    ll.append(2)
    ll.insert_after(2, 1)
    assert ll.head.next_node.value == 1

    # Target Not Present
    ll.insert_after(3, 4)
    assert ll.head.value == 2
    assert ll.head.next_node.value == 1
    assert ll.head.next_node.next_node == None

    # Filled List
    filled_ll.insert_after(42, 'howdy')
    assert filled_ll.head.next_node.next_node.next_node.value == 'howdy'


# creates linked lists of varrying numbers of nodes:
# one node
@pytest.fixture()
def list_one():
    empty_list = LinkedList()
    empty_list.insert('Node_1')
    return empty_list

# two nodes
@pytest.fixture()
def list_two():
    empty_list = LinkedList()
    empty_list.insert('Node_1')
    empty_list.insert('Node_2')
    return empty_list

# six nodes
@pytest.fixture()
def list_many():
    empty_list = LinkedList()
    empty_list.insert('Node_1')
    empty_list.insert('Node_2')
    empty_list.insert('Node_3')
    empty_list.insert('Node_4')
    empty_list.insert('Node_5')
    empty_list.insert('Node_6')
    return empty_list

# ten nodes
@pytest.fixture()
def list_ten_integer():
    empty_list = LinkedList()
    empty_list.insert(1)
    empty_list.insert(2)
    empty_list.insert(3)
    empty_list.insert(4)
    empty_list.insert(5)
    empty_list.insert(6)
    empty_list.insert(7)
    empty_list.insert(8)
    empty_list.insert(9)
    empty_list.insert(10)
    return empty_list

# Can successfully instantiate an empty linked list
def test_empty_linked_list():
    instance_of_linked_list = LinkedList()
    assert isinstance(instance_of_linked_list, LinkedList) == True

# Can properly insert into the linked list
def test_instance_of_node():
    assert Node('Node_1').value == 'Node_1'

def test_one_item_in_list(list_one):
    assert list_one.head and Node('Node_1').next_node == None

# The head property will properly point to the first node in the linked list
def test_two_items_into_new_list(list_two):
    assert str(list_two.head) == 'Node_2'

# Can properly insert multiple nodes into the linked list
def test_many_items_into_new_list(list_many):
    assert str(list_many.head) == 'Node_6' and str(list_many.head.next_node) == 'Node_5'

# Will return true when finding a value within the linked list that exists
def test_finding_specific_value_TRUE(list_two):
    assert list_two.includes('Node_1') == True

def test_finding_value_in_many_TRUE(list_many):
    assert list_many.includes('Node_1') == True

# Will return false when searching for a value in the linked list that does not exist
def test_finding_value_in_many_FALSE(list_many):
    assert list_many.includes('Node_0') == False

def test_finding_integer_in_many_FALSE(list_many):
    assert list_many.includes(5) == False

# Using method, Can properly return a collection of all the values that exist in the linked list
def test_correct_collection_of_list_items_one(list_one):
    assert list_one.return_list() == ['Node_1']

def test_correct_collection_of_list_items_two(list_two):
    assert list_two.return_list() == ['Node_2', 'Node_1']

def test_correct_collection_of_list_items_many(list_many):
    assert list_many.return_list() == ['Node_6', 'Node_5', 'Node_4', 'Node_3', 'Node_2', 'Node_1']

def test_correct_collection_of_list_items_ten(list_ten_integer):
    assert list_ten_integer.return_list() == 'For testing, Please input strings.'

# Using print, Can properly return a collection of all the values that exist in the linked list
def test_print_list_of_items_one(list_one):
    assert list_one.__str__() == "The values of this list are ['Node_1']. A total of 1 nodes."

def test_print_list_of_items_two(list_two):
    assert list_two.__str__() == "The values of this list are ['Node_2', 'Node_1']. A total of 2 nodes."

def test_print_list_of_items_many(list_many):
    assert list_many.__str__() == "The values of this list are ['Node_6', 'Node_5', 'Node_4', 'Node_3', 'Node_2', 'Node_1']. A total of 6 nodes."


# Can successfully add a node to the end of the linked list
def test_app_ll_one(list_one):
    list_one.append('Node_X')
    assert list_one.return_list() == ['Node_1', 'Node_X']

def test_app_ll_two(list_two):
    list_two.append('Node_X')
    assert list_two.return_list() == ['Node_2', 'Node_1', 'Node_X']

def test_app_ll_many(list_many):
    list_many.append('Node_X')
    assert list_many.return_list() == ['Node_6', 'Node_5', 'Node_4', 'Node_3', 'Node_2', 'Node_1', 'Node_X']

# Can successfully add multiple nodes to the end of a linked list
def test_append_ll_two(list_one):
    list_one.append('Node_X')
    list_one.append('Node_Y')
    assert list_one.return_list() == ['Node_1', 'Node_X', 'Node_Y']

def test_append_ll_three(list_two):
    list_two.append('Node_X')
    list_two.append('Node_Y')
    list_two.append('Node_Y')
    assert list_two.return_list() == ['Node_2', 'Node_1', 'Node_X', 'Node_Y', 'Node_Y']

def test_append_ll_many(list_many):
    list_many.append('Node_X')
    list_many.append('Node_Y')
    list_many.append('Node_Y')
    list_many.append('Node_Y')
    list_many.append('Node_Y')
    list_many.append('Node_Y')
    assert list_many.return_list() == ['Node_6', 'Node_5', 'Node_4', 'Node_3', 'Node_2', 'Node_1', 'Node_X', 'Node_Y', 'Node_Y', 'Node_Y', 'Node_Y', 'Node_Y']

# Can successfully insert a node before a node located in the middle of a linked list
def test_insert_before_middle(list_many):
    list_many.insert_before('Node_3', 'Hello world')
    assert list_many.return_list() == ['Node_6', 'Node_5', 'Node_4', 'Hello world', 'Node_3', 'Node_2', 'Node_1']

def test_insert_before_end(list_many):
    list_many.insert_before('Node_1', 'Hello world')
    assert list_many.return_list() == ['Node_6', 'Node_5', 'Node_4', 'Node_3', 'Node_2', 'Hello world', 'Node_1']

def test_insert_before_second(list_many):
    list_many.insert_before('Node_5', 'Hello world')
    assert list_many.return_list() == ['Node_6', 'Hello world', 'Node_5', 'Node_4', 'Node_3', 'Node_2', 'Node_1']

# Can successfully insert a node before the first node of a linked list
def test_insert_before_first(list_many):
    list_many.insert_before('Node_6', 'Hello world')
    assert list_many.return_list() == ['Hello world','Node_6', 'Node_5', 'Node_4', 'Node_3', 'Node_2', 'Node_1']

# Can successfully insert after a node in the middle of the linked list
def test_insert_after_middle(list_many):
    list_many.insert_after('Node_4', 'Hello world')
    assert list_many.return_list() == ['Node_6', 'Node_5', 'Node_4', 'Hello world', 'Node_3', 'Node_2', 'Node_1']
# Can successfully insert a node after the last node of the linked list
def test_insert_after_end(list_many):
    list_many.insert_after('Node_1', 'Hello world')
    assert list_many.return_list() == ['Node_6', 'Node_5', 'Node_4', 'Node_3', 'Node_2', 'Node_1', 'Hello world']

# Where k is greater than the length of the linked list
def test_k_is_greater_than_length(list_many):
    assert list_many.kth_from_end(20) == 'K is out of range'

# Where k and the length of the list are the same
def test_k_is_same_length(list_many):
    assert list_many.kth_from_end(6) == 'K is out of range'

# Where k is not a positive integer
def test_k_is_negative(list_many):
    assert list_many.kth_from_end(-4) == 'K is out of range'

# Where the linked list is of a size 1
def test_k_is_in_list_of_one(list_one):
    assert list_one.kth_from_end(0) == 'Node_1'

# “Happy Path” where k is not at the end, but somewhere in the middle of the linked list
def test_k_is_happy():
    new_list = LinkedList()
    new_list.insert(2)
    new_list.insert(8)
    new_list.insert(3)
    new_list.insert(1)
    assert new_list.kth_from_end(2) == 3

# Stretch Goal
# implement a method that finds the node at the middle of the Linked List.
def test_return_middle_even_number_of_nodes(list_many):
    assert list_many.find_middle_node() == 'Node_3'

def test_return_middle_odd_number_of_nodes(list_many):
    list_many.append('Another_Node')
    assert list_many.find_middle_node() == 'Node_2'


# def __str__(self):
#     as_string = 'linked_list: '
#     current = self.head
#     while current:
#         as_string += f""

