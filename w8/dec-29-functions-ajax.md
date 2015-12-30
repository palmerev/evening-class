### Scope and Hoisting
When JavaScript runs your code, it does so in two phases: the creation phase and the execution phase. During the creation phase, it scans the code and prepares memory space for all variables and functions. The execution phase actually runs each line of code as it is encountered.

**Creation Phase**
- Function statements are loaded into memory.
- Variables are all set to the special JavaScript value `undefined`. This means that the variable exists in memory, but hasn't been assigned a value yet.
- Because functions have their own scope and execution context, their local variables go through the same process.  

Because functions are loaded into memory completely _before_ the execution phase. This is valid code:

```javascript
sayHi(); // logs "Hi!"

function sayHi() {
  console.log("Hi!");
}
```
**Note**: As a best practice, it's better to organize your code so that functions are called _after_ they're defined. However, JavaScript won't complain if you call a function before it's defined.

JavaScript looks for variables during the creation phase and the **names** are loaded into memory:

```javascript
var a; // CREATION PHASE only loads name 'a' as undefined
// CREATION PHASE ignores the rest
console.log(a);
a = 3;
console.log(a);
```

**Execution Phase**

Code is executed line by line. Values are assigned to variables at runtime.

```javascript
var a; // EXECUTION PHASE sees the name a is already in memory
console.log(a); // logs undefined
a = 3; // sets a equal to 3
console.log(a); // logs 3
```


### Function Statements vs. Function Expressions

*Statements __do work__*. *Expressions __return a value.__*

---

**Expressions**
```javascript
var a; // setup
a = 3; // the assignment operator returns 3;
2 + 2; // the plus operator returns 4;
```

**Statements**
```javascript
var b;
if(...)
```
Functions can be created in a few different ways.

Here's an example of the most common way, a function statement:

```javascript
function greet(name) {
  console.log("Hello " + name);
}
```

When JavaScript encounters this statement, it loads the function definition into memory, but the code doesn't __do__ anything at that point. To actually execute the function, call it with parentheses.

```javascript
greet("John"); // logs "Hello John" to the console
```

Because JavaScript functions are __hoisted__, meaning loaded into memory before any code is excuted, it can be called before the definition in the code:

```javascript
greet("John"); // logs "Hello John"


function greet(name) {
  console.log("Hello " + name);
}
```

Functions can also be created using an **expression**. An expression is a unit of code that returns a value. This may or may not be saved in a variable. Here I'm creating a function using a function expression:

```javascript
var anonymousGreet = function (name) {
  console.log("Hello " + name);
}
```

Here we're creating an anonymous function on the fly and assigning to a variable. If we console.log the variable `anonymousGreet`, we'll see that it's value _is_ the anonymous function we just created.

What do you think will happen if I try to call `anonymousGreet` before it's assigned? (What is in memory?)

```javascript
anonymousGreet("John");

var anonymousGreet = function (name) {
  console.log("Hello " + name);
}
```

You may also notice that if an error occurs inside an anonymous function, the traceback says the error occurred inside `(anonymous function)`, which is less helpful than seeing the name of a function, especially when the traceback is large and complex.

However, anonymous functions are good for certain things. They are sometimes necessary when passing parameters to an inner callback function:

```javascript
element.addEventListener('click', function () {
  toggleMenu(param1, param2);
}, false);
```

### APIs, AJAX, and XMLHttpRequest

**API**: Application Programming Interface

A way of exposing data or functionality to programmers through code.

Two kinds:

- APIs provided by languages and libraries (and browsers)
  * Javascript's built-in `Math`, `Date` (programmers can access properties and methods)
  * jQuery provides a similar API with more dollar-signs
  * DOM manipulation relies on an API provided by browsers. `document`, `window`, `getElementById`, etc. are part of the browser's DOM API, not JavaScript.
  * Browsers also provide an API for making asynchronous requests, usually `XMLHttpRequest` (XHR), which we will look at next.

- _Web_ APIs
  * Provides ways of interacting with data through HTTP requests to particular URLs ("endpoints")
  * A website can load content dynamically (without refreshing) from their APIs by requesting data in the background with _AJAX_ (see below)
  * The random quote API endpoint we are targeting returns JSON data that we can load without refreshing the page

**AJAX** stands for _Asynchronous JavaScript and XML_, however, since XML is no longer the dominant data format returned by most APIs, the _X_ in AJAX can now be treated as a reference to the browsers' `XMLHttpRequest` (XHR) API used for making asynchronous requests.

The basic format of an `XMLHttpRequest` is:
  1) create a new XMLHttpRequest
  2) open the request with the desired HTTP method, target url (followed by optional `true` if the request should be asynchronous)
    **NOTE**: support for _synchronous_ requests doesn't exist in IE 10+ and is being phased out in other browsers because of the detrimental effects of making them.
  3) give JavaScript a callback function to execute when the request completes (a `load` event)
  4) send the request

```javascript
 var request = new XMLHttpRequest();
 request.open("GET", "http://www.foo.com");
 request.addEventListener("load", function () {
   console.log(this.responseText);
 })
 request.send(); // sometimes you'll see request.send(null) or request.send(someVar=someValue)
```

**NOTE**: you may have to use the `readystatechange` event instead of the `load` event to support older browsers.
See [AJAX Getting Started on MDN](https://developer.mozilla.org/en-US/docs/AJAX/Getting_Started)

[XMLHttpRequest documentation on MDN](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest)
[Using XMLHttpRequest on MDN](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/Using_XMLHttpRequest)
