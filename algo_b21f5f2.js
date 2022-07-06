

export function arrayBalanceIndex(arr) {
    let leftSum = 0;
    let rightSum = 0;
    for (let i = 0; i < arr.length; i++){
        leftSum = 0;
        rightSum = 0;
        for (let j = 0; j<arr.length; j++){
            if(j < i){
                leftSum += arr[j];
            } else if (j > i){
                rightSum += arr[j];
            }
        }
        if( rightSum === leftSum ){
            return i;
        }
    }
    return -1;
}