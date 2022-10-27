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

marks = int(input("Enter the marks obtained in Engineering Mathematics II : "))
ptr_maths2 = 4 * calc(marks)

marks = int(input("Enter the marks obtained in Seminar : "))
ptr_seminar = 1 * calc(marks)

marks = int(input("Enter the marks obtained in Engineering Physics : "))
ptr_phy = 4 * calc(marks)

marks = int(input("Enter the marks obtained in Engineering Graphics : "))
ptr_eg = 2 * calc(marks)

marks = int(input("Enter the marks obtained in Communication Skils : "))
ptr_cs = 2 * calc(marks)

marks = int(input("Enter the marks obtained in Energy and Environment Engineering : "))
ptr_eee = 2 * calc(marks)

marks = int(input("Enter the marks obtained in Engineering Physics Lab : "))
ptr_phy_lab = 1 * calc(marks)

marks = int(input("Enter the marks obtained in Engineering Graphics Lab : "))
ptr_eg_lab = 2 * calc(marks)

marks = int(input("Enter the marks obtained in Communication Skills Lab : "))
ptr_cs_lab = 1 * calc(marks)

sgpa = (ptr_maths2 + ptr_seminar + ptr_phy + ptr_eg + ptr_cs + ptr_eee + ptr_phy_lab + ptr_eg_lab + ptr_cs_lab)/19
print(f"\nYour SGPA for Second Semester is : {sgpa}")