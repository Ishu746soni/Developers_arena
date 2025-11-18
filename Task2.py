while True:
    marks=input("Enter marks(Type 'end' to stop the program):")

    if marks.lower() == "end":
        print("Program Stopped...")
        break

    marks=int(marks)

    if(marks > 90):
        print("Grade: A")
        print("Congratulations!! U have done a great job...")
    elif(marks > 80 and marks <90):
        print("Grade: B")
        print("Excellent!! Keep it up...")
    elif(marks >70 and marks < 80):
        print("Grade: C")
        print("Good!! Well done....")
    elif(marks > 60 and marks < 70):
        print("Grade: D")
        print("Needs Improvement...")
    else:
        print("Fail :) .....")