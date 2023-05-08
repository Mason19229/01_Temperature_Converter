#Temp_Converter_Celsius.py - Converting temperature from fahrenheit to celsius
#Mason Smythe
#09/05/2023

def to_c(from_f):
    celsius = (from_f - 32) * 5/9
    return celsius

#Main Rountine
temperatures = [0, 32, 100]
converted = []

for item in temperatures:
    answer = to_c(item)
    ans_statement = "{} degrees F is {} degrees C".format(item, answer)
    converted.append(ans_statement)

print(converted)