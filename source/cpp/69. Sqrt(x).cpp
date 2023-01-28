class Solution {
public:
    int mySqrt(int x) {
        if (x == 0) return 0;
        if (x == 1) return 1;

        auto left = 1ULL;                           // 1UUL is used to avoid overflow
        auto right = x;
        while (left <= right) {
            auto mid = (left + right) / 2UL;
            auto square = (long long)mid * mid;
            if (square == x) return mid;
            if (square < x)
                left = mid + 1;
            else
                right = mid - 1;
        }

        return right;
    }
};