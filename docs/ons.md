# Oxen Name System (ONS)

ONS is a system of usernames that links you to registered Session ID mapping and allows you to buy mapping for a few other lokinet products. For more info on ONS, go to [What is ONS?](./principles/users.md#what-is-ons)

## ONS resolving

Use [@session.js/ons](https://www.npmjs.com/package/@session.js/ons). This is a utility module that does not depend on any other packages published in @session scope.

```
bun add @session.js/ons
```

```ts
import { resolve } from '@session.js/mnemonic'

await resolve('hloth') // => 057aeb66e45660c3bdfb7c62706f6440226af43ec13f3b6f899c1dd4db1b8fce5b
```