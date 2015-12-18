//hard-coded object, comma-separated key-value pairs
var person = {
    firstname: "Evan",
    lastname: "Palmer",
    favoriteFood: "anything coconut",
    age: 25.8,
    tellAge: function () {
        "use strict";
        console.log("I am " + this.age + " years old");
    }
};
// console.log("person object: ", person);

// invoking the built-in Object constructor
// creates an empty Object
var guido = new Object();
var janeSmith = Object.create(null);
var johnDoe = {};

// create a property with bracket notation
guido["name"] = "Guido van Rossum";
// create a property with dot notation
guido.age = 59;
// console.log("The guido object is: ", guido);

// access properties either way
// console.log("guido's name is: ", guido.name);
// console.log("guido's age is: ", guido["age"]);

// you can dynamically add and remove properties
guido.nickname = "Benevolent Dictator For Life";
delete guido.age;
// console.log("guido's age is now: ", guido["age"]);
// console.log("guido.blah: ", guido.blah);

// constructor notation
// usually constructor names are capitalized
function Person(name, age, favoriteFood) {
    "use strict";
    // console.log("inside the Person constructor 'this' is pointing to: ", this);
    this.name = name;
    this.age = age;
    this.favoriteFood = favoriteFood;
}

// invoking the Person constructor
var luke = new Person("Luke Skywalker", 35, "kale");
var darth = new Person("Darth Vader", "dead", "Sith Soda");

// what happens if I give fewer arguments?
var r2d2 = new Person("R2D2");

// at the global level, 'this' points to the Window object
console.log("global 'this': ", this);
// all global variables and objects exist on Window

/* This function does a thing.
* It doesn't return anything.
*/
function Thing() {
    "use strict";
    console.log("Inside the constructor, this is: ", this); // logs Thing()
    this.description = "I'm a thing";
    this.getDescription = function() {
        console.log("inside getDescription, 'this' is: ", this);
        return this.description;
    }
}
