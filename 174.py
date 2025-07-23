marks = int(input("Enter your marks: "))

if marks >= 50:
    if marks >= 80:
        print("Passed with scholarship")
    else:
        print("Passed without scholarship")
else:
    print("Failed")