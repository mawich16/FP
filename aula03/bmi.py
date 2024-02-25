# coding: utf-8

# This function computes the body mass index (BMI),
# given the height (in meter) and weight (in kg) of a person.

def bodyMassIndex(height, weight):
	bmi = weight/(height**2)
	return bmi

# This function returns the BMI category acording to this table:
# BMI:        <18.5         [18.5, 25[      [25, 30[      30 or greater 
# Category:   Underweight   Normal weight   Overweight    Obesity 
def bmiCategory(imc):
	assert imc>0
	if imc<18.5:
		bmicategory="underweight"
	elif 18.5<=imc<25:
		bmicategory="normal weight"
	elif 25<=imc<30:
		bmicategory="overweight"
	else:
		bmicategory="obesity"
	return bmicategory



# This is the main function
def main():
    print("Índice de Massa Corporal")
    
    height = float(input("Altura (m)? "))
    if height < 0:
        print("ERRO: altura inválida!")
        exit(1)

    weight = float(input("Peso (kg)? "))
    if weight < 0:
        print("ERRO: peso inválido!")
        exit(1)

    imc = bodyMassIndex(height,weight)
    cat = bmiCategory(imc)

    print("BMI:", imc, "kg/m2")
    print("BMI category:", cat)
    return None

# Program starts executing here
main()

