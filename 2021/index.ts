import { readFileSync } from 'fs';

export const readFile = (): string => readFileSync('input.txt', { encoding: 'utf8' }).trim();

const main = (): void => {
    console.info(readFile());
};

main();
