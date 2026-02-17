function containsDuplicate(nums: number[]): boolean {
  // use a set
  // iterate through the set of number adding them to the set at each step
  // check if the element that we are at is already in the set then return true
  // outside of the look return false

  const seen = new Set<number>();

  for (const num of nums) {
    if (seen.has(num)) return true;
    seen.add(num);
  }

  return false;
}
