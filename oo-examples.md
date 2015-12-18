# More about objects

There are lots of ways to create objects. Thinking about the use cases can help you decide which way is best.

### The how, when, and why of object creation

**Object literal syntax**: pre-initialize your object with everything it needs.
This is good for simple objects in small quantities, or if:
- You know what data each property should start with.
- There will only be one instance of the object.

```javascript
var myLiteralObject = {
    status: "awesome",
    stress: 4,
    /*
      Update the status based on the stress level, and logs the new status.
    */
    updateStatus: function (newStressLevel) {
        this.stress = newStressLevel;
        if (this.stress < 5) {
          this.status = "awesome";
        }
        else if(this.stress > 5 && this.stress < 8) {
            this.status = "kinda stressed";
        }
        else if (this.stress > 8) {
            this.status = "freaking out";
        }
        console.log("new status is: ", this.status);
    }
}
```
**When might you have a singleton object?**
- The single `deck` used in a card game
- The single `map` in an app using location data
- The single `coffeeMachine` for making all the coffee drinks

You can also start with an empty or partial object and add to it later, if the structure needs to be flexible, but this can sometimes make the properties and methods hard to keep track of.

A constructor function _could_ work here too, but constructors really shine when you need to make lots of similar objects using the constructor as a template.

**Constructor function syntax**: declare a function that acts as a template or recipe for creating objects. Then create `new` objects. This is good for creating lots of objects that have the same structure, but different states. Use a constructor if:
- You need to create many similar objects that vary only in the data they hold.
- You like constructors.

Declaring a constructor:
```javascript
function Book(title, author, pages) {
    this.title = title;
    this.author = author;
    this.numPages = pages;
    this.getInfo = function () {
       return this.title + " was written by " + this.author + " and has " + this.numPages + " pages.";
    }
}
```
**Note**: The constructor is only a template and doesn't actually hold any data itself. It is a special kind of function that when called with the keyword `new` creates a new object and returns it to you. Except in some more advanced cases, the only time you should reference the constructor directly is when creating a new object:

```javascript
var book1 = new Book("Harry Potter", "JK Rowling", 350);`.
```

Now `book1` is a `Book` object, so you can access it's properties like `book1.title`. You probably won't need to reference the constructor. It's not an object, so it doesn't have state.
