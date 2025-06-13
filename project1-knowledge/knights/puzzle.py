from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    # 如果A说的话(如果 A既是AKnight，也是AKnave)为真， 那么A是AKnight，反之依然
    Biconditional(And(AKnight, AKnave), AKnight),
    # 如果A说的话(如果 A既是AKnight，也是AKnave)为假， 那么A是AKnave，反之依然
    Biconditional(Not(And(AKnight, AKnave)), AKnave),

)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
aSay10 = Biconditional(AKnight, And(AKnave, BKnave))
aSay12 = Biconditional(AKnave, Not(And(AKnave, BKnave)))
knowledge1 = And(
Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
aSay10,
aSay12
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
aSay20= Biconditional(AKnight, And(AKnight, BKnight))
aSay21= Biconditional(AKnave, And(AKnave, BKnight))
bSay20=Biconditional(BKnight, And(AKnave, BKnight))
bSay21=Biconditional(BKnave, And(AKnave, BKnave))
knowledge2 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    aSay20,
    aSay21,
    bSay20,
    bSay21,
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Biconditional(Or(AKnight, AKnave), AKnight),
    Biconditional(Not(Or(AKnight, AKnave)), AKnave),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Biconditional(And(AKnave, CKnave), BKnight),
    Biconditional(Not(And(AKnave, CKnave)), BKnave),
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),
    Biconditional(AKnight,CKnight),
    Biconditional(Not(AKnight),CKnave)

)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
