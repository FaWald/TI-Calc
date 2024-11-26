def extended_euclidean_algorithm(a, b):
    # Initialwerte für x und y setzen
    x0, y0 = 1, 0
    x1, y1 = 0, 1

    # Tabelle vorbereiten
    headers = ["a div b", "a, b", "x", "y"]
    table_data = []

    table_data.append(["-", (a, b), x0, y0])  # Initialzeile hinzufügen
    while b != 0:
        quotient = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - quotient * x1
        y0, y1 = y1, y0 - quotient * y1
        table_data.append([quotient, (a, b), x0, y0])

    # Tabelle drucken
    print("| {:^7} | {:^7} | {:^5} | {:^5} |".format(*headers))
    print("|" + "-" * 9 + "|" + "-" * 9 + "|" + "-" * 7 + "|" + "-" * 7 + "|")
    for row in table_data:
        print("| {:^7} | ({:^3},{:^3}) | {:^5} | {:^5} |".format(row[0], row[1][0], row[1][1], row[2], row[3]))
    return table_data


def starter_extended_euclidean_algorithm():
    # Beispielhafte Eingabe (kompatibel für den TI-Nspire CX-2 CAS)
    # Der Benutzer kann hier die Werte für a und b anpassen
    print("Enter the values for a and b:")
    a = int(input("a: "))
    b = int(input("b: "))
    return extended_euclidean_algorithm(a, b)

def starter():
    exit_value = True
    while exit_value:
        print("What program do u want?")
        print("0 = exit | 1 = extended euclidean algorithm")
        value = int(input(">"))
        if value == 1:
            starter_extended_euclidean_algorithm()
        elif value == 0:
            exit_value = False



# Starter-Funktion aufrufen
if __name__ == "__main__":
    starter()
    #extended_euclidean_algorithm(71, 15)
