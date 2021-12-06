export const readFile = (input) => input.split('\n')
                                    .map(e => e.split(' '))
                                    .map(e => e.filter(e => e !== '->'))

const createGrid = (c,r) =>{
    const grid = []
    for(let i = 0; i < r; i++ ){
        grid[i]= [];
        for(let j= 0; j< c; j++){
            grid[i][j] = 0;
        }
    }
    
    return grid;
}

const seeOrientation = (data) => {
    if((data[0][0] - data[1][0] && (data[0][1] - data[1][1]))){
        
        return {'orient': 'diag'};
    }
    if(!(data[0][0] - data[1][0])){
        const dir= data[0][0] - data[1][0] < 0 ? 'left': 'right'
        
        return {'orient': 'horiz', 'direction' : dir};
    }
    const dir= data[0][0] - data[1][0] < 0 ? 'up': 'down'
    
    return {'orient': 'verti', 'direction' : dir};
}

const prepareLine = (data, grid) => {
    data.map(e => {
        let orientation = seeOrientation(e);
        if(orientation.orient === 'horiz'){
            let y =orientation.direction === 'left'
            ? [e[0][1], e[1][1]]
            : [e[1][1], e[0][1]] ;
            let x = e[0][0]
            console.log(x)

            drawLine(orientation.orient,x,y, grid);
        } else if(orientation.orient === 'verti') {
            let x =orientation.direction === 'up'
                ? [e[0][0], e[1][0]] 
                : [e[1][0], e[0][0]] ;
            let y = e[0][1];
        drawLine(orientation.orient, x,y, grid);
    }})
}
const drawLine = (orient, x,y, grid) => {
    console.log(`orient ${orient}, x: ${x}, y: ${y}`)
    // if (orient === 'horiz'){
    //     for(let i= x[0]; i < x[1]; i++){
    //         grid[y][i]++
    //     }
    //     return grid;
    // }
    // for(let i= y[0]; i < y[1]; i++){
    //     grid[i][x]++
    // }
    // return grid;
}

const makeLine = (data) => data.map(e => e.map(e => e.split(',')));

export const dayFive = (inputData): void => {
    const data = readFile(inputData);
    const finalData = makeLine(data)
    console.log(finalData)
    const grid = createGrid(10,10)
    const drawedGrid = prepareLine(finalData,grid)
    // console.log(drawedGrid)
    // console.log(grid)
};

