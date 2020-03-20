# python-design-patterns
This repo contains design pattern implementations in python

## Usage ##
#### flyweight design pattern ####
Reference: https://www.geeksforgeeks.org/flyweight-design-pattern/

##### Sample Code #####
```python
from flyweight import flyweight

@flyweight
class Sample():
    def __init__(self, val=None):
        self.val = val if val else 100
```

###### Execution ######
```bash
>>> s1 = Sample()
>>> s2 = Sample()
>>> s1 == s2
True
>>> s1
<__main__.Sample object at 0x00000229CB26DE80>
>>> s2
<__main__.Sample object at 0x00000229CB26DE80>
>>> s3 = Sample(120)
>>> s4 = Sample(120)
>>> s3 == s4
True
>>> s3
<__main__.Sample object at 0x00000229CB26DEE0>
>>> s4
<__main__.Sample object at 0x00000229CB26DEE0>
>>> s1 == s3
False
```
