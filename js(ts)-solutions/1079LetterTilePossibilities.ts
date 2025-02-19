function numTilePossibilities(tiles: string): number {
    let seen: Set<string> = new Set<string>();
    let N: number = tiles.length;

    const countSequences = (currTiles: string, indexSet: Set<number>) => {
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
    countSequences('', new Set<number>());
    return seen.size;
};