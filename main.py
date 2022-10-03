random_object = {
     "Name": "Testy test",
     "Random Data": ["1", "2", "3"]
}

random_object_2 = {
     "Name": "Testyy test",
     "Random Data 1": ["1", "2", "3"],
     "Random Data 2": ["123", "456", "789"]
}

print(random_object)

random_object["Random Data"][1] = "3"

oneplusone = 2

print(random_object_2)

random_object_2[f"Random Data {oneplusone}"][2] = "987"

print(random_object_2)