# lets talk about TOX
.tox is generic virutalenv command line test tool.
It means we don't have to worry about different operating system
whether you are working on mac, windows or linux.
- we don't have to worry about setting up python paths, configuring environment variables.
We do all this in tox.ini file.

    > go ahead and install -- pip install tox
- you might face some issues in the beginning on MAX_PATH limitation.
    - To solve follow this link [https://docs.python.org/3/using/windows.html]()
    and open you registry editor and change the variables given in the documentation.
    
For more on Tox read [here](https://christophergs.com/python/2020/04/12/python-tox-why-use-it-and-tutorial/)

# Pytest
I have used Pytest framework makes it easy to write small tests, yet
scales to support complex functional testing for application and libraries.
If you have used Python unittest libraries, this one offers a richer statement during failures,
which makes debugging easier. 

Features:
- Detailed info on failing assert statements (no need to remember self.assert* names)
- Auto-discovery of test modules and functions
- Modular fixtures for managing small or parametrized long-lived test resources
- Can run unittest (including trial) and nose test suites out of the box 
- Rich plugin architecture, with over 315+ external plugins and thriving community
Don't worry if I have intimidated you, you only need to remember fixtures.
    > what the hell is fixtures

In simple words how your testing module work step by step, fixture is all about it. 
I cannot explain better than this documentation, it's a must read. (https://docs.pytest.org/en/6.2.x/fixture.html#fixture)
## for example
Write this simple python script and save it say square.py
```python
def square(x):
    return x**2
```
Now open a new file name it whatever you want and import this function
```python
from my_folder import square
def test_square_gives_correct_value():
    #when
    subject = square(2)
    #then
    assert subject == 4
```
Now open the terminal from the same terminal and just type 'pytest' you will get your result.
