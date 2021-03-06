# 0x0F. ES6 Promises

# Learning Objectives
* Promises (how, why, and what)
* How to use the then, resolve, catch methods
* How to use every method of the Promise object
* Throw / Try
* The await operator
* How to use an async function

## Promise

![](https://res.cloudinary.com/dvovmo7yu/image/upload/v1648522378/promises_hrcteh.png)

A **Promise** is an object representing the eventual completion or failure of an asynchronous operation.

A **Promise** is in one of these states:
* *pending*: initial state, neither fulfilled nor rejected
* *fulfilled*: meaning that the operation was completed successfully
* *rejected*: meaning that the operation failed

![](https://res.cloudinary.com/dvovmo7yu/image/upload/v1648523028/promises_1_p5o3a0.png)

| Method | Description | Syntax |
| ------ | ----------- | ------ |
| `Promise.resolve()` | The static `Promise.resolve` function returns a `Promise` that is resolved. | `Promise.resolve(value);` |
| `Promise.reject()` | The static `Promise.reject` function returns a `Promise` that is rejected. For debugging purposes and selective error catching, it is useful to make `reason` an `instanceof` `Error`. | `Promise.reject(reason);` |
| `Promise.prototype.then()` | The `then()` method returns a Promise. It takes up to two arguments: callback functions for the success and failure cases of the Promise. | <pre>p.then(onFulfilled[, onRejected]); <br>p.then(value => <br> // fulfillment <br>}, reason => { <br> // rejection <br>});</pre> |
| `Promise.prototype.catch()` | The `catch` method is used for error handling in promise composition. Since it returns a `Promise`, it can be chained in the same way as its sister method, `then()`. | <pre>p.catch(onRejected);<br>p.catch(function(reason) {<br>// rejection<br>});</pre> |