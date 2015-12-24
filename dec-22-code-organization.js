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
  resultElem.innerText = counterVar;

// EXAMPLE: another way, without global counter
//   if (resultElem.innerText === '') {
//     resultElem.innerText = 0;
//   }
//   else {
//     resultElem.innerText = Number(resultElem.innerText) + 1;
//   }
// }

}
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
