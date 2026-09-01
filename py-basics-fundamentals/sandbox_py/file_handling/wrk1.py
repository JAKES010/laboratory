total_score = 0
student_count = 0

with open("scores.txt", "r") as file:
    for content in file :
        content = content.strip()
        name_char, score_char = content.split(",")
        int_char = int(score_char)
        print(f"{name_char} scored {int_char}")
        total_score += int_char
        student_count +=1

    if student_count > 0 :
        average = total_score/student_count
    print(f"Average Score: {average}")
 


