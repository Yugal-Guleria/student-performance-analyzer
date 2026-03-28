class_choice = input("In which class you study 10th or 12th? ")

if class_choice == "10th" or class_choice == "10":
    print("Your subject is Maths , Hindi , English , Science , Social science ")

    sub1 = "Maths"
    sub2 = "Hindi"
    sub3 = "English"
    sub4 = "Science"
    sub5 = "Social Science"

    m1 = int(input(f"Enter your {sub1} marks: "))
    m2 = int(input(f"Enter your {sub2} marks: "))
    m3 = int(input(f"Enter your {sub3} marks: "))
    m4 = int(input(f"Enter your {sub4} marks: "))
    m5 = int(input(f"Enter your {sub5} marks: "))

    print("\n" + "="*50)
    print("FINAL RESULT - CLASS 10TH")
    print("="*50)
    for s,m in [(sub1,m1),(sub2,m2),(sub3,m3),(sub4,m4),(sub5,m5)]:
        if m >= 75:
            print(f"{s}: {m}% - Excellent")
        elif m >= 50:
            print(f"{s}: {m}% - Good")
        elif m >= 33:
            print(f"{s}: {m}% - Pass")
        else:
            print(f"{s}: {m}% - Fail")
    total=(m1+m2+m3+m4+m5)
    pct=(total/500)*100
    print(f"Total: {total}/500 ({pct:.1f}%)")
    print("="*50)

elif class_choice == "12th" or class_choice == "12":
    stream = input("What is your Stream Biology or Maths or Both? ")

    if stream == "Biology":
        sub1, sub2, sub3, sub4 = "Physics", "Chemistry", "Biology", "English"
        m1 = int(input(f"Enter your {sub1} marks: "))
        m2 = int(input(f"Enter your {sub2} marks: "))
        m3 = int(input(f"Enter your {sub3} marks: "))
        m4 = int(input(f"Enter your {sub4} marks: "))
        print("\n" + "="*50)
        print("FINAL RESULT - CLASS 12TH (Biology)")
        print("="*50)
        for s,m in [(sub1,m1),(sub2,m2),(sub3,m3),(sub4,m4)]:
            if m >= 75:
                print(f"{s}: {m}% - Excellent")
            elif m >= 50:
                print(f"{s}: {m}% - Good")
            elif m >= 33:
                print(f"{s}: {m}% - Pass")
            else:
                print(f"{s}: {m}% - Fail")
        total=(m1+m2+m3+m4)
        pct=(total/400)*100
        print(f"Total: {total}/400 ({pct:.1f}%)")
        print("="*50)

    elif stream == "Maths":
        sub1, sub2, sub3, sub4 = "Physics", "Chemistry", "Maths", "English"
        m1 = int(input(f"Enter your {sub1} marks: "))
        m2 = int(input(f"Enter your {sub2} marks: "))
        m3 = int(input(f"Enter your {sub3} marks: "))
        m4 = int(input(f"Enter your {sub4} marks: "))
        print("\n" + "="*50)
        print("FINAL RESULT - CLASS 12TH (Maths)")
        print("="*50)
        for s,m in [(sub1,m1),(sub2,m2),(sub3,m3),(sub4,m4)]:
            if m >= 75:
                print(f"{s}: {m}% - Excellent")
            elif m >= 50:
                print(f"{s}: {m}% - Good")
            elif m >= 33:
                print(f"{s}: {m}% - Pass")
            else:
                print(f"{s}: {m}% - Fail")
        total=(m1+m2+m3+m4)
        pct=(total/400)*100
        print(f"Total: {total}/400 ({pct:.1f}%)")
        print("="*50)

    elif stream == "Both" or stream == "both":
        sub1, sub2, sub3, sub4, sub5 = "Physics", "Chemistry", "Biology", "Maths", "English"
        m1 = int(input(f"Enter your {sub1} marks: "))
        m2 = int(input(f"Enter your {sub2} marks: "))
        m3 = int(input(f"Enter your {sub3} marks: "))
        m4 = int(input(f"Enter your {sub4} marks: "))
        m5 = int(input(f"Enter your {sub5} marks: "))
        print("\n" + "="*50)
        print("FINAL RESULT - CLASS 12TH (Both)")
        print("="*50)
        for s,m in [(sub1,m1),(sub2,m2),(sub3,m3),(sub4,m4),(sub5,m5)]:
            if m >= 75:
                print(f"{s}: {m}% - Excellent")
            elif m >= 50:
                print(f"{s}: {m}% - Good")
            elif m >= 33:
                print(f"{s}: {m}% - Pass")
            else:
                print(f"{s}: {m}% - Fail")
        total=(m1+m2+m3+m4+m5)
        pct=(total/500)*100
        print(f"Total: {total}/500 ({pct:.1f}%)")
        print("="*50)

else:
    print("Invalid class")