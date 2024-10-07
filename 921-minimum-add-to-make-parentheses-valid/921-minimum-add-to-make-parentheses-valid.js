/**
 * @param {string} s
 * @return {number}
 */
var minAddToMakeValid = function(s) {
    let stack = [], moves = 0;
    
    for (let char of s) {
        if (char == '(')
            stack.push(char);
        if (stack.length == 0 && char === ')') 
            moves += 1;
        
        if (stack.length > 0 && char === ')') 
            stack.pop();
    }
    
    return stack.length + moves
};