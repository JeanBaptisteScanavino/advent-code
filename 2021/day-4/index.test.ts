import { dayFour } from './index';
import { readFile,checkRow } from './index';


describe('Unit tests', () => {
    it('Runs a simple test', () => {
        expect(checkRow([
            [ 14, 21, 17, 24, 4 ],
            [ 10, 16, 15, 9, 19 ],
            [ 18, 8, 23, 26, 20 ],
            [ 22, 11, 13, 6, 5 ],
            [ 2, 0, 12, 3, 7 ]
          ], 4, [
            7,  4,  9,  5, 11, 17, 23,  2,
            0, 14, 21, 24, 10, 16, 13,  6,
           15, 25, 12, 22, 18, 20,  8, 19,
            3, 26,  1
         ]).toBeFalsy());
    });
});
