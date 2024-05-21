

# def mergesort(array, byfunc=None):

def merge(array, p, q, r, byfunc=None):
    Aleft = array[p:q+1]
    n_left = len(Aleft)
    left = 0
    Aright = array[q+1 : r+1]
    n_right = len(Aright)
    right = 0
    dest = p
    
    
    while left < n_left and right < n_right:
        if byfunc(Aleft[left]) < byfunc(Aright[right]):
            array[dest] = Aleft[left]
            left += 1
        else:
            array[dest] = Aright[right]
            right += 1
        dest += 1
    while left < n_left:
        array[dest] = Aleft[left]
        left += 1
        dest += 1
    while right < n_right:
        array[dest] = Aright[right]
        right += 1
        dest += 1


def mergesort_recursive(array, p, r, byfunc=None):
    if r - p > 0:
        middle = (p + r)//2
        mergesort_recursive(array, p, middle, byfunc)
        mergesort_recursive(array, middle + 1, r, byfunc)
        if sorted(array, key=byfunc) == array:
            return 
        # print(array)
        merge(array, p, middle, r, byfunc)
        # print(array)

def mergesort(array, byfunc=None):
    p = 0
    r = len(array) - 1
    if len(array) <= 1:
        return array
    else:
        return mergesort_recursive(array, p, r, byfunc)
    


class Stack:
    def __init__(self):
        self.__items = []
        
    def push(self, item):
        return self.__items.append(item)

    def pop(self):
        if self.size == 0:
            return None
        else:
            return self.__items.pop()

    def peek(self):
        return self.__items[-1]

    @property
    def is_empty(self):
        return self.size == 0

    @property
    def size(self):
        return len(self.__items)
    
    def __str__(self):
        return str(self.__items)


class EvaluateExpression:
  # copy the other definitions
  # from the previous parts


  valid_char = '0123456789+-*/() '
  operator = '+-*/'
  operand ='0123456789'
  

  def __init__(self, string=""):
      self._expression = string

  @property
  def expression(self):
      return self._expression

  @expression.setter
  def expression(self, new_expr):
      for i in new_expr:
        if i not in self.valid_char:
          new_expr = ''
        else:
          self._expression = new_expr

  def insert_space(self):
      result = ''
      for i in self._expression:
        if i in self.operator:
          result += f" {i} "
        else:
          result += i
      return result


  def process_operator(self, operand_stack, operator_stack):
      element = operator_stack.pop()
      operand2 = operand_stack.pop()
      operand1 = operand_stack.pop()
      if element == '+':
        result = operand1 + operand2
        operand_stack.push(result)
      elif element == '-':
        result = operand1 - operand2
        operand_stack.push(result)
      elif element == '*':
        result = operand1 * operand2
        operand_stack.push(result)
      elif element == '/':
        result = operand1 // operand2
        operand_stack.push(result)
      elif element == '(':
        pass
      # elif element == ')':
      #   self.process_operator(operand_stack, operator_stack)
     
    
    
  def precedence(self, operator):
      if operator in ('+', '-'):
          return 1
      elif operator in ('*', '/'):
          return 2
      return 0
   
  
  def evaluate(self):
      operand_stack = Stack()
      operator_stack = Stack()
      expression = self.insert_space()
      tokens = list(expression)
    
      for i in tokens:
          if i == ' ':
             continue
          elif i in self.operand:
              operand_stack.push(int(i))  
     
          elif i == '+' or i == '-':
          # while (not operator_stack.is_empty) and (operator_stack.peek() != '(' and operator_stack.peek() !=')'):
              while (not operator_stack.is_empty and operator_stack.peek() not in ('(', ')') and 
                    self.precedence(operator_stack.peek()) >= self.precedence(i)):
              # while (not operator_stack.is_empty and operator_stack.peek() not in ('(', ')') ):
                  self.process_operator(operand_stack, operator_stack)
              operator_stack.push(i)

          elif i == '*' or i == '/':
              # while not operator_stack.is_empty:
              while (not operator_stack.is_empty and self.precedence(operator_stack.peek()) >= self.precedence(i)):
                  self.process_operator(operand_stack, operator_stack)
              operator_stack.push(i)

             
          elif i == '(':
              operator_stack.push(i)

  
          elif i == ')':
            print(operator_stack)
            while not operator_stack.is_empty and operator_stack.peek() != '(':
                  self.process_operator(operand_stack, operator_stack)
            print(operand_stack)
            operator_stack.pop()

            
      while not operator_stack.is_empty:
          self.process_operator(operand_stack, operator_stack)
      return operand_stack.pop()
         


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





