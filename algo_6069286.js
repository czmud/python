



function rotateArray(arr, shiftBy) {
    if(shiftBy < 0){
        shiftBy = (shiftBy % arr.length) + arr.length;
    } else {
        shiftBy = shiftBy % arr.length;
    }
    
    if(arr.length <= 1 || shiftBy === 0){
        return arr;
    }
    
    let newPosition = shiftBy;
    let tempPosition = 0;
    let temp = [];
    for(let i = 0; i < arr.length; i++){
        newPosition = (i + shiftBy) % arr.length;
        if(i < shiftBy){
            temp.push(arr[newPosition]);
            arr[newPosition] = arr[i];
        } else {
            tempPosition = (i - shiftBy);
            //console.log("tempP:" +tempPosition);
            //console.log(temp);
            arr[newPosition] = temp[tempPosition];
        }
    }
    return arr;
}


// Test Cases

console.log(rotateArray([1,2,3,4,5],1));
// console.log(rotateArray([3,7],1));
// console.log(rotateArray([1,2,3,4,5],3));
// console.log(rotateArray([6,17,21,3],-2));
// console.log(rotateArray([89],1));
// console.log(rotateArray([6,21,15,-8],17));
// console.log(rotateArray([6,21,15,-8],18));


let x = 5;