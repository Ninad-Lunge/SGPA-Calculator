def calc(pointer):

    if marks<=100 and marks>=91:
        return 10
    elif marks<=90 and marks>=86:
        return 9
    elif marks<=85 and marks>=81:
        return 8.5
    elif marks<=80 and marks>=76:
        return 8
    elif marks<=75 and marks>=71:
        return 7.5
    elif marks<=70 and marks>=66:
        return 7
    elif marks<=65 and marks>=61:
        return 6.5
    elif marks<=60 and marks>=56:
        return 6
    elif marks<=55 and marks>=51:
        return 5.5
    elif marks<=50 and marks>=40:
        return 5
    else:
        return 0

marks = int(input("Enter the marks obtained in Engineering Mathematics I : "))
ptr_maths = 4 * calc(marks)

marks = int(input("Enter the marks obtained in Engineering Chemistry : "))
ptr_chem = 4 * calc(marks)

marks = int(input("Enter the marks obtained in Engineering Mechanics : "))
ptr_mech = 3 * calc(marks)

marks = int(input("Enter the marks obtained in Computer Programming in C : "))
ptr_cp = 3 * calc(marks)

marks = int(input("Enter the marks obtained in Workshop Practices : "))
ptr_ws = 2 * calc(marks)

marks = int(input("Enter the marks obtained in Engineering Chemistry Lab : "))
ptr_chem_lab = 1 * calc(marks)

marks = int(input("Enter the marks obtained in Engineering Mechanics Lab : "))
ptr_mech_lab = 1 * calc(marks)

sgpa = (ptr_maths + ptr_chem + ptr_mech + ptr_cp + ptr_ws + ptr_chem_lab + ptr_mech_lab)/18
print(f"\nYour SGPA for First Semester is : {sgpa}")

