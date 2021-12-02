export const readListAndNumberify = (input: string): number[] => input.split('\n').map((e) => parseInt(e, 10));

export const decreasedMesure = (part: string, input: number[]): void => {
    let result = 0;
    for (let i = 0; i < input.length; i++) {
        if (input[i + 1] > input[i]) {
            result++;
        }
    }
    console.info(`${part}: ${result}`);
};

export const makeWindowsByThree = (input: number[]): number[] => {
    const windows = [];
    for (let i = 0; i < input.length - 2; i++) {
        windows.push(input[i] + input[i + 1] + input[i + 2]);
    }

    return windows;
};

export const dayOne = (inputData: string): void => {
    const cleanData = readListAndNumberify(inputData);
    decreasedMesure('Part 1', cleanData);
    const windows = makeWindowsByThree(cleanData);
    decreasedMesure('Part 2', windows);
};
