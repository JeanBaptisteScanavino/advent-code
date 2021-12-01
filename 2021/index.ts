import { decreasedMesure, makeWindowsByThree, readListAndNumberify } from './day-1';
import { readFileSync } from 'fs';

export const readFile = (): string => readFileSync('input.txt', { encoding: 'utf8' }).trim();

const main = (): void => {
    const inputData= readFile()
    const cleanData = readListAndNumberify(inputData)
    decreasedMesure('Part 1', cleanData)
    const windows = makeWindowsByThree(cleanData)
    decreasedMesure('Part 2', windows)
};

main();
