function findDifferentBinaryString(nums: string[]): string {
    const convertToString = (num: number, N: number) => {
        let numInBinary: string = Number(num).toString(2);
        while (numInBinary.length < N) {
            numInBinary = "0" + numInBinary;
        }
        return numInBinary;
    };

    const N: number = nums.length;
    const allBinaryStrings: Set<string> = new Set<string>(nums);
    for (let num = 0; num < 2 ** N; num++) {
        const numInBinary: string = convertToString(num, N);
        if (!allBinaryStrings.has(numInBinary)) {
            return numInBinary;
        }
    }

    return "";
};