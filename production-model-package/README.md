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
 
    