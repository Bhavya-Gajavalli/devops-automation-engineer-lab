# Python automation script
# Collects basic system info — useful in DevOps audits

import os
import platform

print("System:", platform.system())
print("Release:", platform.release())
print("CPU cores:", os.cpu_count())

# Shows current working directory
print("Working directory:", os.getcwd())
