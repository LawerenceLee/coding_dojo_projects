// Page 16

////////////////////////////////////////////////////////////////////////////////
// Setting and Swapping
// Set myNumber to 42. Set myName to your name.
// Now swap myNumber into myName & vice versa.

var myNumber = 42;
var myName = "Zach";
var temp = myNumber;
myNumber = myName;
myName = temp;

// console.log("Name: " + myName)
// console.log("Number: " + myNumber)


////////////////////////////////////////////////////////////////////////////////
// Print -52 to 1066
// Print integers from -52 to 1066 using a FOR loop.

for (var x=-52; x<1067; x++) {
    console.log(x);
}


////////////////////////////////////////////////////////////////////////////////
// Don’t Worry, Be Happy
// Create beCheerful(). Within it, console.log string "good
// morning!" Call it 98 times.

function beCheerful() {
        console.log("good morning!");
}

for (var x=1; x<99; x++) {
    beCheerful();
}


////////////////////////////////////////////////////////////////////////////////
// Multiples of Three – but Not All 
// Using FOR, print multiples of 3 from -300 to 0.
// Skip -3 and -6.

for (var x=-300; x<1; x++) {
    if (x == -3 || x == -6) {}
    else if (x % 3 == 0) {
        console.log(x)
    }
}


////////////////////////////////////////////////////////////////////////////////
// Printing Integers with While
// Print integers from 2000 to 5280, using a WHILE

var num = 2000;
while (num != 5281) {
    console.log(num)
    num++
}


////////////////////////////////////////////////////////////////////////////////
// You say it's your birthday
// If 2 given numbers represent your birth month and day in
// either order, log "How did you know?", else log "Just another 
// day...."

function isBirthday(a,b) {
    if (a === 12 || b === 12) {
        if (a === 5 || b === 5) {
            console.log("How did you know?");
            return
        }
    }
    console.log("Just another day....");
}


////////////////////////////////////////////////////////////////////////////////
// Leap Year
// Write a function that determines whether a given year is a 
// leap year. If a year is divisible by four, it is a leap year, 
// unless it is divisible by 100. However, if it is divisible by 
// 400, then it is

function isLeapYear(year) {
    var isLeap = false;
    if (year % 4 === 0) {
        if (year % 100 === 0) {
            if (year % 400 === 0) {
                isLeap = true;
            }
        }
        else {
            isLeap = true;
        }
    }
    console.log("It is " + isLeap + " that " + year + " is a leap year.")
}


////////////////////////////////////////////////////////////////////////////////
// Print and Count
// Print all integer multiples of 5, from 512 to 4096.
// Afterward, also log how many there were.

var count = 0;
for (var x=512; x<4097; x++) {
    if (x % 5 == 0) {
        console.log(x)
        count += 1
    }
}


////////////////////////////////////////////////////////////////////////////////
// Multiples of Six
// Print multiples of 6 up to 60,000, using a WHILE.

var num = 6;
while (num != 60001) {
    if (num % 6 === 0) {
        console.log(num)
    }
    num++
}


////////////////////////////////////////////////////////////////////////////////
// Counting, the Dojo Way
// Print integers 1 to 100. If divisible by 5, print
// "Coding" instead. If by 10, also print " Dojo".

var num = 1;
while (num != 101) {
    if (num % 5 === 0 && num % 10 === 0) {
        console.log("Coding Dojo");
    }
    else if (num % 5 === 0) {
            console.log("Coding");
    }
    else {
        console.log(num)
    }
    num++
}


////////////////////////////////////////////////////////////////////////////////
// What Do You Know?
// Your function will be given an input parameter incoming. 
// Please console.log this value.

function isKnown(incoming) {
    console.log(incoming);
}


////////////////////////////////////////////////////////////////////////////////
// Whoa, That Sucker’s Huge...
// Add odd integers from -300,000 to 300,000, and console.log
// the final sum. Is there a shortcut?

var sum = 0;
for (var num=0; num<300001; num++) {
    if (num % 2 !== 0) {
        sum += num
    }
}
console.log(sum + (-sum))


////////////////////////////////////////////////////////////////////////////////
// Countdown by Fours
// Log positive numbers starting at 2016, counting
// down by fours (exclude 0), without a FOR loop.

var num = 2016;
while (num != 3) {
    if (num % 4 === 0) {
        console.log(num)
    }
    num--
}


////////////////////////////////////////////////////////////////////////////////
// Flexible Countdown
// Based on earlier “Countdown by Fours”, given lowNum, highNum,
// mult, print multiples of mult from highNum down to lowNum,
// using a FOR. For (2,9,3), print 9 6 3 (on successive lines).

function flexableCountdown(lowNum, highNum, mult) {
    for (var x=highNum; x>=lowNum; x--) {
        if (x % mult === 0) {
            console.log(x)
        }
    }
}


////////////////////////////////////////////////////////////////////////////////
// The Final Countdown
// This is based on “Flexible Countdown”. The parameter names 
// are not as helpful, but the problem is essentially identical; 
// don’t be thrown off! Given 4 parameters (param1,param2,param3,
// param4), print the multiples of param1, starting at param2 
// and extending to param3. One exception: if a multiple is 
// equal to param4, then skip (don’t print) it. Do this using a 
// WHILE. Given (3,5,17,9), print 6,12,15 (which are all of the 
// multiples of 3 between 5 and 17, and excluding the value 9).

function finalCountdown(param1, param2, param3, param4) {
    var num = param2;
    while (num != (param3+1)) {
        if (num % param1 === 0) {
            if (num % param4 === 0) {
            }
            else {
                console.log(num)
            }
        }
        num++
    }
}


// Page 20


