import { readFileSync } from "fs";
import {readFile as toTestReadFile} from './day-4/index'

const readFile = (): string => readFileSync('./day-4/inputTest.txt', { encoding: 'utf8' }).trim();

describe('Unit tests', () => {
    it('Runs a simple test', () => {
        expect(toTestReadFile()).toBe('Hello world');
    });
});
