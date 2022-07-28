- What are the built-in data types in Python?

  ```
  There are multiples built-in data types in Python. They are int, float, complex, bool, list, tuple, set, dict, str.
  ```

- What’s the difference between list and tuple?
  ```
  Both list and tuple are used to store the collection of objects. The main difference between the list and tuple is “the list is mutable object whereas tuple is an immutable object”.
  ```
- Explain some methods of the list.

  ```
  1. _append_ – the method is used to add an element to the list. It adds the element to the end of the list.

  > > > a = [1, 2]
  > > > a.append(3)
  > > > a
  > > > [1, 2, 3]

  2. _pop_ – the method is used to remove an element from the list. It will remove the last element if we don’t provide any index as an argument or remove the element at the index if we provide an argument.

  > > > a = [1, 2, 3, 4, 5]
  > > > a.pop()
  > > > 5
  > > > a
  > > > [1, 2, 3, 4]
  > > > a.pop(1)
  > > > 2
  > > > a
  > > > [1, 3, 4]

  3. _remove_ – the method is used to remove an element from the list. We need to provide the element as an argument that we want to remove from the list. It removes the first occurrence of the element from the list.

  > > > a = [1, 2, 2, 3, 4]
  > > > a = [1, 2, 3, 2, 4]
  > > > a.remove(1)
  > > > a
  > > > [2, 3, 2, 4]
  > > > a.remove(2)
  > > > a
  > > > [3, 2, 4]

  4. _sort_ – the method used to sort the list in ascending or descending order.

  > > > a = [3, 2, 4, 1]
  > > > a.sort()
  > > > a
  > > > [1, 2, 3, 4]
  > > > a.sort(reverse=True)
  > > > a
  > > > [4, 3, 2, 1]

  5. reverse – the method is used to reverse the list elements.

  > > > a = [3, 2, 4, 1]
  > > > a.reverse()
  > > > a
  > > > [1, 4, 2, 3]

  clear, insert, count, etc
  ```

- Explain some methods of string

  ```
  1. _split_ the method is used to split the string at desired points. It returns the list as a result.
     > > > a = "This is Geekflare"
     > > > a.split()
     > > > ['This', 'is', 'Geekflare']
     > > > a = "1, 2, 3, 4, 5, 6"
     > > > a.split(", ")
     > > > ['1', '2', '3', '4', '5', '6']
  2. _join_ – the method is used to combine the list of string objects. It combines the string objects with the delimiter
     > > > a = ['This', 'is', 'Geekflare']
     > > > ' '.join(a)
     > > > 'This is Geekflare'
     > > > ', '.join(a)
     > > > 'This, is, Geekflare'

  others capitalize, isalnum, isalpha, isdigit, lower, upper, center, etc
  ```

- Ques
  ```
  > > > a = [1, 2, 3, 4, 5]
  > > > a[-1]
  ```
- Explain some methods of dict

  ```
  1. items – the method returns key: value pairs of dictionaries as a list of tuples.

  > > > a = {1: 'Geekflare', 2: 'Geekflare Tools', 3: 'Geekflare Online Compiler'}
  > > > a.items()
  > > > dict_items([(1, 'Geekflare'), (2, 'Geekflare Tools'), (3, 'Geekflare Online Compiler')])

  2. pop – the method is used to remove the key: value pair from the dictionary. It accepts the key as an argument and removes it from the dictionary.

  > > > a = {1: 2, 2: 3}
  > > > a.pop(2)
  > > > 3
  > > > a
  > > > {1: 2}
  > > > Note: Some other methods of dict are: get, keys, values, clear, etc.
  ```

- What is slicing in Python?

  ```
  Slicing is used to access the subarray from a sequence data type. It returns the data from the sequence data type based on the arguments we provide. It returns the same data type as the source data type.

  Slicing accepts three arguments. They are the start index, end index, and increment step. The syntax of slicing is variable[start:end:step]. Arguments are not mandatory for slicing.

  > > > a = [1, 2, 3, 4, 5]
  > > > a[:] > > > [1, 2, 3, 4, 5]
  > > > a[:3] > > > [1, 2, 3]
  > > > a[3:] > > > [4, 5]
  > > > a[0:5:2] > > > [1, 3, 5]
  ```

- Which data types allow slicing?
  ```
  We can use slicing on list, tuple, and str data types.
  ```