////////////////////////////////////////////////////////////////////////////////
// Countdown
// Create a function that accepts a number as an input. Return a 
// new array that counts down by one, from
// the number (as array’s ‘zeroth’ element) down to 0 (as the 
// last element). How long is this array?

function countdown(num) {
    var arr = [];
    for (var x=num; x>=0; x--) {
        arr.push(x)
    }
    return arr
}

var num = 5;
if (countdown(num).length === num + 1) {
    console.log("The array's length is always one more than the import number due to the inclusion of zero.")
}


////////////////////////////////////////////////////////////////////////////////
//  Print and Return
// Your function will receive an array with two numbers. Print 
// the first value, and return the second.

function printReturn(arr) {
    console.log(arr[0]);
    return arr[1];
}


////////////////////////////////////////////////////////////////////////////////
// First Plus Length
// Given an array, return the sum of the first value in the 
// array, plus the array’s length. What happens if
// the array’s first value is not a number, but a string (like 
// "what?") or a boolean (like false).

function firstPlusLength(arr) {
    if (typeof arr[0] == "number") {
        return arr[0] + arr.length;
    }
    else {
        throw "TypeError: '" + arr[0] + "' is not of type 'number'";
    }
}

////////////////////////////////////////////////////////////////////////////////
// Values Greater than Second
// For [1,3,5,7,9,13], print values that are greater than its 2 nd value. 
// Return how many values this is.

function secondGreater(){
    var arr = [1,3,5,7,9,13]
    var count = 0;
    for (var x=0; x<arr.length; x++) {
        if (arr[x] > arr[1]) {
            console.log(arr[x])
            count += 1
        }
    }
    return count;
}

////////////////////////////////////////////////////////////////////////////////
// Values Greater than Second, Generalized
// Write a function that accepts any array, and returns a new array with the array values that are greater than its 2nd value. Print how many values this is. What will you do if the array is only one element long?

function greaterThanSecond(arr) {
    var count = 0;
    for (var x=0; x<arr.length; x++) {
        if (arr[x] > arr[1]) {
            console.log(arr[x])
            count += 1
        }
    }
    return count;
}
greaterThanSecond([1,3,5,7,9,13])


////////////////////////////////////////////////////////////////////////////////
// This Length, That Value
// Given two numbers, return array of length num1 with
// each value num2. Print "Jinx!" if they are same.

function lengthValue(num1, num2) {
    var arr = [];
    if (num1 === num2) {
        console.log("Jinx!");
    }
    for (var x=0; x<num1; x++) {
        arr.push(num2);
    }
    return arr;
}


////////////////////////////////////////////////////////////////////////////////
// Fit the First Value
// Your function should accept an array. If value at [0] is greater than
// array’s length, print "Too big!";
// if value at [0] is less than array’s length, print "Too small!"; otherwise 
// print "Just right!".

function fitFirstValue(arr) {
    var arrLen = arr.length;
    var firstVal = arr[0]
    if (firstVal > arrLen) {
        console.log("Too big!")
    }
    else if (firstVal < arrLen) {
        console.log("Too small!")
    }
    else {
        console.log("Just right!")
    }
}



////////////////////////////////////////////////////////////////////////////////
// Fahrenheit to Celsius
// Kelvin wants to convert between temperature scales. Create 
// fahrenheitToCelsius(fDegrees)
// that accepts a number of degrees in Fahrenheit, and returns the equivalent 
// temperature as expressed
// in Celsius degrees. For review, Fahrenheit = (9/5 * Celsius) + 32.

function fahrenheitToCelsius(fDegrees) {
    return ((fDegrees - 32) * (5/9))
}



////////////////////////////////////////////////////////////////////////////////
// Celsius to Fahrenheit
//Create celsiusToFahrenheit(cDegrees) that accepts number of degrees Celsius, 
// and returns the equivalent temperature expressed in Fahrenheit degrees.

function celsiusToFahrenheit(cDegrees) {
    return (9/5) * cDegrees + 32
} 

// (optional) Do Fahrenheit and Celsius values equate at a certain number? 
// Scientific calculation can be complex, so for this challenge just try a 
// series of Celsius integer values starting at 200, going downward
// (descending), checking whether it is equal to the corresponding Fahrenheit 
// value.

for (var x=200; x>-201; x--) {
    if (x == fahrenheitToCelsius(x)){
        console.log(x)
    }
}

// Answer: -40


////////////////////////////////////////////////////////////////////////////////
// Biggie Size
// Given an array, write a function that changes all positive numbers in the 
// array to “big”. Example: makeItBig([-1,3,5,-5]) returns that same array, 
// changed to [-1,"big","big",-5].

function makeItBig(arr) {
    for (var x=0; x<arr.length; x++) {
        if (arr[x] > 0) {
            arr[x] = "big";
        }
    }
    return arr
}
makeItBig([-1,3,4,-5])



////////////////////////////////////////////////////////////////////////////////
// Print Low, Return High
// Create a function that takes array of numbers. The function should print 
// the lowest value in the array, and return the highest value in the array.

function printLowReturnHigh(arr) {
    var max = arr[0];
    var min = arr[0];
    for (var x=1; x<arr.length; x++) {
        if (arr[x] > max) {
            max = arr[x];
        }
        else if (arr[x] < min) {
            min = arr[x];
        }
    }
    console.log(min);
    return max
}


////////////////////////////////////////////////////////////////////////////////
// Print One, Return Another
// Build a function that takes array of numbers. The function should print 
// second-to-last value in the array, and return first odd value in the array.

function printOneReturnAnother(arr) {
    console.log(arr[arr.length-2])
    for (var x=0; x<arr.length; x++) {
        if (arr[x] < 0) {
            return arr[x] 
        }
    }
}
printOneReturnAnother([2,3,-6,5,4])


////////////////////////////////////////////////////////////////////////////////
// 