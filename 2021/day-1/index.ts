export const readListAndNumberify = (input) => input.split('\n').map((e)=> parseInt(e))
    
export const decreasedMesure = (part, input) => {
    let result = 0;
    for(let i=0; i< input.length; i++){
        if (input[i+1]> input[i]){
            result++;
        }
    }
    console.info(`${part}: ${result}`)
}

export const makeWindowsByThree = (input) =>{
    let windows =[]
    for(let i=0; i< input.length-2; i++){
        windows.push(input[i]+input[i+1]+input[i+2])
    }
    return windows;
}