- What are list and dictionary comprehensions?

  ```
  List and dictionary comprehensions are syntactic sugar for the for-loops.

  > > > a = [i for i in range(10)]
  > > > a
  > > > [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  > > > a = {i: i + 1 for i in range(10)}
  > > > a
  > > > {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10}
  ```

- How does the range function work?

  ```
  The range function returns the sequence of numbers between the start to stop with a step increment. The syntax of the range function is range(start, stop[, step]).

  > > > list(range(10))
  > > > [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  > > > list(range(1, 10))
  > > > [1, 2, 3, 4, 5, 6, 7, 8, 9]
  > > > list(range(1, 10, 2))
  > > > [1, 3, 5, 7, 9]
  ```

- What’s the difference between normal function and lambda function?

  ```
  The functionality of both normal functions and lambda functions are similar. But, we need to write some extra code in normal functions compared to lambda functions for the same functionality.

  Lambda functions come in handy when there is a single expression.
  ```

- How to instantiate a class in Python?

  ```
  We can create an instance of a class in Python by simply calling it like function. We can pass the required attributes for the object in the same way as we do for function arguments.

  > > > class Car:
  > > > ... def **init**(self, color):
  > > > ... self.color = color
  > > > ...
  > > > red_car = Car('red')
  > > > red_car.color
  > > > 'red'
  > > > green_car = Car('green')
  > > > green_car.color
  > > > 'green'
  ```

- What is self in Python?

  ```
  The self represents the object of the class. It’s used to access the object attributes and methods inside the class for the particular object.
  ```

- What is the **init** method?

  ```
  The **init** is the constructor method similar to the constructors in other OOP languages. It executes immediately when we create an object for the class. It’s used to initialize the initial data for the instance.
  ```

- How do you implement inheritance in Python?

  ```
  We can pass the parent class to the child class as an argument. And we can invoke the init method parent class in the child class.

  > > > class Animal:
  > > > ... def **init**(self, name):
  > > > ... self.name = name
  > > > ...
  > > > class Animal: e):
  > > > ... def **init**(self, name):
  > > > ... self.name = name
  > > > ...
  > > > ... def display(self):
  > > > ... print(self.name)
  > > > class Dog(Animal): e):ame)
  > > > ... def **init**(self, name):
  > > > ... super().**init**(name)
  > > > ...
  > > > doggy = Dog('Tommy')
  > > > doggy.display()
  > > > Tommy
  ```

- What is shallow and deep copy?

  ```
  1. Shallow Copy: it creates the exact copy as the original without changing references of the objects. Now, both copied and original objects refer to the same object references. So, changing one object will affect the other.

  The copy method from the copy module is used for the shallow copy.

  > > > from copy import copy
  > > > a = [1, [2, 3]]
  > > > b = copy(a)
  > > > a[1].append(4)
  > > > a
  > > > [1, [2, 3, 4]]
  > > > b
  > > > [1, [2, 3, 4]]

  2. Deep Copy: it copies the values of the original object recursively into the new object. We have to use the slicing or deepcopy function from the copy module for the deep copying.

  > > > from copy import deepcopy
  > > > a = [1, [2, 3]]
  > > > b = deepcopy(a)
  > > > a[1].append(4)
  > > > a
  > > > [1, [2, 3, 4]]
  > > > b
  > > > [1, [2, 3]]
  > > > b[1].append(5)
  > > > a
  > > > [1, [2, 3, 4]]
  > > > b
  > > > [1, [2, 3, 5]]
  ```

- What are iterators?

  ```
  Iterators are objects in Python which remember their state of iteration. It initializes the data with the **iter** method and returns the next element using the **next** method.

  We need to call the next(iterator) to get the next element from the iterator. And we can convert a sequence data type to an iterator using the iter built-in method.

  > > > a = [1, 2]
  > > > iterator = iter(a)
  > > > next(iterator)
  > > > 1
  > > > next(iterator)
  > > > 2
  > > > next(iterator)
  > > > Traceback (most recent call last):
  > > > File "<stdin>", line 1, in <module>
  > > > StopIteration
  ```

- What are generators?

  ```
  Generators are the functions that return an iterator like a generator object. It uses the yield to generate the data.

  > > > def numbers(n):
  > > > ... for i in range(1, n + 1):
  > > > ... yield i
  > > > ...
  > > > \_10 = numbers(10)
  > > > next(\_10)
  > > > 1
  > > > next(\_10)
  > > > 2
  > > > next(\_10)
  > > > 3
  > > > next(\_10)
  > > > 4
  ```
