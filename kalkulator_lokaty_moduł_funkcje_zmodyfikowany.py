#funkcja obliczająca wartość inwestycji z lokaty
def calculate_investment_value(initial_value, percentage, years):
    result=initial_value*(1+percentage/100)**years
    return result

#pytania do użytkownika w celu uzyskania danych potzrebnych do obliczeń
def question_to_user(message):
    input_value = input(message)
    return float(input_value)

print("Kalkulator wartości lokaty z roczną kapitalizacją")

initial_value=question_to_user("Jaką kwotę wpłaciłaś/łeś na lokatę? ")
percentage=question_to_user("Jakie jest oprocentowanie (%) ")
years=question_to_user("Ile lat trwa lokata?")

final_value=calculate_investment_value(initial_value,percentage,years)
print(f"Po {years} latach Twoja lokata będzie warta {final_value:.2f}")

longer_term = years*2
alternative_value = calculate_investment_value(initial_value, percentage, longer_term)
print(f"Rozważ zostawienie lokaty na {longer_term} lat - będzie wtedy warta {alternative_value:.2f}")