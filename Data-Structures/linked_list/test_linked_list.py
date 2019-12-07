from linked_list import Linked_List, Node

# Can successfully instantiate an empty linked list
def test_empty_linked_list():
    instance_of_linked_list = Linked_List()
    assert isinstance(instance_of_linked_list, Linked_List) == True
# Can properly insert into the linked list
# The head property will properly point to the first node in the linked list
# Can properly insert multiple nodes into the linked list
# Will return true when finding a value within the linked list that exists
# Will return false when searching for a value in the linked list that does not exist
# Can properly return a collection of all the values that exist in the linked list
