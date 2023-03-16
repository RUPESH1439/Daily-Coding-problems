// https://leetcode.com/problems/reverse-integer/description/
// https://leetcode.com/problems/reverse-integer/submissions/916028175/

function reverse(x: number): number {
    let isNegative = false
    if(x < 0){
        isNegative = true
    }
    let length = 0
    let _x = Math.abs(x)
    const numbers:number[] = []
    while(_x > 0){
        numbers.push(_x % 10)
        _x = Math.floor(_x/10)
        length++
    }
    let newNum = 0
    numbers.forEach((num)=>{
        if(isNegative){
        newNum -= num * Math.pow(10, length-1)
        }
        else{
            newNum += num * Math.pow(10, length-1)
        }
        length--;
    })
    return (newNum > -Math.pow(2,31) && newNum < Math.pow(2,31) -1 ) ? newNum: 0
};