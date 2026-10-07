# bmi = weight in kg / (height in meter * height in meter)
def calculateBMI(height, weight):
    heightInMeter = height * 0.4536

    bmi = weight/(heightInMeter * heightInMeter)
    return bmi

print(calculateBMI(5.8, 70))