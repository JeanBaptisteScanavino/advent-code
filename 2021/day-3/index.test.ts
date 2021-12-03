import { readFile } from './index';

describe('Unit tests', () => {
    it('Runs a simple test', () => {
        expect(readFile().trim()).toBe('Hello world');
    });
});
