import sys
import os
print(sys.path[0])
print(sys.argv[0])
print(os.path.dirname(os.path.realpath(sys.executable)))
print(os.path.dirname(os.path.realpath(sys.argv[0])))
if hasattr(sys, '_MEIPASS'):
    self.appPath = os.path.dirname(os.path.realpath(sys.executable))

