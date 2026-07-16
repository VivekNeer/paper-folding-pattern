# Paper Folding Pattern

Returns "Valley" or "Mountain" for the x-th crease after n folds.

## Observation

By observation of the physical paper folding we get to know that:

- the midpoint being = `2^(n-1)` is the brand new crease made by the last fold will always be a Valley
- all values left of midpoint retain their values which was held previously as such we can recurse with `n-1` and `x`
- positions right of the midpoint are mirrored and inverted of the left half

So u could say the general formula is:

`seq(n) = seq(n-1) + "Valley" + flip(reverse(seq(n-1)))`

## Example

So for example if we had to take `n=3`

1. `n=1 : V`
   First point always Valley
2. `n=2 : VVM`
   1. Since `n=2`, total no of creases = `2**n-1` >> so `4-1` >> `3`
   2. we also know midpoint(being `2`) is always Valley and left side of midpoint is preserved >> `VV`
   3. We also know that right side of midpoint is mirrored and inverted of left side >> we know `V` is left side >> mirroring it results in `V` >> inverting it results in `M`
   4. In Total we get `VVM`

3. `n=3 : VVMVVMM`
   1. Total No of Creases : `2**n-1` >> `8-1` >> `7 creases`
   2. Midpoint (being `4`) is `V` and all values to the left side is preserved >> `VVM V`
   3. Right side of midpoint is the mirrored and inverted half of left side >> left side half = `VVM` >> mirrored = `MVV` >> inverted & mirrored = `VMM`
   4. Joining `2&3` we get `VVMVVMM`
