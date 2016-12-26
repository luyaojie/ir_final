import os


def get_path(root_dir):
    list_dirs = os.walk(root_dir)
    for root, dirs, files in list_dirs:   
        for f in files: 
            yield os.path.join(root, f) 


def extract_result(filename):
    result = open(filename, 'r').readlines()[-1].strip()
    result = result.replace("[", "").replace("]", "")
    result = result.strip()
    result = [r for r in result.split()]
    return result


if __name__ == "__main__":
    import sys
    import os
    for fname in get_path(sys.argv[1]):
        if sys.argv[2] not in fname:
            continue
        r = extract_result(fname)
        if len(r) < 4:
            continue
        print "%s, %s" % (fname, ",".join(r))
