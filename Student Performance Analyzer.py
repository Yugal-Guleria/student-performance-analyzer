class_choice = input("In which class you study 10th or 12th? ")

if class_choice == "10th" or class_choice == "10":
    print("Your subject is Maths , Hindi , English , Science , Social science ")
    math = int(input("Enter your Maths marks out of 100: "))
    hindi = int(input("Enter your Hindi marks out of 100: "))
    english = int(input("Enter your English marks out of 100: "))
    science = int(input("Enter your Science marks out of 100: "))
    sst = int(input("Enter your Social Science marks out of 100: "))
    
    # Final Result
    print("\n" + "="*50)
    print("FINAL RESULT - CLASS 10TH")
    print("="*50)
    
    if math > 50:
        print(f"Maths: {math}% - Strong concepts. Keep practicing for better expression")
    elif math >= 33:
        print(f"Maths: {math}% - Understanding is good. Improve by practicing problems regularly")
    else:
        print(f"Maths: {math}% - Focus on basic concepts and formulas. Practice more daily")
    
    if hindi > 50:
        print(f"Hindi: {hindi}% - Strong language skills. Keep practicing for better expression")
    elif hindi >= 33:
        print(f"Hindi: {hindi}% - Understanding is good. Improve by practicing writing and revisions")
    else:
        print(f"Hindi: {hindi}% - Focus on grammar and writing skills. Practice reading and writing daily")
    
    if english > 50:
        print(f"English: {english}% - Strong language skills. Keep practicing for better expression")
    elif english >= 33:
        print(f"English: {english}% - Understanding is good. Improve by practicing writing and revisions")
    else:
        print(f"English: {english}% - Focus on grammar and vocabulary. Practice reading and writing daily")
    
    if science > 50:
        print(f"Science: {science}% - Strong grasp of concepts. Keep revising to maintain performance")
    elif science >= 33:
        print(f"Science: {science}% - Understanding is good. Improve by revising regularly and practicing")
    else:
        print(f"Science: {science}% - Focus on concepts clearly. Revise theory and practice diagrams daily")
    
    if sst > 50:
        print(f"Social Science: {sst}% - Strong grasp of concepts. Keep revising to maintain performance")
    elif sst >= 33:
        print(f"Social Science: {sst}% - Understanding is good. Improve by revising regularly and practicing")
    else:
        print(f"Social Science: {sst}% - Focus on concepts clearly. Revise theory and practice daily")
    
    total = math + hindi + english + science + sst
    percentage = total / 5
    print("-"*50)
    print(f"Total: {total}/500")
    print(f"Average: {percentage:.2f}%")
    
    if percentage > 50:
        print("Overall: Strong performance. Keep practicing for better expression")
    elif percentage >= 33:
        print("Overall: Understanding is good. Improve by practicing regularly")
    else:
        print("Overall: Focus on basic concepts. Practice more daily")
    print("="*50 + "\n")
    
