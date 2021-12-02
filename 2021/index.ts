import { readFileSync } from 'fs';
import { dayOne } from './day-1';
import { dayTwo } from './day-2';

export const readFile = (): string => readFileSync('input.txt', { encoding: 'utf8' }).trim();

const main = (): void => {
    const inputData: string = readFile();
    dayOne(inputData);
    dayTwo(inputData);
};

main();
