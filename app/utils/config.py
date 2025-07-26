import os
ADMIN_IDS = list(map(int, os.getenv("ADMIN_IDS", "").split(","))) 
