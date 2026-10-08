# Contact book
contacts = [ 
    {
        "name": "Akintayo Sinmiloluwa",
        "number": +2349042089471,
        "email": "akintayosinmi@gmail.com"
    },
    {
        "name": "Obeata Israel",
        "number": +2349112828891,
        "email": "israelob@gmail.com"
    },

    {
        "name": "Adenuga Joel",
        "number": +2348028711278,
        "email": "akintayosinmi@gmail.com"
    }
]

set_1 = {1,2}
set_2 = {2,3}
universal_set = set_1 | set_2

#NOTE | is used to rep union in sets and  & is used to rep intersection - is used to rep difference ^ is used to rep symmetric difference where we have all the differences in both of them
print(set_1 | set_2)
print(set_1 & set_2)
print(set_1 - set_2)
print(universal_set - (set_1 & set_2))
print(set_1 ^ set_2)


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

scores = []
names = []

for student in student_info:
    scores.append(student["score"])
    names.append(student["name"])
highest_score = max(scores)
average_score = sum(scores)/len(scores)
print(f"The highest score is {highest_score}")
print(f"The average score is {average_score}")
print("The names in alphabetical order:")
names.sort()
for name in names:
    print(name)