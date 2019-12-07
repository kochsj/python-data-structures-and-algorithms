import pytest
from linked_list import Linked_List, Node

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

# Can properly return a collection of all the values that exist in the linked list
def test_correct_collection_of_list_items_one(list_one):
    assert list_one.return_list() == ['Node_1']

def test_correct_collection_of_list_items_two(list_two):
    assert list_two.return_list() == ['Node_2', 'Node_1']

@pytest.fixture()
def list_one():
    empty_list = Linked_List()
    empty_list.insert('Node_1')
    return empty_list

@pytest.fixture()
def list_two():
    empty_list = Linked_List()
    empty_list.insert('Node_1')
    empty_list.insert('Node_2')
    return empty_list

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


