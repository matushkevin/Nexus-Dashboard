import sys
import os

# Add your project folder to the path
project_home = '/home/YOUR_USERNAME/nexus-dashboard'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

from app import app as application
