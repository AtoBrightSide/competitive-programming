/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    let memo = new Map();
    return function (...args) {
        const params = JSON.stringify(args);
        if (!memo.has(params)) {
            const result = fn(...args);
            memo.set(params, result);
            return result;
        }
        return memo.get(params);
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */