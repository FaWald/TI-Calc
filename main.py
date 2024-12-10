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
    return table_data[-1][3]

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_teilfremd(m):
    a = 2  # Starte mit 1, weil jede Zahl teilerfremd zu 1 ist
    while gcd(a, m) != 1:
        a += 1  # Erhöhe a, bis es teilerfremd zu m ist
    return a

def starter_extended_euclidean_algorithm():
    # Beispielhafte Eingabe (kompatibel für den TI-Nspire CX-2 CAS)
    # Der Benutzer kann hier die Werte für a und b anpassen
    print("Enter the values for a and b:")
    a = int(input("a: "))
    b = int(input("b: "))
    return extended_euclidean_algorithm(a, b)

def public_key(p, q):
    n = p * q
    print("n: ", n)
    m = (p - 1) * (q - 1)
    print("m: ", m)
    custom_a = input("custom a? [y/n]: ")
    if custom_a == "y":
        a = int(input("a: "))
    else:
        a = find_teilfremd(m)
    print("a: ", a)
    return n,a,m

def private_key(x, public_k):
    a = public_k[1]
    n = public_k[0]
    y = pow(x, a, n)
    return y


def rsa():
    p = int(input("p: "))
    q = int(input("q: "))
    public_k = public_key(p, q)
    encrypted_number = int(input("x: "))
    y = private_key(encrypted_number, public_k)
    print("y: ", y)
    b = extended_euclidean_algorithm(public_k[2], public_k[1])
    print("b: ", b)
    x = pow(y, b, public_k[0])
    print("x: ", x)
    pass

def mod_inverse(e, phi):
    """Berechnet das modulare Inverse von e modulo phi"""
    # Erweiterten Euklidischen Algorithmus anwenden
    t, new_t = 0, 1
    r, new_r = phi, e

    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r

    if r > 1:
        return None  # Kein inverses Element
    if t < 0:
        t += phi
    return t


def check_rsa_keys(n, e, d):
    """Überprüft die RSA-Schlüssel."""
    # Faktorisierung von n (nur für kleine Zahlen wie hier machbar)
    p, q = None, None
    for i in range(2, n):
        if n % i == 0:
            p = i
            q = n // i
            break

    if p is None or q is None:
        return "n konnte nicht faktorisiert werden."

    # Berechnung von phi(n)
    phi = (p - 1) * (q - 1)

    # Prüfen, ob e und phi teilerfremd sind
    if gcd(e, phi) != 1:
        return "e = "+ str(e) +" ist nicht teilerfremd zu PHI(n) = "+ str(phi)

    # Berechnen, ob d das modulare Inverse von e modulo phi ist
    d_computed = mod_inverse(e, phi)
    if d_computed != d:
        return "d = "+str(d)+" ist nicht das modulare Inverse von e = "+str(e)+" modulo PHI(n) = "+str(phi)

    return "Die Schlüssel sind korrekt: (n = "+str(n)+", e = "+str(e)+", d = "+str(d)+")."



def starter_rsa():
    exit_value = True
    while exit_value:
        print("What subprogram do u want?")
        print("0 = exit | 1 = Full RSA | 2 = extended euclidean algorithm | 3 = Teilerfremd | 4 = ggT | 5 = Public | 6 = Private | 7 = check rsa keys")
        value = int(input(">"))
        if value == 1:
            rsa()
        elif value == 2:
            starter_extended_euclidean_algorithm()
        elif value == 3:
            m = int(input("m: "))
            print(find_teilfremd(m))
        elif value == 4:
            a = int(input("a: "))
            b = int(input("b: "))
            print(gcd(a,b))
        elif value == 5:
            p = int(input("p: "))
            q = int(input("q: "))
            print(public_key(p, q))
        elif value == 6:
            key = []
            key[0] = int(input("n: "))
            key[1] = int(input("a: "))
            x = int(input("x: "))

            print(private_key(x, key))
        elif value == 7:
            n = int(input("n: "))
            e = int(input("e: "))
            d = int(input("d: "))
            print(check_rsa_keys(n, e, d))
        elif value == 0:
            exit_value = False

    pass

