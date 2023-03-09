"""Typy zmiennych"""
some_text = "Typ tekstowy"  # Tekst
print(type(some_text), some_text)

some_integer = 12  # Wartość liczbowa całkowita
print(type(some_integer), some_integer)

some_float = 12.23  # Wartość liczbowa zmiennoprzecinkowa
print(type(some_float), some_float)

some_bool = True  # Wartosc logiczna prawda (False dla nieprawda)
print(type(some_bool), some_bool)

print("*" * 50)

"""Dodatkowe cechy wartości"""
# Podstawowe wyświetlanie tekstu
other_text = "Jestem jakims tekstem"
value_one = 1
print("TEKST" + str(value_one) + ": " + other_text)  # Dodawanie zmiennych tekstowych
print(f"TEKST{str(value_one)}: {other_text}")  # f-string!!!! (WAŻNE)
print("TEKST{value1}: {text}".format(value1=value_one, text=other_text))  # Formatowanie tekstu (lepiej używać f-string)

print("*" * 50)

"""Operacje matematyczne"""
# Operacje na int/float
print(f"Dodawanie: {12 + 13}")
print(f"Odejmowanie: {12 - 13}")
print(f"Mnożenie: {12 * 13}")
print(f"Dzielenie: {12 / 13}")
print(f"Modulo (reszta z dzielenia) 5 i 2: {5 % 2}")
print(f"Modulo (reszta z dzielenia) 8 i 3: {8 % 3}")
print(f"Potęgowanie: {2 ** 3}")

print("*" * 50)

# Operacje na str
print(f"Dodawanie: {'Jakis ' + 'tekst'}")
print(f"Mnozenie przez liczbę: {'*' * 50}")

print("*" * 50)

"""Rzutowanie zmiennych"""
# Zamiana z tekstu na liczbę całkowitą
integer_as_text = "12"
integer_value = int(integer_as_text)
print(type(integer_as_text), integer_as_text)
print(type(integer_value), integer_value)
print(integer_value + 3)

print("*" * 50)

# Zamiana z integera na float
some_other_integer = 12
print(type(some_other_integer), some_other_integer)
float_from_integer = float(some_other_integer)
print(type(float_from_integer), float_from_integer)

print("*" * 50)

# Zamiana z liczby na tekst
integer_value = 12
print(type(integer_value), integer_value)
string_from_integer = str(integer_value)
print(type(string_from_integer), string_from_integer)

print("*" * 50)

# Rzutowanie float na int
float_value = 123.3333
int_from_float = int(float_value)  # Float na int zawsze da int (utnie część po przecinku)
print(float_value, int_from_float)

# Rzutowanie bool na tekst
some_bool = True
text_from_bool = str(some_bool)
print(type(some_bool), some_bool)
print(type(text_from_bool), text_from_bool)

print("*" * 50)

# Rzutowanie tekstu na bool
some_bool_as_text = "True"
bool_from_text = bool(some_bool_as_text)
print(type(some_bool_as_text), some_bool_as_text)
print(type(bool_from_text), bool_from_text)

print("*" * 50)

"""Ciekawe przypadki"""
print(f"Dzielenie takich samych liczb {12 / 12}")  # Dzielenie zawsze daje typ float
# print(f"Dzielenie przez 0 {12 / 0}")  # Dzielenie przez zero wywala błąd - nie robimy tak!
print(f"Suma int i float: {12 + 13.0}")  # Dodawanie int i float zawsze da float
print(f"Iloczyn int i float: {12 * 13.0}")
bool_value_as_integer = 1  # Odpowiada wartości True jako bool
print(type(bool_value_as_integer), bool_value_as_integer)
print("*" * 50)
