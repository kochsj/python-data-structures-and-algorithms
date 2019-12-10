import pytest
from linked_list import Node, Linked_List

# Can successfully instantiate an empty linked list
def test_empty_linked_list():
    instance_of_linked_list = Linked_List()
    assert isinstance(instance_of_linked_list, Linked_List) == True

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

# def __str__(self):
#     as_string = 'linked_list: '
#     current = self.head
#     while current:
#         as_string += f""



# creates linked lists of varrying numbers of nodes:
# one node
@pytest.fixture()
def list_one():
    empty_list = Linked_List()
    empty_list.insert('Node_1')
    return empty_list

# two nodes
@pytest.fixture()
def list_two():
    empty_list = Linked_List()
    empty_list.insert('Node_1')
    empty_list.insert('Node_2')
    return empty_list

# six nodes
@pytest.fixture()
def list_many():
    empty_list = Linked_List()
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
    empty_list = Linked_List()
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

