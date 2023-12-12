class ArrayStack :
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None]*self.capacity
        self.top = -1

    def isEmpty(self) :
        return self.top == -1
   
    def isFull (self):
        return self.top == self.capacity
   
    def push(self, e):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = e
        else: pass

    def pop( self ):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top+1]
        else: pass

    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else: pass

def precedence(op):
    if op=='(' or op==')': return 0
    elif op=='+' or op=='-': return 1
    elif op=='*' or op=='/': return 2
    else : return -1

def Infix2Postfix (expr):
    s = ArrayStack(100)
    output = []
    for term in expr :
        if term in '(':
            s.push('(')

        elif term in ')':
            while not s.isEmpty():
                op = s.pop()
                if op=='(':
                    break
                else:
                    output.append(op)
        elif term in "+-*/":
            while not s.isEmpty() :
                op = s.peek()
                if( precedence(term) <= precedence(op)):
                    output.append(op)
                    s.pop()
                else: break
            s.push(term)
        else:
            output.append(term)

    while not s.isEmpty() :
        output.append(s.pop())
    return output