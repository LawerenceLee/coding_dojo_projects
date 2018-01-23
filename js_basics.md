# Javascript Basics

## Syntax:

* All JavaScript statements end in a `;`.
* Declaring Variables: `var <var_name> = "text";` or `var <var_name>;`
  * Var names can contain `$`, `_` and `( )`.
* Language employs: `+= -=`
* Language uses camelcase.
* Strings:
    * Can use escape characters.

## Common Functions:

* `alert("<alert message>");` - Opens a pop up that contains your alert message.
* `document.write("<your html>");` - Document refers to the current web page, and write allows you to append html to that page.
* `console.log("<your_message>")` - Prints a message to the console in your browser.
* `prompt("<your_text>");` - Captures input from the user with a popup dialog. Good to insert incoming vaue into a variable.

## Common Properties of variables:

* `<my_var>.length` - Returns the number of charcters in the variable.

## Common Methods:

* `<myVar>.toLowerCase()` - changes all characters to lower case in a string.
* `<myVar>.toUpperCase()` - changes all characters to upper case in a string.

## Run JS scripts in the browser:

```javascript
<script src="your_script_here.js"></script>
```

## Writing JS directly in html:

```javascript
<script>
alert("Hello there.");
</script>
```

## Loading JS console in various Browsers:

### Chrome Console Keyboard Shortcuts

* Windows: Ctrl + Shift + J
* Mac: Cmd + Option + J

### Firefox Console Keyboard Shortcuts

* Windows: Ctrl + Shift + K
* Mac: Cmd + Option + K

### Safari Console Keyboard Shortcuts

* Cmd + Option + C

## Declaring Variables

* Strings, ints, floats and scientific notation are all variable types that can be used.
* Here is an example of scientific notation:

```javascript
var numberOfAtomsOnEarth = 1.33e+105;
```

## Converting Between Types:

* String --> Int:

```javascript
parseInt("10");
```

* String --> Float:

```javascript
parseFloat("3.14");
```

* You can even provide these conversion methods with letter characters mixed (howerver they must be after the number)

```javascript
var width = '190px';
var numOfDivs = 10;
var totalWidth = parseInt(width) * numOfDivs;
// Answer: 1900
```

## Adding variables to strings:

```javascript
var name = prompt("What's your name?");
alert("Hi there " + name + ", welcome aboard.");
```

## The Math Object:

* Provides access to various mathematical operations, such as rounding, triginometric funcitons, etc.

```javascript
Math.round(3.14)
// Answer: 3
Math.ceil(3.14)
// Answer: 4
Math.random()
// Some number between 0 and 1
```

* More info can be found here:
  * [Mozilla Developer Network page on the Math object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math)
  * [Math.round() on the MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/round)

## Operators:
  * `===` - The equality operator
    * Enforces a strict comparison, such that the string 3 does not equal the number three.
  * `==` - Equal to.
    * "3" is equal to 3 with the double equals
  * `!=` and `!==` work in the exact same way.
  * `&&` - And operator
  * `||` - Or operator

## Conditional Statements:

```javascript
if () {

} else if {

} else {

}
```

