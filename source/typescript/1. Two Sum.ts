function twoSum(nums: number[], target: number): number[] {
    const hashmap = new Map<number, number>();

    for (let i = 0; i < nums.length; i++) {
        if (hashmap.has(target - nums[i]))
            return [hashmap.get(target - nums[i])!, i];

        hashmap.set(nums[i], i);
    }

    return [];
};
