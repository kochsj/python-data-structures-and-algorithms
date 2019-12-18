class Dog:
    """
    Takes no parameters
    Creates an instance of a Dog with name and next properties
    """
    def __init__(self):
        self.name = 'Ima dog'
        self.next = None

class Cat:
    """
    Takes no parameters
    Creates an instance of a Cat with name and next properties
    """
    def __init__(self):
        self.name = 'Ima cat'
        self.next =  None

#######################################################
# Actual Queue
#######################################################
class AnimalShelter:
    """
    Class constructor for a queue of 'animals'
    Takes no parameters. Creates an instance of an AnimalShelter with front and end properties.
    Has two methods, enqueue and dequeue.
    Enqueue('cat'/'dog') - Adds a dog or cat to the 'end' of the queue
    Dequeue(['cat'/'dog']) - Removes the cat or dog closest to the front of the queue. Takes an optional parameter, cat or dog, that will return the first in the queue.
    """
    def __init__(self):
        self.front = None
        self.end = None

    def enqueue(self, animal):
        if animal.lower() == 'dog':
            new_dog = Dog()
            if self.end:
                self.end.next = new_dog
                self.end = new_dog
            elif self.front:
                self.front.next = new_dog
                self.end = new_dog
            else:
                self.front = new_dog

        if animal.lower() == 'cat':
            new_cat = Cat()
            if self.end:
                self.end.next = new_cat
                self.end = new_cat
            elif self.front:
                self.front.next = new_cat
                self.end = new_cat
            else:
                self.front = new_cat

        else:
            return 'Dogs and Cats only please.'

    def dequeue(self, pref=''):
        new_queue, front, looking, first = AnimalShelter(), self.front, True, None
        if self.front:
            self.front = front.next
        while front:
            if pref.lower() == 'cat' and looking:
                if isinstance(front, Cat):
                    first = front
                    looking = False
                else:
                    new_queue.enqueue('dog')
                    front = self.front

            if pref.lower() == 'dog'and looking:
                if isinstance(front, Dog):
                    first = front
                    looking = False
                else:
                    new_queue.enqueue('cat')
                    front = self.front

            else:
                return front
        return first                    
        
#######################################################
# OOPS - Linked List Implementation
#######################################################

# class AnimalShelter:
#     def __init__(self, front=None):
#         self.front = front
#         self.end = None

#     def enqueue(self, animal):
#         if animal.lower() == 'dog':
#             new_animal = Dog('Ima dog')
#             if self.end:
#                 self.end.next = new_animal
#                 self.end = new_animal
#             elif self.front:
#                 self.front.next = new_animal 
#                 self.end = new_animal
#             else:
#                 self.front = new_animal

#         if animal.lower() == 'cat':
#             new_animal = Cat('Ima cat')
#             if self.end:
#                 self.end.next = new_animal
#                 self.end = new_animal
#             elif self.front:
#                 self.front.next = new_animal 
#                 self.end = new_animal
#             else:
#                 self.front = new_animal

#         else:
#             return 'Only cats and dogs please.'


#     def dequeue(self, pref):
#         if pref.lower() == 'cat':
#             current, previous = self.front, None
#             while current:
#                 if isinstance(current, Cat):
#                     if previous:
#                         previous.next = current.next
#                         current.next = None
#                         return current
#                     else:
#                         self.front = current.next
#                         current.next = None
#                         return current
#                 else:
#                     previous = current
#                     current = current.next
#             return None

#         if pref.lower() == 'dog':
#             current, previous = self.front, None
#             while current:
#                 if isinstance(current, Dog):
#                     if previous:
#                         previous.next = current.next
#                         current.next = None
#                         return current
#                     else:
#                         self.front = current.next
#                         current.next = None
#                         return current
#                 else:
#                     previous = current
#                     current = current.next
#             return None 

#         else:
#             front = self.front
#             self.front = self.front.next
#             return front

# if __name__ == "__main__":
#     a = 'Dog'
#     b = 'dog'
#     c = 'cat'
#     d = AnimalShelter()
#     d.enqueue(a)
#     d.enqueue(b)
#     d.enqueue(c)
#     e = d.dequeue('cat')
#     f = d.dequeue('dog')
#     print(d.front.next)
