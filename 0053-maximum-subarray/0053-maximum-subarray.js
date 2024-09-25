/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let largestSum = 0, partialSum = 0;
    
    for (let num of nums){
        partialSum += num;
        if (partialSum < 0) partialSum = 0;
        else largestSum = Math.max(largestSum, partialSum);
    }
    
    let maxElement = nums.reduce((greater, num) => Math.max(greater, num), -Infinity);
    return (maxElement <= 0 ? maxElement : largestSum)
};