'''
I often find that I end up needing to write a function to return multiple values, in this case I would often split it up into two different functions but then I have to spend time thinking of a new function name! Wouldn't it be great if I could use same name for a function again and again...

In this kata your task is to make a decorator, FuncAdd which will allow function names to be reused and when called all functions with that name will be called (in order) and the results returned as a tuple.

@FuncAdd
def foo():
    return 'Hello'

@FuncAdd
def foo():
    return 'World'

foo() --> ('Hello', 'World')
As well as this you will have to implement two more things, a way of deleting a particular function, and a way of deleting all stored functions. The delete method must work as follows:

@FuncAdd
def foo():
    return 'Hello'

FuncAdd.delete(foo) # Delete all foo() functions only
foo() # Should raise NameError
And the clear method must work like this:

@FuncAdd
def foo():
    return 'Hello'

FuncAdd.clear() # Delete all decorated functions
foo() # Should raise NameError
'''


from collections import defaultdict

class FuncAdd:
    functions = defaultdict(list)

    def __init__(self, func):
        self.name = func.__name__
        self.functions[func.__name__].append(func)

    def __call__(self, *args, **kwargs):
        result = tuple(func(*args, **kwargs) for func in self.functions[self.name])
        if result:
            return result
        else:
            raise NameError(f"name '{self.name}' is not defined")
    
    @classmethod
    def delete(cls, func):
        del cls.functions[func.name]

    @classmethod
    def clear(cls):
        cls.functions.clear()
