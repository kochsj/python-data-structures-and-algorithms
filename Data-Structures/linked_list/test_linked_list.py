from linked_list import Linked_List, Node

# Can successfully instantiate an empty linked list
def test_empty_linked_list():
    instance_of_linked_list = Linked_List()
    assert isinstance(instance_of_linked_list, Linked_List) == True
# Can properly insert into the linked list
def test_instance_of_node():
    assert Node('Node_1').value == 'Node_1'
def test_one_item_in_list():
    empty_list = Linked_List()
    empty_list.insert('Node_1')
    assert empty_list.head and Node('Node_1').next == None
def test_two_items_into_new_list():
    empty_list = Linked_List()
    empty_list.insert('Node_1')
    empty_list.insert('Node_2')
    assert str(empty_list.head) == 'Node_2'
def test_many_items_into_new_list():
    empty_list = Linked_List()
    empty_list.insert('Node_1')
    empty_list.insert('Node_2')
    empty_list.insert('Node_3')
    empty_list.insert('Node_4')
    empty_list.insert('Node_5')
    empty_list.insert('Node_6')
    assert str(empty_list.head) == 'Node_6' and str(empty_list.head.next) == 'Node_5'

# The head property will properly point to the first node in the linked list

# Can properly insert multiple nodes into the linked list
# Will return true when finding a value within the linked list that exists
# Will return false when searching for a value in the linked list that does not exist
# Can properly return a collection of all the values that exist in the linked list