def binary_addition_steps(bin1, bin2):
    max_length = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(max_length)  # Füllt mit Nullen auf, um gleiche Länge zu erreichen
    bin2 = bin2.zfill(max_length)

    result = []
    carry = 0
    steps = []

    for i in range(max_length - 1, -1, -1):
        b1 = int(bin1[i])
        b2 = int(bin2[i])
        total = b1 + b2 + carry

        result_bit = total % 2
        carry = total // 2

        result.insert(0, str(result_bit))
        steps.append({
            "Position": max_length - i,
            "Bit1": b1,
            "Bit2": b2,
            "Übertrag": carry,
            "Summe": total,
            "Ergebnis-Bit": result_bit
        })

    if carry:
        result.insert(0, '1')
        steps.append({
            "Position": "Carry-Out",
            "Bit1": 0,
            "Bit2": 0,
            "Übertrag": carry,
            "Summe": carry,
            "Ergebnis-Bit": 1
        })

    print("Zwischenschritte:")
    for step in reversed(steps):
        print(step)

    print("\nEndergebnis:", "".join(result))
    return "".join(result)


def binary_subtraction_steps(bin1, bin2):
    # Beide Zahlen gleich lang machen
    max_length = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(max_length)
    bin2 = bin2.zfill(max_length)

    # Zweierkomplement von bin2 berechnen
    def twos_complement(binary):
        # Invertieren
        inverted = ''.join('1' if b == '0' else '0' for b in binary)
        # Eins addieren
        result = binary_addition_steps(inverted, '1')
        return result.zfill(max_length)

    print(f"Binärzahl 1: {bin1}")
    print(f"Binärzahl 2: {bin2}")
    print("Berechnung des Zweierkomplements von Binärzahl 2...")

    # Zweierkomplement von bin2 berechnen
    complement = twos_complement(bin2)
    print(f"Zweierkomplement von Binärzahl 2: {complement}")

    # Addition von bin1 mit dem Zweierkomplement von bin2
    print("Addition der Binärzahl 1 mit dem Zweierkomplement von Binärzahl 2...")
    result = binary_addition_steps(bin1, complement)

    # Prüfen, ob ein Übertrag (Carry-Out) vorhanden ist
    if len(result) > max_length:
        result = result[1:]  # Entfernt den Übertrag
        print("Übertrag entfernt (Carry-Out), Ergebnis ist positiv.")
    else:
        print("Kein Übertrag, Ergebnis ist negativ (Zweierkomplement).")
        result = "-" + twos_complement(result)

    print(f"Endergebnis: {result}")
    return result

def binary_multiplication_steps(bin1, bin2):
    # Um die Zwischenschritte richtig zu berechnen, arbeiten wir von rechts nach links
    bin1 = bin1[::-1]
    bin2 = bin2[::-1]
    partial_results = []

    # Für jedes Bit in der zweiten Zahl
    for i, bit in enumerate(bin2):
        if bit == '1':  # Wenn das aktuelle Bit 1 ist
            partial_result = bin1[::-1] + '0' * i  # Verschieben um i Positionen nach links
        else:
            partial_result = '0' * (len(bin1) + i)  # Alles 0 für das Zwischenergebnis

        partial_results.append(partial_result.zfill(len(bin1) + len(bin2)))

    # Zwischenschritte anzeigen
    print("Zwischenschritte der Multiplikation:")
    for idx, step in enumerate(partial_results):
        print(f"Schritt {idx + 1}: {step}")

    # Endergebnis berechnen, indem die Zwischenschritte im Dezimalformat summiert werden
    result_decimal = sum(int(step, 2) for step in partial_results)
    result = bin(result_decimal)[2:]  # Zurück in Binär konvertieren

    print("\nEndergebnis:", result)
    return result


def convert_number(number, convert):
    result = 0
    length = len(number)
    for digit in str(number):
        length -= 1
        result += int(digit) * int(convert)**int(length)


    return result


def starter_counting_system():
    exit_value = True
    while exit_value:
        print("What subprogram do u want?")
        print("0 = exit | 1 = + | 2 = - | 3 = * | 4 = convert")
        value = int(input(">"))
        if value == 1:
            bit1 = input("bit1: ")
            bit2 = input("bit2: ")
            binary_addition_steps(bit1, bit2)
        elif value == 2:
            bit1 = input("bit1: ")
            bit2 = input("bit2: ")
            binary_subtraction_steps(bit1, bit2)
        elif value == 3:
            bit1 = input("bit1: ")
            bit2 = input("bit2: ")
            binary_multiplication_steps(bit1, bit2)
        elif value == 4:
            number = input("number: ")
            convert = input("convert: ")
            print(convert_number(number, convert))
        elif value == 0:
            exit_value = False


def starter():
    exit_value = True
    while exit_value:
        print("What program do u want?")
        print("0 = exit | 1 = RSA | 2 = Zahlensysteme ")
        value = int(input(">"))
        if value == 1:
            starter_rsa()
        elif value == 2:
            starter_counting_system()
        elif value == 0:
            exit_value = False



# Starter-Funktion aufrufen
if __name__ == "__main__":
    starter()

