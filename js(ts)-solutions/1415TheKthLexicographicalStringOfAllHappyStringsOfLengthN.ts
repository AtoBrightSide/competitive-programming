function getHappyString(n: number, k: number): string {
    let happyStrings: string[] = [];
    const dfs = (stack: string[]) => {
        if (stack.length === n) {
            happyStrings.push(stack.join(""));
            return
        }

        for (const letter of "abc") {
            if (letter !== stack.at(-1)) dfs([...stack, letter]);
        }
    };

    for (const letter of "abc") dfs([letter]);

    happyStrings.sort();

    return (k <= happyStrings.length) ? happyStrings[k - 1] : "";
};