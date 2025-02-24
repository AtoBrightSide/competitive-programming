var TimeLimitedCache = function () {
    this.pairs = new Map();
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function (key, value, duration) {
    const keyPresent = this.pairs.has(key);
    const timerId = setTimeout(() => this.pairs.delete(key), duration);

    if (keyPresent) {
        const prevTimerId = this.pairs.get(key)[1];
        clearTimeout(prevTimerId);
    }
    this.pairs.set(key, [value, timerId]);
    return keyPresent;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function (key) {
    return (this.pairs.has(key)) ? this.pairs.get(key)[0] : -1;
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function () {
    return this.pairs.size;
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */