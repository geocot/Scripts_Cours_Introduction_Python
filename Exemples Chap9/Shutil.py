"""
import shutil, math
total_mem, used_mem, free_mem = shutil.disk_usage('c:')
print("Mémoire totale: {} GB,"
      " Mémoire utilisée: {} GB,"
      " Mémoire libre: {} GB".format(math.floor(total_mem/10 **9),
                                     math.floor(used_mem/10 **9),
                                     math.floor(free_mem/10 **9)))
"""
import shutil
shutil.copyfile("sauvchar.py", "toto.txt")