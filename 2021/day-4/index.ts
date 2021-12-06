import { table } from 'console';
import { sum } from 'lodash';

export const readFile = (inputData:string): string[] => inputData.split('\n\n');

export const playGame = (gameTable, lotoNumber, lotoTableFlat) => {
    const tableOfScore = []
    let haveAWinner = false;
    let counter=0;
    let scoreByTable: number[]= [];
    for(let i = 0; i < gameTable.length; i++){
        scoreByTable[i]= 0;
    }
    while( haveAWinner === false) {
        let number = lotoNumber[counter];
        for(let j = 0; j < lotoTableFlat.length; j++){
            if(lotoTableFlat[j].includes(number))
                {
                scoreByTable[j]++;

                }
            if (scoreByTable[j] >= 5){
                if(checkRow(gameTable[j],counter,lotoNumber)){
                    return {'table': lotoTableFlat[j], 'counter': counter, 'pass': 'row', 'test':number }
                }
                if(checkColumns(gameTable[j],counter,lotoNumber)){
                    return {'table': lotoTableFlat[j], 'counter': counter, 'pass': 'column'  }
                }
            }
        }
        counter++;
        if(counter>=22){
            console.log('end')
            haveAWinner=true;
        }
    }
    return counter;
 }
 export const checkRow = (table,counter,lotoNumber): boolean => {
    let scoreThisRow = false;
    table.forEach(row => {
        let rowScore = 0;
        for(let i = 0; i <= counter; i++){
            if(row.includes(lotoNumber[i])){
                rowScore++;
                if (rowScore === 5){
                    console.log(`row : ${row}`)
                    console.log(table)
                    scoreThisRow= true;
                }
            };
        }
    })
    return scoreThisRow
    // let rowScore = 0;
    // for(let r = 0; r < 5; r++){
    //     for(let c = 0; c<5; c++){
    //         for(let n = 0; n <= counter; n++){
    //             if(table[r][c] === lotoNumber[n]){
    //                 // table[r][c]='.';
    //                 rowScore++;
    //                 // console.log(table)
    //                 if(rowScore === 5){
    //                     console.log(table)
    //                     return true;
    //                 }
    //             }  
    //         }
    //     }
    //     rowScore = 0;
    // }
    // return false
 }
 export const checkColumns = (table, counter, lotoNumber): boolean => {
    let columnScore = 0;
    for(let c = 0; c < 5; c++){
        for(let r = 0; r<5; r++){
            for(let n = 0; n <= counter; n++){
                if(table[r][c] === lotoNumber[n]){
                    columnScore++;
                    if(columnScore === 5){
                        calculateScore({'table':table, 'counter': counter}, lotoNumber)
                        // return true;
                    }
                }  
            }
        }
        columnScore = 0;
    }
    return false
 }
 export const calculateScore = (table, lotoNumber) =>{
    // let tableFiltered = table.table
    let totalScoreOFTable = sum(table.table)
    for(let i  = 0; i <= table.counter; i++){
        if(table.table.includes(lotoNumber[i])){
            totalScoreOFTable -= lotoNumber[i]
        }
    }
    console.log(totalScoreOFTable)
    return totalScoreOFTable * lotoNumber[table.counter]

    // for(let i  = 0; i <= table.counter; i++){
    //     tableFiltered.splice(tableFiltered.indexOf(lotoNumber[i]),1)
    // }
    // console.log(tableFiltered)
    // const scoreOfUnmarkedNumbers = sum(tableFiltered)
    // console.log(lotoNumber[table.counter]*scoreOfUnmarkedNumbers)
    // console.log((46+52+40)*49)
    // return scoreOfUnmarkedNumbers * lotoNumber[table.counter]
 }

 export const dayFour = (inputData): void => {
    const splitInput = readFile(inputData);
    const lotoNumber: number[] = splitInput[0].split(',').map(n => parseInt(n, 10));
    splitInput.shift();
    let lotoTable = splitInput.map((t) => t.split('\n')).map(e => e.map(r => r.trim().split(' ').filter(e => e !== '')));
    lotoTable = lotoTable.map(t => t.map(e => e.map(n => parseInt(n, 10))));
    const lotoTableFlat = lotoTable.map(e => e.flat());
    const gameTable = lotoTable;
    const tableWin = playGame(gameTable, lotoNumber, lotoTableFlat);
    console.log(tableWin)
    const score = calculateScore(tableWin,lotoNumber);
    console.log(score);
};

