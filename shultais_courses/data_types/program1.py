import sys
disk, catalog1, catalog2, filename = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
source = disk + ":" + "\\" + catalog1 + "\\" + catalog2 + "\\" + filename
print(disk + ":", catalog1, catalog2, filename, sep="\\")
print("-" * len(source))
# D:\sources\python\task.py
# -------------------------
