from logic import *

# ============================================================
# CHARACTERS
# ============================================================

# A can either be a Knight or a Knave
AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

# B can either be a Knight or a Knave
BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

# C can either be a Knight or a Knave
CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")


# ============================================================
# EXTRA SYMBOLS FOR PUZZLE 3
# ============================================================

# We do not know which sentence A actually said.
# So we create two symbols representing the possibilities.

ASaidKnight = Symbol("A said I am a Knight")
ASaidKnave = Symbol("A said I am a Knave")


# ============================================================
# GENERAL RULES
# ============================================================
#
# Every character:
#
# 1. Is either a Knight or a Knave.
# 2. Cannot be both.
#
# Instead of writing these rules repeatedly,
# we create reusable variables.
#

A_Rules = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave))
)

B_Rules = And(
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave))
)

C_Rules = And(
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave))
)


# ============================================================
# PUZZLE 0
# ============================================================
#
# A says:
#
# "I am both a knight and a knave."
#

AStatement0 = And(AKnight, AKnave)

knowledge0 = And(

    A_Rules,

    # If A is a Knight,
    # then the statement must be true.
    Implication(
        AKnight,
        AStatement0
    ),

    # If A is a Knave,
    # then the statement must be false.
    Implication(
        AKnave,
        Not(AStatement0)
    )
)


# ============================================================
# PUZZLE 1
# ============================================================
#
# A says:
#
# "We are both knaves."
#

AStatement1 = And(AKnave, BKnave)

knowledge1 = And(

    A_Rules,
    B_Rules,

    Implication(
        AKnight,
        AStatement1
    ),

    Implication(
        AKnave,
        Not(AStatement1)
    )
)


# ============================================================
# PUZZLE 2
# ============================================================
#
# A says:
#
# "We are the same kind."
#

AStatement2 = Or(

    And(AKnight, BKnight),

    And(AKnave, BKnave)

)

#
# B says:
#
# "We are different kinds."
#

BStatement2 = Or(

    And(AKnight, BKnave),

    And(AKnave, BKnight)

)

knowledge2 = And(

    A_Rules,
    B_Rules,

    # A speaks

    Implication(
        AKnight,
        AStatement2
    ),

    Implication(
        AKnave,
        Not(AStatement2)
    ),

    # B speaks

    Implication(
        BKnight,
        BStatement2
    ),

    Implication(
        BKnave,
        Not(BStatement2)
    )
)


# ============================================================
# PUZZLE 3
# ============================================================
#
# A says either:
#
# "I am a Knight."
#
# OR
#
# "I am a Knave."
#
# We don't know which.
#

knowledge3 = And(

    A_Rules,
    B_Rules,
    C_Rules,

    # A said exactly ONE sentence.

    Or(
        ASaidKnight,
        ASaidKnave
    ),

    Not(
        And(
            ASaidKnight,
            ASaidKnave
        )
    ),

    # ---------------------------------
    # If A said "I am a Knight"
    # ---------------------------------

    Implication(

        ASaidKnight,

        And(

            Implication(
                AKnight,
                AKnight
            ),

            Implication(
                AKnave,
                Not(AKnight)
            )

        )

    ),

    # ---------------------------------
    # If A said "I am a Knave"
    # ---------------------------------

    Implication(

        ASaidKnave,

        And(

            Implication(
                AKnight,
                AKnave
            ),

            Implication(
                AKnave,
                Not(AKnave)
            )

        )

    ),

    # ---------------------------------
    # B says:
    #
    # "A said I am a Knave."
    # ---------------------------------

    Implication(
        BKnight,
        ASaidKnave
    ),

    Implication(
        BKnave,
        Not(ASaidKnave)
    ),

    # ---------------------------------
    # B says:
    #
    # "C is a Knave."
    # ---------------------------------

    Implication(
        BKnight,
        CKnave
    ),

    Implication(
        BKnave,
        Not(CKnave)
    ),

    # ---------------------------------
    # C says:
    #
    # "A is a Knight."
    # ---------------------------------

    Implication(
        CKnight,
        AKnight
    ),

    Implication(
        CKnave,
        Not(AKnight)
    )
)


def main():

    symbols = [

        AKnight,
        AKnave,

        BKnight,
        BKnave,

        CKnight,
        CKnave

    ]

    puzzles = [

        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)

    ]

    for puzzle, knowledge in puzzles:

        print(puzzle)

        for symbol in symbols:

            if model_check(knowledge, symbol):

                print(f"    {symbol}")


if __name__ == "__main__":
    main()

