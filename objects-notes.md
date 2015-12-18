# Objects in Javascript

## Objects are collections key-value pairs

  Objects group data and the functions that act on that data.
  - Objects are very similar to Python dictionaries
  - Keys can be either **properties**(data) or **methods**(functions)
  - Keys can be any valid Javascript data type, including another object

#### Creating an object with object literal notation

```javascript
//hard-coded object, comma-separated key-value pairs
var person = {
  firstname: "Evan",
  lastname: "Palmer",
  favoriteFood: "anything coconut",
  age: 25.8
};
```

#### Creating an empty object and adding properties

```javascript
// invoking the built-in Object constructor creates an empty Object
// both of these do the same thing
var guido = new Object();
var johnDoe = {};

// create a property with bracket notation
guido["name"] = "Guido van Rossum";
// create a property with dot notation
guido.age = 59;
console.log("The guido object is: ", guido);
```
The dot notation is easier to read and debug (and less typing), so it should be your first choice. However, if you need to access a property dynamically, using a value that can change, the bracket notation will accept a string variable:

```javascript
var propertyIWant = "name";
console.log("guido's name is: ", guido[propertyIWant]);
```

#### Reading object properties
```javascript
// access properties with bracket notation or dot notation
console.log("guido's name is: ", guido.name);
console.log("guido's age is: ", guido["age"])
```
Again, use dot notation if possible.
#### Changing object properties
```javascript
// you can dynamically add and remove properties
guido.nickname = "Benevolent Dictator For Life";
delete guido.age;
// accessing non-existent properties doesn't cause an error!
console.log("guido's age is now: ", guido["age"]);
console.log("guido.blah: ", guido.blah);
```
#### Creating an Object with constructor notation
```javascript
// constructor notation
// usually constructor names are capitalized
function Person(name, age, favoriteFood) {
    "use strict";
    this.name = name;
    this.age = age;
    this.favoriteFood = favoriteFood;
}

// invoking the Person constructor
var luke = new Person("Luke Skywalker", 35, "kale");
var darth = new Person("Darth Vader", "dead", "Sith Soda");

// what happens if I give fewer arguments?
var r2d2 = new Person("R2D2");
```

**WARNING**: Don't forget the 'new' keyword. If you don't include the 'new', the constructor will attach the properties to the global object (window).
This is why some developers prefer using '{}' instead of 'new' for creating empty objects.

#### An aside about 'this'
```javascript
// at the global level, 'this' points to the Window object
console.log("this: ", this);
// all global variables and objects exist on Window

// inside a constructor or object 'this' points to the parent object/function
function Thing() {
    "use strict";
    console.log("Inside the constructor, this is: ", this); // logs Thing()
    this.description = "I'm a thing";
    this.getDescription = function() {
        console.log("inside getDescription, 'this' is: ", this);
        return this.description;
    }
}
```

### More on Objects

#### Objects within objects

  An object property can be another object.
  ```javascript
      var info = {
        prop1: "blah",
        favorites: {
           color: "green",
           food: "ice cream"
        }
      }
      var favoriteFood = info.favorites.food; // gets "ice cream"
  ```

#### Built-in objects

##### The BOM
  The browser implements the Browser Object Model, which includes built-in objects like `window`, `document`, and `screen`.

##### The DOM
  The Document Object Model is the browser's model of the current page. The root is `document`.

##### Global Javascript Objects
  `String`, `Number`, `Boolean`,
  `Date`, `Math`, `Regex`,
  `Object`
