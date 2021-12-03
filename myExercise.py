import sys

class StudentNotFound(Exception):
    pass

with open(sys.argv[1]) as f:
    if len(sys.argv) == 3:
        inp_names = sys.argv[2].split(",")
        all_names = [line.split(":")[0] for line in f]
        for name in inp_names:
            try:
                if not name in all_names:
                    raise StudentNotFound
            except StudentNotFound:
                print(f"No record of '{name}' was found!")
            else:
                f.seek(0)
                dic = {name : line.split(":")[1].strip("\n").split(",") for line in f if name == line.split(":")[0]}
                print(f"Name: {name}, University: {dic[name][0]},{dic[name][1]}")
    else:
        print("Wrong input!")