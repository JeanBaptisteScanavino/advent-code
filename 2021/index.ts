import { dayFive } from './day-5';
import { readFileSync } from 'fs';
import { dayOne } from './day-1';
import { dayTwo } from './day-2';
import { dayThree } from './day-3';
import { dayFour } from './day-4';

export const readFile = (): string => readFileSync('./day-5/input.txt', { encoding: 'utf8' }).trim();

const main = (): void => {
    const inputData: string = readFile();
    // dayOne(inputData);
    // dayTwo(inputData);
    // dayThree(inputData);
    dayFive(inputData);
};

main();
