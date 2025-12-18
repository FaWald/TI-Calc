def read_int(prompt):
    while True:
        s = input(prompt).strip()
        try:
            return int(s)
        except:
            print("Bitte eine ganze Zahl eingeben.")

def divmod_calc(a, b):
    # gibt (q, r) zurück mit: a = q*b + r
    # und (üblich in Mathe) 0 <= r < |b|
    q = a // b
    r = a % b

    # Rest positiv machen (mathematische Standard-Variante)
    if r < 0:
        r += abs(b)
        q -= 1 if b > 0 else -1

    return q, r

if __name__ == "__main__":
    a = read_int("Gib a ein (die Zahl, die geteilt wird): ")
    b = read_int("Gib b ein (der Teiler, nicht 0): ")

    if b == 0:
        print("Fehler: Division durch 0 ist nicht erlaubt.")
    else:
        q, r = divmod_calc(a, b)

        print("\n--- Teilen mit Rest / Modulo ---")
        print("q = der Quotient (ganze Teile)   :", q)
        print("r = der Rest                     :", r)

        print("\nModulo:")
        print("a mod b = r  ->", str(a) + " mod " + str(b) + " = " + str(r))
