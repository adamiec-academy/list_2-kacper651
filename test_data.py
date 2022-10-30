REMOVE_PARENTHESES_DATA = [
    ("To jest (słoneczny) dzień", "To jest dzień"),
    ("(Trochę) fajne, a (trochę) niefajne", "fajne, a niefajne"),
    ("Ostatni (żywy) władca wiatru!", "Ostatni władca wiatru!"),
]


IS_PRIME_DATA = [
    (0, False),
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (11, True),
    (19, True),
    (53, True),
    (71, True),
    (89, True),
    (97, True),
    (98, False),
    (99, False),
    (100, False),
    (2137, True),
]


IS_DIABOLIC_DATA = [
    (0, False),
    (6, False),
    (2137, False),
    (666, True),
    (6666, True),
    (66566, False),
    (663466623, True),
]


MULTIPLICATION_TABLE_DATA = [
    (3, 9, 2, 12,
"""\
    |   3   4   5   6   7   8   9
---------------------------------
  2 |   6   8  10  12  14  16  18
  3 |   9  12  15  18  21  24  27
  4 |  12  16  20  24  28  32  36
  5 |  15  20  25  30  35  40  45
  6 |  18  24  30  36  42  48  54
  7 |  21  28  35  42  49  56  63
  8 |  24  32  40  48  56  64  72
  9 |  27  36  45  54  63  72  81
 10 |  30  40  50  60  70  80  90
 11 |  33  44  55  66  77  88  99
 12 |  36  48  60  72  84  96 108
""")
]


CIPHER_DATA = [
    ("Alfa i Omega", 13, "Nysn v Bzrtn"),
    ("Nysn v Bzrtn", 13, "Alfa i Omega"),
    ("imperator", 3, "lpshudwru"),
    ("Imperator", 3, "Lpshudwru"),
]


DECIPHER_DATA = [
    ("Alfa i Omega", 13, "Nysn v Bzrtn"),
    ("Nysn v Bzrtn", 13, "Alfa i Omega"),
    ("lpshudwru", 3, "imperator"),
    ("Lpshudwru", 3, "Imperator"),
]
