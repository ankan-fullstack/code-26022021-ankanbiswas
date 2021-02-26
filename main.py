#Calculates BMI
def calculateBMI(height,weight):
  return round(weight/(height/100)**2,2)

#Test Cases
assert calculateBMI(175,75)==24.49
assert calculateBMI(161,57)==21.99

#Seperates BMI in Category
def categoryRisk(bmi):
  if bmi <= 18.4:
    return('Underweight','Malnutrition Risk')
  elif 18.5 <= bmi <= 24.9:
    return('Normal Weight','Low Risk')
  elif 25 <= bmi <= 29.9:
    return('Overweight','Enhanced Risk')
  elif 30 <= bmi <= 34.9:
    return('Moderately Obese','Medium Risk')
  elif 35 <= bmi <= 39.9:
    return('Severely Obese','High Risk')
  elif bmi >= 40:
    return('Very severely Obese','Very High Risk')
  
 #Test Cases
assert categoryRisk(17.55) == ('Underweight','Malnutrition Risk')
assert categoryRisk(21.66) == ('Normal Weight','Low Risk')
assert categoryRisk(26.5) == ('Overweight','Enhanced Risk')
assert categoryRisk(32.7) == ('Moderately Obese','Medium Risk')
assert categoryRisk(37.6) == ('Severely Obese','High Risk')
assert categoryRisk(47) == ('Very severely Obese','Very High Risk')

# Update existing objects
def updateObject(obj):  
 for n in obj:
   _bmi = calculateBMI(n['HeightCm'],n['WeightKg'])
   _temp = categoryRisk(_bmi)
   n.update({'BMI':_bmi})
   n.update({'BMI Category':_temp[0]})
   n.update({'Health Risk':_temp[1]})

    
#Processing the data
data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg":
85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166,
"WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female",
"HeightCm": 167, "WeightKg": 82}]
  
updateObject(data)
print(data)
