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

## `Promise.resolve()`
The `Promise.resolve()` method returns a Promise object that is resolved with a given value. If the value is a promise, that promise is returned; if the value is a thenable (i.e. has a `"then" method`), the returned promise will "follow" that thenable, adopting its eventual state; otherwise the returned promise will be fulfilled with the value.
### Syntax
`Promise.resolve(value);`
## Parameters
### value
**Argument** to be resolved by this `Promise`. Can also be a `Promise` or a thenable to resolve.

## Return value
A `Promise` that is resolved with the given value, or the promise passed as value, if the value was a promise object.

## Description
The static `Promise.resolve` function returns a `Promise` that is resolved.

## Composition
`Promise.resolve()` and `Promise.reject()` are shortcuts
to manually create an already resolved or rejected promise respectively. This can be useful at times.
`Promise.resolve()` and `Promise.reject()` are two composition tools for running asynchronous operations in parallel