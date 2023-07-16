# funkcja obliczająca wartość inwestycji z lokaty
def calculate_investment_value(initial_value, percentage, years):
    result = (amount*(percentage/number_of_installments)*((1+(percentage/number_of_installments))**loan_period))/(((1+(percentage/number_of_installments))**loan_period)-1)
    return result

#installment=amount*(1+(percentage/months)**number_of_installments)*(1+(percentage/months)-1)/[(1+(percentage/months)**number_of_installments)-1],
# result = to wysokość raty równej,
# amount to kwota udzielonego kredytu,
# percentage to oprocentowanie kredytu w skali roku,
# loan_period to okres kredytowania
# number_of_installments to liczba rat w ciągu roku

#pytania do użytkownika w celu uzyskania danych potzrebnych do obliczeń
def question_to_user(message):
    input_value = input(message)
    return float(input_value)

print("Kalkulator wysokości raty równej kredytu")

amount=question_to_user("Jaka kwota kredytu Cię interesuje? ")
percentage=float(question_to_user("Jakie jest oprocentowanie kredytu ")/100)
loan_period=question_to_user("Na jaki okres chciałabyś/chciałbyś zaciągnąć kredyt. Informację podaj w miesiącach.")
number_of_installments =question_to_user("Ilość rat płatnych w ciągu roku. ")

final_value=calculate_investment_value(amount,percentage,loan_period)
print(f"Wartość raty kredytu wynosi {final_value:.2f}")

