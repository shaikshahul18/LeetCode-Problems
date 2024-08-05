function addNumbersToArray(nums, timesOfExecution){
    var ansArray = [];
    while(timesOfExecution != 0){
        for(var i =0; i<nums.length;i++){
            ansArray.push(nums[i])
        }
        timesOfExecution--;
    }
    return ansArray;
};