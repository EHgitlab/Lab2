wt = int(input("Enter your weight \n"))
ht = float(input("Enter your height \n"))
def calculate_bmi(height, weight):
    Height = "Height = " + str(height)
    Weight = "Weight = " + str(weight)
    Bmi = weight / (height*height)
    print(Weight)
    print(Height)
    Bmi = weight / (height*height)
    print("BMI = " + str(Bmi))
    return Bmi

def conditional_queue(Bmi):
    if Bmi < 18.5:
        return "Under Weight"
    elif Bmi >= 18.5 and Bmi <= 25:
        return "Normal Weight"
    elif Bmi > 25.0:
        return "Over Weight"


Bmi = calculate_bmi(weight = wt, height = ht)
conditional_queue(Bmi)

ans = conditional_queue(Bmi)
print(ans)