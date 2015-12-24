# December 22nd Notes

## Form Basics


## Event Handlers vs. Event Listeners

**Event Handlers**
```javascript
elem.onclick = function() {
  console.log('HOHOHO!');
};
```
- event handlers like this can only handle one function
- could cause potential conflicts with other scripts run on the same page

```javascript
elem.addEventListener('click', function() {
  console.log('HOHOHO!');
});
```
- many event listeners can be attached to (and removed from) an element
- less likely to cause conflicts with other scripts

## Page Load Events

The **DOMContentLoaded** event is fired when the initial HTML document has been completely loaded and parsed, _without_ waiting for stylesheets, images, and subframes to finish loading. A very different event - **load** - should be used only to detect a fully-loaded page. It is an incredibly popular mistake to use **load** where **DOMContentLoaded** would be much more appropriate, so be cautious.

My preferred form:
```javascript
var globalLimit,
    counterVar;

function incrementCounter() {
    if (counterVar >= globalLimit) {
      counterVar = 0;
    }
    else {
      counterVar += 1;
    }
    console.log(counterVar);0
}

function init() {
    globalLimit = 100;
    counterVar = 0;
    // assuming there's only one button on the page
    document.getElementsByTagName('button').addEventListener('click', incrementCounter, false);
    incrementCounter();
}

document.addEventListener('DOMContentLoaded', init, false);
```
## Wrapper Objects
_they do weird things_

Avoid 'new-ing' built-in objects as wrappers around primitive types.
prefer



## Code Organization
_code is more often read than written. Write code for humans._
```javascript
// variables to set a limit and a counter, initialized in the init function
var globalLimit,
    counterVar;
/**
* update the output element on the page to match the number of clicks tracked
* by counterVar.
* @param {resultElem} The element where the number of clicks will be displayed
* @return {undefined}
*/
function updateDisplay(resultElem) {
  // resultElem.innerText = counterVar;

// EXAMPLE: another way, without global counter
//   if (resultElem.innerText === '') {
//     resultElem.innerText = 0;
//   }
//   else {
//     resultElem.innerText = Number(resultElem.innerText) + 1;
//   }
// }

/**
* increment a global counter variable by one up to a global limit,
* or reset it to zero if it reaches the global limit, then call updateDisplay.
* @param {counterOutput}
* @return {undefined}
*/
function incrementCounter(counterOutput) {
  if (counterVar >= globalLimit) {
    counterVar = 0;
  }
  else {
    counterVar += 1;
  }
  updateDisplay(counterOutput);
}

/**
* initialize global variables and set up event listeners
* @return {undefined}
*/
function init() {
  globalLimit = 10;
  counterVar = 0;
  var clickCounter = document.getElementById('click-count');
  // assuming there's only one button on the page, or we only want the first one
  document.getElementsByTagName('button')[0].addEventListener('click', function () {
      incrementCounter(clickCounter);
  }, false);
  updateDisplay(clickCounter);
  // call other setup code here
  // if creating a lot of event listeners, consider using a separate function
}

// wait for the initial DOM to load, but not other resources
document.addEventListener('DOMContentLoaded', init, false);
```
