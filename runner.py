import unittest
from datetime import datetime

loader = unittest.TestLoader()
start_dir = './tests'
suite = loader.discover(start_dir)
now = datetime.now()
datetime = now.strftime("%d.%m.%Y_%H-%M-%S")
log_file = 'Dog_TESTREPORT_' + datetime + '.txt'

if __name__ == '__main__':
    with open(log_file, "w") as f:
        runner = unittest.TextTestRunner(f, verbosity=2)
        result = runner.run(suite)
