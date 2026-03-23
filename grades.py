# grades.py

students = {
    "John": 70,
    "Kelvin": 85,
    "Mercy": 60
}

# Calculate average score
def calculate_average(data):
    total = sum(data.values())
    average = total / len(data)
    return average

# Find top student
def top_student(data):
    name = max(data, key=data.get)
    score = data[name]
    return name.upper(), score

# Display results
def display_results(data):
    avg = calculate_average(data)
    top_name, top_score = top_student(data)
    
    print(f"Average Score: {avg:.2f}")
    print(f"Top Student: {top_name} ({top_score})")


# Run program
if __name__ == "__main__":
    display_results(students)