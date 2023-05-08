#Temp_Converter_Fahrenheit.py - Converting temperature from celsius to fahrenheit
#Mason Smythe
#09/05/2023


def to_f(from_c):
    fahrenheit = (from_c * 9/5) + 32
    return fahrenheit

#Main Routine
temperatures = [0, 40, 100]
converted = []

for item in temperatures:
    answer = to_f(item)
    ans_statement = "{} degrees C is {} degrees F".format(item, answer)
    converted.append(ans_statement)

print(converted)


