# grades.py

def get_student_data():
    students = {}
    
    n = int(input("Enter number of students: "))
    
    for _ in range(n):
        name = input("Enter student name: ")
        score = int(input("Enter score: "))
        students[name] = score
    
    return students


def calculate_average(data):
    return sum(data.values()) / len(data)


def top_student(data):
    name = max(data, key=data.get)
    return name.upper(), data[name]


def display_results(data):
    avg = calculate_average(data)
    name, score = top_student(data)
    
    print(f"Average Score: {avg:.2f}")
    print(f"Top Student: {name} ({score})")


if __name__ == "__main__":
    students = get_student_data()
    display_results(students)