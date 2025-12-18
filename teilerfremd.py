# MicroPython: a-Finder (nur m eingeben, ohne Libraries)

def gcd(a, b):
    a = abs(a)
    b = abs(b)
    while b != 0:
        a, b = b, a % b
    return a

def find_a_candidates(m, count):
    res = []
    a = 2
    while a < m and len(res) < count:
        if gcd(a, m) == 1:
            res.append(a)
        a += 1
    return res

def main():
    print("=== a suchen (teilerfremd zu m) ===")
    m = int(input("m eingeben: "))

    candidates = find_a_candidates(m, 3)

    if len(candidates) == 0:
        print("Kein a gefunden.")
        return

    print("\nErste", len(candidates), "gültige a (ggT(a,m)=1):")
    print(candidates)
    print("Kleinster gültiger a =", candidates[0])

if __name__ == "__main__":
    main()
