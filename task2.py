def get_crease(n: int, x: int) -> str:
    """
    Returns "Valley" or "Mountain" for the x-th crease after n folds.

    By observation of the physical paper folding we get to know that:
      -the midpoint being = 2^(n-1) is the brand new crease made by the last fold will always be a Valley
      - all values left of midpoint retain their values which was held previously as such we can recurse with n-1 and x
      - positions right of the midpoint are mirrored and inverted of the left half
    
    So u could say the general formula is:
    seq(n) = seq(n-1) + "Valley" + flip(reverse(seq(n-1)))
    """
    total_creases = 2 ** n - 1
    if not (1 <= x <= total_creases):
        raise ValueError(f"x must be between 1 and {total_creases} for n={n}")

    return _get_crease_helper(n, x)


def _get_crease_helper(n: int, x: int) -> str:
    mid = 1 << (n - 1)  # the crease made by the most recent fold

    if x == mid:
        return "Valley"  # newest crease - always a Valley
    elif x < mid:
        return _get_crease_helper(n - 1, x)  # left side hasn't changed, so just go back a fold
    else:
        mirrored_x = (1 << n) - x  # find where this would sit on the left side instead
        inner = _get_crease_helper(n - 1, mirrored_x)
        return "Mountain" if inner == "Valley" else "Valley"  # right side is flipped


if __name__ == "__main__":
    print(get_crease(1, 1))    # Valley
    print(get_crease(2, 3))    # Mountain
    print(get_crease(3, 6))    # Mountain
    print(get_crease(4, 11))   # Mountain
    print(get_crease(5, 16))   # Valley
    print(get_crease(8, 255))  # Mountain