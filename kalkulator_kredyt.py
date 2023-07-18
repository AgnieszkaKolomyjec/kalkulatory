# funkcja obliczająca wartość raty równej
def calculate_value_equal_installment(initial_value, percentage, years, numer_of_installments):
    result = (amount*(percentage/number_of_installments)*((1+(percentage/number_of_installments))**loan_period))/(((1+(percentage/number_of_installments))**loan_period)-1)
    return result

#funkcja oblczająca całkowitą wysokość zapłaconych odsetek
def calculate_interest_rate_equal_installment(final_value,loan_period, amount, number_of_installments):
    cko = (final_value * loan_period) - amount
    return cko

# amount to kwota udzielonego kredytu,
# percentage to oprocentowanie kredytu w skali roku,
# loan_period to okres kredytowania
# number_of_installments to liczba rat w ciągu roku

#funkcja,pytająca użytkownika o dane potrzebne do obliczeń
def question_to_user(message):
    input_value = input(message)
    return float(input_value)

print("Kalkulator wysokości raty równej oraz wysokości odsetek od kredytu ")

amount = question_to_user("Jaka kwota kredytu Cię interesuje? ")
percentage = float(question_to_user("Jakie jest oprocentowanie kredytu ")/100)
loan_period = question_to_user("Na jaki okres chciałabyś/chciałbyś zaciągnąć kredyt. Informację podaj w miesiącach.")
number_of_installments = question_to_user("Ilość rat płatnych w ciągu roku. ")

final_value = calculate_value_equal_installment(amount,percentage,loan_period, number_of_installments)
print(f"Wartość raty kredytu wynosi {final_value:.2f}")

final_value_interest =calculate_interest_rate_equal_installment(final_value,loan_period, amount, number_of_installments)
print(f"Całkowita wartość odsetek wynosi:{final_value_interest:.2f} ")

