/**
 * @param {string} s1
 * @param {string} s2
 * @return {string[]}
 */
const helper = (counter1, counter2) => {
    let uncommon_words = [];
    for (const [word, freq] of counter1.entries()) {
        if (freq === 1 && !counter2.get(word)) {
            uncommon_words.push(word)
        }
    }
    
    return uncommon_words;
}
var uncommonFromSentences = function(s1, s2) {
    let counter1 = new Map();
    let counter2 = new Map();
    
    s1.split(" ").map(word => {
        let count = counter1.get(word);
        if (count >= 1) {
            counter1.set(word, count + 1)
        } else {
            counter1.set(word, 1)
        }
    })
    
    s2.split(" ").map(word => {
        let count = counter2.get(word);
        if (count >= 1) {
            counter2.set(word, count + 1)
        } else {
            counter2.set(word, 1)
        }
    })
    
    return [...helper(counter1, counter2), ...helper(counter2, counter1)]
};