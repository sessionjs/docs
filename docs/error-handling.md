# Error handling

Session.js validates and handles a lot of errors for you, wrapping them in special different classes, so you can easily handle them on your abstract level. 

However, you absolutely should always handle errors when calling any method in Session.js. At the very least, to not crash your entire production server with unhandled thrown error.

To handle errors correctly, install [@session.js/errors](https://www.npmjs.com/package/@session.js/errors):

```
bun add @session.js/errors
```

All errors extend from SessionJsError class, which itself extends from Error class.

Example of handling errors:

```ts
import { Session, ready } from '@session.js/client'
import { 
  SessionValidationError, 
  SessionValidationErrorCode, 
  SessionJsError 
} from '@session.js/errors'
await ready

const session = new Session()

try {
  session.setMnemonic('invalid mnemonic') // <- throws SessionValidationError, which extends from generic Error class
} catch(e) {
  if(e instanceof SessionValidationError) {
    if(e.code === SessionValidationErrorCode.InvalidMnemonic) {
      console.error('You entered invalid mnemonic!') // <- `e` will have code property with one of SessionValidationErrorCode enums
    } else {
      // some other SessionValidationError error
      console.error(e.code)
    }
  } else if(e instanceof SessionJsError) {
    // another error not related to validation, but related to Session.js
    console.error(e.code)
  } else if(e instanceof Error) {
    // unknown error that was thrown by javascript, not Session.js
    console.error(e.message)
  } else {
    // generally all errors in JavaScript extend from Error class, but
    // it is possible to throw primitive values like `throw "primitive string"`
    throw e
  }
}
```
