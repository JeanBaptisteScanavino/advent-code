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

const keepData = (data, number, toKeep, i) => {
    const dataToKeep = []
    let j= 0;
    let counter=0;
    while (counter < number && j < data.length){
        if (data[j][i]=== toKeep){
            dataToKeep.push(data[j])
            counter++;
        }
        j++;
    }

    return dataToKeep;
 }


const lookForoxigen = (data) => {
    for (let i = 0; i < data[0].length; i++) {
        let number = 0;
        for (let j = 0; j < data.length; j++) {
            number += data[j][i];
        }
        if (number >= data.length / 2) {
            // console.log(`data ${data}, number : ${number}, i ${i} `)
            data = keepData(data, number, 1, i);
        } else {
            data = keepData(data, data.length - number, 0, i); 
        }
        console.log(data);
        if (data.length === 1 ){

            return data;
        }
    }
}
const lookForCarbone = (data)=> {
    for (let i = 0; i < data[0].length; i++) {
        let number = 0;
        for (let j = 0; j < data.length; j++) {
            number += data[j][i];
        }
        if (number < data.length / 2) {
            data = keepData(data, number, 1, i);
        } else {
            data = keepData(data, data.length - number, 0, i); 
        }
        console.log(data);
        if (data.length === 1 ){

            return data;
        }
    }
}
const toDecimal = (input) => parseInt(input[0].join(''), 2)

export const dayThree = (inputData: string): void => {
    const data: number[][] = readInput(inputData);
    // const finalBit = transformInputInFinalBit(data);
    // const reverseFinalBit = reverseBit(finalBit);
    // const finalDecimal = parseInt(finalBit.join(''), 2);
    // const reversefinalDecimal = parseInt(reverseFinalBit.join(''), 2);
    const determineOxigen = lookForoxigen(data);
    const determineCarbone= lookForCarbone(data);
    // console.log(`oxygen ${determineOxigen}`);
    // console.log(`carbone ${determineCarbone}`)
    console.log(toDecimal(determineOxigen) * toDecimal(determineCarbone))

    // console.log(finalDecimal * reversefinalDecimal);
};
