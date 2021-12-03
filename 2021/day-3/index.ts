/* eslint-disable no-console */
const readInput = (input: string): number[][] => input.split('\n').map((e) => e.split('').map((f) => parseInt(f, 10)));

const transformInputInFinalBit = (data: number[][]): number[] => {
    const finalBit = [];
    for (let i = 0; i < data[0].length; i++) {
        let number = 0;
        for (let j = 0; j < data.length; j++) {
            number += data[j][i];
        }
        if (number > data.length / 2) {
            finalBit.push(1);
        } else {
            finalBit.push(0);
        }
    }

    return finalBit;
};

const reverseBit = (fiveBit: number[]): number[] => {
    const result = [];
    fiveBit.flatMap((bit) => (bit ? result.push(0) : result.push(1)));

    return result;
};

export const dayThree = (inputData: string): void => {
    const data = readInput(inputData);
    const finalBit = transformInputInFinalBit(data);
    const reverseFinalBit = reverseBit(finalBit);
    const finalDecimal = parseInt(finalBit.join(''), 2);
    const reversefinalDecimal = parseInt(reverseFinalBit.join(''), 2);

    console.log(finalDecimal * reversefinalDecimal);
};
