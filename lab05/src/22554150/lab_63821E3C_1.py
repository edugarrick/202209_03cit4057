
def get_dict():
    database= {"annie": { "age":28, "hours":8 },
    "jake": { "age":23, "hours":8 },
    "mollie": { "age":29, "hours":4 },
    "peter": { "age":34, "hours":7.5 },  }
    return database

def get_peter_age( database ):
    age=database["peter"]["age"]
    return age

def get_age( name, database ):
    age=database[name]["age"]
    return age

def update_hour( name, database, hour ):
    database[name]["hours"] = hour
    return

def remove( name, database ):
    del ( database[name] )
    return

def add( name, age, hour, database ):
    database[name] = {"age": age, "hours": hour}
    return

def get_names_work4( target_hour, database ):
    names= []
    for staff_name, staff_data in database.items():
        if staff_data["hours"] >=target_hour :
            names.append(staff_name)
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
