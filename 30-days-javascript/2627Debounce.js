/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function (fn, t) {
    const timers = [];
    return function (...args) {
        if (timers.length > 0) {
            const cancelledId = timers.pop();
            clearTimeout(cancelledId);
        }
        const timerId = setTimeout(() => {
            fn(...args);
            timers.pop();
        }, t);
        timers.push(timerId)
    }
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */