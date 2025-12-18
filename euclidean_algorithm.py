def read_int(prompt):
    while True:
        s = input(prompt).strip()
        try:
            return int(s)
        except:
            print("Bitte eine ganze Zahl eingeben.")

def euclid_table(a, b):
    # ggT ist immer positiv gemeint
    a = abs(a)
    b = abs(b)

    # Für die Tabelle meistens schöner: a >= b
    if a < b:
        a, b = b, a

    steps = []
    while b != 0:
        r = a % b
        steps.append((a, b, r))
        a, b = b, r

    # Letzte Zeile wie auf der Folie: (ggT, 0, leer)
    steps.append((a, 0, None))
    return a, steps

def print_table(steps):
    h1, h2, h3 = "a", "b", "a mod b"

    w1 = max(len(h1), max(len(str(row[0])) for row in steps))
    w2 = max(len(h2), max(len(str(row[1])) for row in steps))
    w3 = max(len(h3), max(len(str(row[2])) for row in steps if row[2] is not None) if steps else 0)

    # Kopf
    print(h1.rjust(w1), h2.rjust(w2), h3.rjust(w3))
    print("-" * w1, "-" * w2, "-" * w3)

    # Zeilen
    for a, b, r in steps:
        r_str = "" if r is None else str(r)
        print(str(a).rjust(w1), str(b).rjust(w2), r_str.rjust(w3))

if __name__ == "__main__":
    a = read_int("a eingeben: ")
    b = read_int("b eingeben: ")

    g, steps = euclid_table(a, b)
    print_table(steps)
    print("\nDer ggT von", a, "und", b, "ist also", g, ".")
