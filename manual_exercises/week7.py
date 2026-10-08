def squared_numbers(list):
    new_list = []
    for number in list:
        new_list.append(number**2)
    return new_list

numbers = [10, 189, 56]
doubled_number = list(map(lambda x:x*2, numbers))
print(doubled_number)

student_info = [
    {
    "name": "Akintayo Sinmiloluwa",
    "score": 78
    },
    {
    "name": "Obisesan Ephraim",
    "score": 89
    },
    {
    "name": "Rotimi Daniel",
    "score": 56
    },
    {
    "name": "Salau Ali",
    "score": 65
    },
    {
    "name": "Solomon Oluwatomisin",
    "score": 77
    },
    {
    "name": "Alex Fortune",
    "score": 45
    },
    {
    "name": "Famakinde Zion",
    "score": 71
    }
]

sorted_list = sorted(student_info, key = lambda x: x["name"])
print(sorted_list)