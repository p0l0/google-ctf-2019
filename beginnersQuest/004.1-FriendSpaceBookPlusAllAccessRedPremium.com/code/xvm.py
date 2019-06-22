import sys


def palindrome(num):
  return str(num) == str(num)[::-1]


# Prime Test
def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n % 2 == 0: return False
  if n < 9: return True
  if n % 3 == 0: return False
  r = int(n ** 0.5)
  f = 5
  while f <= r:
    if n % f == 0: return False
    if n % (f + 2) == 0: return False
    f += 6
  return True

# Implements a simple stack-based VM
class VM:

  def __init__(self, rom):
    self.rom = rom
    self.accumulator1 = 0
    self.accumulator2 = 0
    self.instruction_pointer = 1
    self.stack = []
    self.hist = []

  def step(self):
    cur_ins = self.rom[self.instruction_pointer]
    htmp = [self.instruction_pointer]
    k = 0
    while k <= VM.OPERATIONS_LEN.get(cur_ins,0) and ((self.instruction_pointer +k)  < len(self.rom)) :
      htmp.append(self.rom[self.instruction_pointer+k])
      k += 1
    self.hist.append(htmp)
    if len(self.hist) > 50:
      self.hist.pop(0)

    self.instruction_pointer += 1

    fn = VM.OPERATIONS.get(cur_ins, None)

    if cur_ins[0] == '🖋':
      return
    if fn is None:
      raise RuntimeError("Unknown instruction '{}' at {}".format(
          repr(cur_ins), self.instruction_pointer - 1))
    else:
      fn(self)

  def add(self):
    self.stack.append(self.stack.pop() + self.stack.pop())



  def sub(self):
    a = self.stack.pop()
    b = self.stack.pop()
    self.stack.append(b - a)

  def if_zero(self):
    if self.stack[-1] == 0:
      while self.rom[self.instruction_pointer] != 'fi':
        if self.rom[self.instruction_pointer] in ['jump_to', 'jump_top']:
          break
        self.step()
    else:
      self.find_first_endif()
      self.instruction_pointer += 1

  def if_not_zero(self):
    if self.stack[-1] != 0:
      while self.rom[self.instruction_pointer] != 'fi':
        if self.rom[self.instruction_pointer] in ['jump_to', 'jump_top']:
          break
        self.step()
    else:
      self.find_first_endif()
      self.instruction_pointer += 1

  def find_first_endif(self):
    while self.rom[self.instruction_pointer] != 'fi':
      self.instruction_pointer += 1

  def jump_to(self):
    marker = self.rom[self.instruction_pointer]
    if marker[0] != '💰':
      print('Incorrect symbol : ' + marker[0])
      raise SystemExit()
    marker = '🖋' + marker[1:]
    self.instruction_pointer = self.rom.index(marker) + 1

  def jump_top(self):
    self.instruction_pointer = self.stack.pop()

  def exit(self):
    print('\nDone.')
    raise SystemExit()

  def print_top(self):
    sys.stdout.write(chr(self.stack.pop()))
    sys.stdout.flush()

  def push(self):
    if self.rom[self.instruction_pointer] == 'acc1':
      self.stack.append(self.accumulator1)
    elif self.rom[self.instruction_pointer] == 'acc2':
      self.stack.append(self.accumulator2)
    else:
      raise RuntimeError('Unknown instruction {} at position {}'.format(
          self.rom[self.instruction_pointer], str(self.instruction_pointer)))
    self.instruction_pointer += 1

  def pop(self):
    if self.rom[self.instruction_pointer] == 'acc1':
      self.accumulator1 = self.stack.pop()
    elif self.rom[self.instruction_pointer] == 'acc2':
      self.accumulator2 = self.stack.pop()
    else:
      raise RuntimeError('Unknown instruction {} at position {}'.format(
          self.rom[self.instruction_pointer], str(self.instruction_pointer)))
    self.instruction_pointer += 1

  def pop_out(self):
    self.stack.pop()

  def load(self):
    num = 0

    if self.rom[self.instruction_pointer] == 'acc1':
      acc = 1
    elif self.rom[self.instruction_pointer] == 'acc2':
      acc = 2
    else:
      raise RuntimeError('Unknown instruction {} at position {}'.format(
          self.rom[self.instruction_pointer], str(self.instruction_pointer)))
    self.instruction_pointer += 1

    num = int(self.rom[self.instruction_pointer])
    self.instruction_pointer += len(self.rom[self.instruction_pointer])

    if acc == 1:
      self.accumulator1 = num
    else:
      self.accumulator2 = num

    self.instruction_pointer += 1

  def clone(self):
    self.stack.append(self.stack[-1])

  def multiply(self):
    a = self.stack.pop()
    b = self.stack.pop()
    self.stack.append(b * a)

  def divide(self):
    a = self.stack.pop()
    b = self.stack.pop()
    self.stack.append(b // a)

  def modulo(self):
    a = self.stack.pop()
    b = self.stack.pop()
    self.stack.append(b % a)

  def xor(self):
    a = self.stack.pop()
    b = self.stack.pop()
    self.stack.append(b ^ a)

  def ppp(self):
    x = self.stack.pop()
    x += 1
    while not (palindrome(x) and is_prime(x)):
      x += 1
    self.stack.append(x)



  OPERATIONS_LEN = {
      'add': 0,
      'clone': 0,
      'divide': 0,
      'if_zero': 3,
      'if_not_zero': 3,
      'jump_to': 1,
      'load': 2,
      'modulo': 0,
      'multiply': 0,
      'pop': 1,
      'pop_out': 0,
      'print_top': 0,
      'push': 1,
      'sub': 0,
      'xor': 0,
      'jump_top': 0,
      'exit': 0,
      'ppp':  0
  }

  OPERATIONS = {
    'add': add,
    'clone': clone,
    'divide': divide,
    'if_zero': if_zero,
    'if_not_zero': if_not_zero,
    'jump_to': jump_to,
    'load': load,
    'modulo': modulo,
    'multiply': multiply,
    'pop': pop,
    'pop_out': pop_out,
    'print_top': print_top,
    'push': push,
    'sub': sub,
    'xor': xor,
    'jump_top': jump_top,
    'exit': exit,
    'ppp': ppp
  }


if __name__ == '__main__':
  if len(sys.argv) != 2:
    print('Missing program')
    raise SystemExit()

  with open(sys.argv[1], 'r') as f:
    print('Running ....')
    all_ins = ['']
    all_ins.extend(f.read().split())
    i = 0
    new_ins = []
    while i < len(all_ins):
      new_ins.append(all_ins[i])
      if i > 1 and all_ins[i-2] == "load":
        k = len(all_ins[i])
        while k > 0 :
          new_ins.append('')
          k -= 1
      i += 1

    vm = VM(new_ins)

    while 1:
      vm.step()
