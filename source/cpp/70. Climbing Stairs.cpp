class Solution {
public:
    int climbStairs(int n) {
        if (n == 1) return 1;
        if (n == 2) return 2;

        auto prevStep = 2;
        auto beforePrevStep = 1;
        auto current = 0;

        for (auto i = 2; i <= n; i++) {
            current = prevStep + beforePrevStep;
            beforePrevStep = prevStep;
            prevStep = current;
        }

        return current;
    }
};
