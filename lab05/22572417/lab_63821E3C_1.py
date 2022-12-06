
def get_dict():
    return database

def get_peter_age( database ):
    return age

def get_age( name, database ):
    return age

def update_hour( name, database, hour ):
    return

def remove( name, database ):
    return

def add( name, age, hour, database ):
    return

def get_names_work4( target_hour, database ):
    return names

def main():
    db = get_dict()
    print("Peter age is: {}".format(get_peter_age(db)) )
    name = "jake"
    print("{} age is: {}".format(name, get_age(name, db)) )
    name = "mollie"
    mollie_hour = 9
    print("Update {} hour to {}".format(name, mollie_hour))
    update_hour( name, db, mollie_hour)
    name = "jake"
    print("Remove {} from the database".format(name))
    remove( name, db)
    name = "jane"
    age = 19
    hour = 12
    print("Add {}, age: {}, hour: {} to the database".format(
        name, age, hour))
    add(name, age, hour, db)
    workhr = 8
    print("Name list which works >= {} hours".format(workhr))
    print(get_names_work4(workhr, db))


if __name__ == "__main__":
    main()
