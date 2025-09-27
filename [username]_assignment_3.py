student_name = "YourName"
current_gpa = 3.2
study_hours = 20
social_points = 50
stress_level = 35

# --- Step 1: Foundation: display welcome and starting stats (Test Case 1) ---
print(f"Welcome, {student_name}, to the College Life Adventure Game!")
print("Starting stats:")
print(f"  GPA: {current_gpa}")
print(f"  Study hours available this semester: {study_hours}")
print(f"  Social points: {social_points}")
print(f"  Stress level: {stress_level}")
print("-" * 50)

# --- Step 2: Course Planning Decision (if/elif/else + comparison ops) ---
print("Choose your course load:")
print("A) Light (12 credits)")
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")
choice = input("Your choice (A/B/C): ").strip().upper()

if choice == "A":
    print("You chose Light course load.")
    if current_gpa < 2.5:
        study_hours += 10
        stress_level -= 5
        print("Low GPA -> extra study time allocated to recover.")
    elif current_gpa >= 3.5:
        social_points += 10
        stress_level -= 10
        print("High GPA -> you can safely socialize more.")
    else:
        study_hours += 5
        stress_level -= 3
        print("Moderate GPA -> modest adjustments made.")
elif choice == "B":
    print("You chose Standard course load.")
    if current_gpa >= 3.0 and current_gpa < 3.7:
        study_hours += 0
        stress_level += 5
        print("You maintain your balance but stress rises slightly.")
    elif current_gpa < 3.0:
        study_hours += 5
        stress_level += 8
        print("You need to study more to keep up with the standard load.")
    else:
        social_points += 5
        stress_level += 2
        print("You handle the load well; small social boost.")
elif choice == "C":
    print("You chose Heavy course load.")
    if current_gpa >= 3.5:
        study_hours += 15
        stress_level += 15
        social_points -= 10
        print("High GPA allows you to take a heavy load, but it's stressful.")
    else:
        study_hours += 20
        stress_level += 25
        social_points -= 20
        print("Heavy load with lower GPA is risky — prepare for long hours.")
else:
    print("Invalid course load option chosen. No changes made.")
print("-" * 50)
