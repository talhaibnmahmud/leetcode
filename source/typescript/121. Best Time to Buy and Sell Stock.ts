function maxProfit(prices: number[]): number {
    let maxProfit = 0;
    let minPrice = Number.MAX_SAFE_INTEGER;

    prices.forEach((price) => {
        minPrice = Math.min(minPrice, price);
        maxProfit = Math.max(maxProfit, price - minPrice);
    });

    return maxProfit;
};
