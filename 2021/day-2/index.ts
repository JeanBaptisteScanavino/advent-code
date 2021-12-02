const readListAndShapefy = (input: string): string[][] => input.split('\n').map((e) => e.split(' '));

const readMouvement = (input: string[][]): number => {
    let horizontalPosition = 0;
    let depth = 0;
    input.forEach((element) => {
        switch (element[0]) {
            case 'forward':
                horizontalPosition += parseInt(element[1], 10);
                break;
            case 'down':
                depth += parseInt(element[1], 10);
                break;
            case 'up':
                depth -= parseInt(element[1], 10);
                break;
            default:
                // eslint-disable-next-line no-console
                console.log('error Default statement');
                break;
        }
    });

    return horizontalPosition * depth;
};
export const dayTwo = (inputData: string): void => {
    const dataList = readListAndShapefy(inputData);
    const result = readMouvement(dataList);
    // eslint-disable-next-line no-console
    console.log(result);
};
