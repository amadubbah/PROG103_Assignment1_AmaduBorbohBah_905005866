try:
    # Variable declaration
    score1 = float(input("Enter first test score: "))
    score2 = float(input("Enter second test score: "))
    score3 = float(input("Enter third test score: "))

    # Operation: calculate average
    average = (score1 + score2 + score3) / 3

    # Display results
    print("Scores entered:", score1, score2, score3)
    print("Average score:", round(average, 2))

except ValueError:
    print("Invalid input! Please enter numeric values only.")