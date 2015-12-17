# Objects in Javascript

  ## Objects are collections key-value pairs

  - Objects are very similar to Python dictionaries
  - Keys can be either **properties**(data) or **methods**(functions)
  - Keys can be any valid Javascript data type, including another object

  ## Ways to create objects

  #### Object Literal Notation

```javascript
    //hard-coded object, comma-separated key-value pairs
    var person = {
      firstname: "Evan",
      lastname: "Palmer",
      favoriteFood: "anything coconut",
      age: 25.8
    };

    // invoking the built-in Object constructor
    // creates an empty Object
    var guido = new Object();
    var johnDoe = {};

    // create a property with bracket notation
    guido["name"] = "Guido van Rossum";
    // create a property with dot notation
    guido.age = 59;
    console.log("The guido object is: ", guido);

    // access properties the same way
```
  Both of these methods give you an empty object.

  You can add properties to an object anytime in two different ways:

```javascript
  var first = person["firstname"];
  var second = person.lastname;
```
