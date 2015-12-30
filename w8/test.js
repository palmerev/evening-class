// console.log(anonymousGreet);

var anonymousGreet = function (name) {
  console.log("Hello " + name);
  throw "Oops!";
}
anonymousGreet("John");
