def get_set():
    return my_set

def answer(target, your_set):
    return ret

def answer2(target, your_set):
    return ret

def main():
    namelist = get_set()
    look4person = 'molly'
    print("Set:")
    print(namelist)
    if answer(look4person, namelist) :
        print("Found " + look4person)
    else :
        print("Not found " + look4person)
    if answer2(look4person, namelist) :
        print("Found " + look4person)
    else :
        print("Not found " + look4person)

if __name__ == "__main__":
    main()
