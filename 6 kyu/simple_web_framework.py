'''
In this Kata, you have to design a simple routing class for a web framework.

The router should accept bindings for a given url, http method and an action.

Then, when a request with a bound url and method comes in, it should return the result of the action.

Example usage:

router = Router()
router.bind('/hello', 'GET', lambda: 'hello world')

router.runRequest('/hello', 'GET') // returns 'hello world'
When asked for a route that doesn't exist, router should return:

'Error 404: Not Found'
'''


class Router(object):
    def __init__(self):
        self.req = {}
        
    def bind(self, path, meth, act):
        self.req[(path, meth)] = act
    
    def runRequest(self, path, meth):
        return self.req.get((path, meth), lambda: "Error 404: Not Found")()
