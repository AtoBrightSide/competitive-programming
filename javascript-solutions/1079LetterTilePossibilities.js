/**
 * @param {string} tiles
 * @return {number}
 */
var numTilePossibilities = function (tiles) {
    let seen = new Set();
    let N = tiles.length;

    const countSequences = (currTiles, indexSet) => {
        if (seen.has(currTiles)) return

        if (currTiles.trim() !== '') seen.add(currTiles);
        for (let i = 0; i < N; i++) {
            currTiles += tiles[i];
            if (!seen.has(currTiles) && !indexSet.has(i)) {
                indexSet.add(i);
                countSequences(currTiles, indexSet);
                indexSet.delete(i);
            }
            currTiles = currTiles.slice(0, -1);
        }
    };
    countSequences('', new Set());
    return seen.size;
};