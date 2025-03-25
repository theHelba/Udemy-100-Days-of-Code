capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}


# Nested List in Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

# Print Lille
print(travel_log["France"][1])

# Nested List
nested_list = ["A", "B", ["C", "D"]]

# Print D
print(nested_list[2][1])

# Nesting Dictionaries
travel_log_2 = {
    "France": {
        "num_times_visited": 12,
        "cities_visited": ["Paris", "Lille", "Dijon"],
    },
    "Germany": {
        "num_times_visited": 5,
        "cities_visited": ["Stuttgart", "Berlin"],
    }
}

# Print out Stuttgart
print(travel_log_2["Germany"]["cities_visited"][0])