elif class_choice == "12th" or "12":
    stream = input("What is your Stream Biology or Maths or Both ?  ")
    if stream == "Biology":
        print("Your Subjects are Physics , Chemistry , Biology , English ")
        physics = int(input("Enter your Physics marks "))
        chemistry = int(input("Enter your Chemistry marks"))
        biology = int(input("Enter your Biology marks "))
        english = int(input("Enter your English marks "))
        
        print("\n" + "="*50)
        print("FINAL RESULT - CLASS 12TH (Biology)")
        print("="*50)
        
        if physics > 50:
            print(f"Physics: {physics}% - Strong concepts. Keep practicing for better expression")
        elif physics >= 33:
            print(f"Physics: {physics}% - Understanding is good. Improve by practicing problems regularly")
        else:
            print(f"Physics: {physics}% - Focus on basic concepts. Practice more daily")
        
        if chemistry > 50:
            print(f"Chemistry: {chemistry}% - Strong concepts. Keep practicing for better expression")
        elif chemistry >= 33:
            print(f"Chemistry: {chemistry}% - Understanding is good. Improve by practicing regularly")
        else:
            print(f"Chemistry: {chemistry}% - Focus on basic concepts. Practice more daily")
        
        if biology > 50:
            print(f"Biology: {biology}% - Strong concepts. Keep practicing for better expression")
        elif biology >= 33:
            print(f"Biology: {biology}% - Understanding is good. Improve by practicing regularly")
        else:
            print(f"Biology: {biology}% - Focus on basic concepts. Practice more daily")
        
        if english > 50:
            print(f"English: {english}% - Strong language skills. Keep practicing for better expression")
        elif english >= 33:
            print(f"English: {english}% - Understanding is good. Improve by practicing writing and revisions")
        else:
            print(f"English: {english}% - Focus on grammar and writing skills. Practice daily")
        
        total = physics + chemistry + biology + english
        percentage = total / 4
        print("-"*50)
        print(f"Total: {total}/400")
        print(f"Average: {percentage:.2f}%")
        
        if percentage > 50:
            print("Overall: Strong performance. Keep practicing for better expression")
        elif percentage >= 33:
            print("Overall: Understanding is good. Improve by practicing regularly")
        else:
            print("Overall: Focus on basic concepts. Practice more daily")
        print("="*50 + "\n")
        
    elif stream == "Maths":
        print("Your subject are Physics , Chemistry , Maths , English ")
        physics = int(input("Enter your Physics marks here "))
        chemistry = int(input("Enter your Chemistry marks here "))
        maths = int(input("Enter your Maths marks "))
        english = int(input("Enter your English marks here "))
        
        print("\n" + "="*50)
        print("FINAL RESULT - CLASS 12TH (Maths)")
        print("="*50)
        
        if physics > 50:
            print(f"Physics: {physics}% - Strong concepts. Keep practicing for better expression")
        elif physics >= 33:
            print(f"Physics: {physics}% - Understanding is good. Improve by practicing regularly")
        else:
            print(f"Physics: {physics}% - Focus on basic concepts. Practice more daily")
        
        if chemistry > 50:
            print(f"Chemistry: {chemistry}% - Strong concepts. Keep practicing for better expression")
        elif chemistry >= 33:
            print(f"Chemistry: {chemistry}% - Understanding is good. Improve by practicing regularly")
        else:
            print(f"Chemistry: {chemistry}% - Focus on basic concepts. Practice more daily")
        
        if maths > 50:
            print(f"Maths: {maths}% - Strong concepts. Keep practicing for better expression")
        elif maths >= 33:
            print(f"Maths: {maths}% - Understanding is good. Improve by practicing regularly")
        else:
            print(f"Maths: {maths}% - Focus on basic concepts. Practice more daily")
        
        if english > 50:
            print(f"English: {english}% - Strong language skills. Keep practicing for better expression")
        elif english >= 33:
            print(f"English: {english}% - Understanding is good. Improve by practicing writing and revisions")
        else:
            print(f"English: {english}% - Focus on grammar and writing skills. Practice daily")
        
        total = physics + chemistry + maths + english
        percentage = total / 4
        print("-"*50)
        print(f"Total: {total}/400")
        print(f"Average: {percentage:.2f}%")
        
        if percentage > 50:
            print("Overall: Strong performance. Keep practicing for better expression")
        elif percentage >= 33:
            print("Overall: Understanding is good. Improve by practicing regularly")
        else:
            print("Overall: Focus on basic concepts. Practice more daily")
        print("="*50 + "\n")
        
    elif stream == "Both" or "both":
        print("Your Subjects are Physics , Chemistry , Biology , Maths , English ")
        physics = int(input("Enter your Physics marks "))
        chemistry = int(input("Enter your Chemistry marks "))
        biology = int(input("Enter your Biology marks "))
        maths = int(input("Enter your Maths marks "))
        english = int(input("Enter your English marks "))
        
        print("\n" + "="*50)
        print("FINAL RESULT - CLASS 12TH (Both)")
        print("="*50)
        
        if physics > 50:
            print(f"Physics: {physics}% - Strong concepts. Keep practicing for better expression")
        elif physics >= 33:
            print(f"Physics: {physics}% - Understanding is good. Improve by practicing regularly")
        else:
            print(f"Physics: {physics}% - Focus on basic concepts. Practice more daily")
        
        if chemistry > 50:
            print(f"Chemistry: {chemistry}% - Strong concepts. Keep practicing for better expression")
        elif chemistry >= 33:
            print(f"Chemistry: {chemistry}% - Understanding is good. Improve by practicing regularly")
        else:
            print(f"Chemistry: {chemistry}% - Focus on basic concepts. Practice more daily")
        
        if biology > 50:
            print(f"Biology: {biology}% - Strong concepts. Keep practicing for better expression")
        elif biology >= 33:
            print(f"Biology: {biology}% - Understanding is good. Improve by practicing regularly")
        else:
            print(f"Biology: {biology}% - Focus on basic concepts. Practice more daily")
        
        if maths > 50:
            print(f"Maths: {maths}% - Strong concepts. Keep practicing for better expression")
        elif maths >= 33:
            print(f"Maths: {maths}% - Understanding is good. Improve by practicing regularly")
        else:
            print(f"Maths: {maths}% - Focus on basic concepts. Practice more daily")
        
        if english > 50:
            print(f"English: {english}% - Strong language skills. Keep practicing for better expression")
        elif english >= 33:
            print(f"English: {english}% - Understanding is good. Improve by practicing writing and revisions")
        else:
            print(f"English: {english}% - Focus on grammar and writing skills. Practice daily")
        
        total = physics + chemistry + biology + maths + english
        percentage = total / 5
        print("-"*50)
        print(f"Total: {total}/500")
        print(f"Average: {percentage:.2f}%")
        
        if percentage > 50:
            print("Overall: Strong performance. Keep practicing for better expression")
        elif percentage >= 33:
            print("Overall: Understanding is good. Improve by practicing regularly")
        else:
            print("Overall: Focus on basic concepts. Practice more daily")
        print("="*50 + "\n")
