import pandas as pd

df = pd.read_csv("./csv_files/manual_text.txt", sep = "\t", header=None, names=["line_text"])

# . Counts apply directly to that single text column
line_count = len(df)
word_count = df["line_text"].str.split().str.len().sum()
char_count = df["line_text"].str.len().sum()

print(f"Lines: {line_count} | Words: {word_count} | Characters: {char_count}")
print(line_count)

# writing to
data2 = {'name': ["Samuel", "Esther", "Joy"],
        'score': [76, 78, 82],
        'gender': ['Male', "Female", "Female"]}
df2 = pd.DataFrame(data2)
df2.to_csv("student_info", index=False)
# reading
df3 = pd.read_csv("./csv_files/Iris.csv")
print(df3)


file_name = "students.csv"

data = {'name': ["Paul", "David", "Sarah"],
        'age': [18, 16, 17],
        'gender': ['Male', "Male", "Female"]}
df4 = pd.DataFrame(data)
df4.to_csv(file_name, index = False)
print(df4.info())

# VIEW RECORDS
print("--- Current Database ---")
print(df4)

# ADD RECORD
new_student = pd.DataFrame({'name': ['Alex'], 'age': [19], 'gender': ['Male']})
df4 = pd.concat([df4, new_student], ignore_index=True)
df4.to_csv(file_name, index=False)  # Persist to file

# DELETE RECORD (e.g., delete 'David')
df4 = df4[df4['name'] != 'David']
df4.to_csv(file_name, index=False)  # Persist to file

print("\n--- Updated Database ---")
print(df4)