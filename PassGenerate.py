# Lesser General Public License (LGPL) v3.0 .
# The project has been developed by Saman Ebrahimnezhad .
# Created at Iran (IR) .
# Python 3 .

import random
import string

class PassGenerate:

    def __init__(self):
        pass

    def generate(self, size):
        return ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))

def main():
    app = PassGenerate()

if __name__ == '__main__':
    main()
