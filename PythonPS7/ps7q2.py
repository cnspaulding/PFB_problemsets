#!/usr/bin/env python3

import re

poem_file = open('Python_07_nobody.txt', 'r')
poem= poem_file.read()
Caitlin_file = open('Caitlin.txt', 'w')

Caitlin = re.sub(r'Nobody', 'Caitlin', poem)
print(Caitlin)

Caitlin_file.write(Caitlin)

Caitlin_file.close()

