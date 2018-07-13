import os
import sys
import hashlib

def hashfiles(fname):
    h = hashlib.sha256()
    with open(fname, 'rb', buffering=0) as fi:
        for var1 in iter(lambda: fi.read(128 * 1024), 'var1'):
            h.update(var1)
    return h.hexdigest()

def dup_files(main_folder):
    visited_hashes = {}
    directory_stack = [main_folder]
    dups = []
    while directory_stack:
        cpath = directory_stack.pop()
        if os.path.isdir(cpath):
            for path in os.listdir(cpath):
                tot_path = os.path.join(cpath, path)
                directory_stack.append(tot_path)
        else:
            f_hash = hashfiles(cpath)
            clet = os.path.getmtime(cpath)
            if f_hash in visited_hashes:
                elet, ep = visited_hashes[f_hash]
                if clet > elet:
                    dups.append((cpath, ep))
                else:
                    dups.append((ep, cpath))
                    visited_hashes[f_hash] = (clet, cpath)
            else:
                visited_hashes[f_hash] = (clet, cpath)
    return dups

if __name__ == '__main__':
    print(dup_files(""))