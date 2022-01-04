"""Time to learn recursion!!!"""
import random

recursion_understood = False


def understand_recursion(attempts=0) -> None:
    """May help you understand recursion"""
    # user may forget what recursion is after running this script
    # NOTE: this is not a bug, it's a feature!

    # randomly decide whether recursion is understood
    global recursion_understood
    recursion_understood = bool(random.getrandbits(1))
    print(f"{recursion_understood=}")

    # use human psychology (cramming) to understand recursion if it is not understood yet
    if recursion_understood:
        print(f"Recursion understood after {attempts} attempts. Ez!! 🎉🎉")
    else:
        understand_recursion(attempts + 1)


if __name__ == "__main__":
    understand_recursion()
