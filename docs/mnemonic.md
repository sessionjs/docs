# Mnemonic encoding & decoding

Use [@session.js/mnemonic](https://www.npmjs.com/package/@session.js/mnemonic) for operations related to mnemonic.

```
bun add @session.js/mnemonic
```

```ts
import { encode, decode } from '@session.js/mnemonic'

const seed = decode('love love love love love love love love love love love love')
console.log('Account seed', seed)
const mnemonic = encode(seed)
console.log('Encoded mnemonic', mnemonic) // => love love love love love love love love love love love love
```

## Generate random mnemonic

To create a new Session instance with random mnemonic, you have to use two packages: @session.js/mnemonic and @session.js/keypair

```
bun add @session.js/mnemonic @session.js/keypair
```

Now generate random seed and encode it to get random mnemonic

```ts
import { generateSeedHex } from '@session.js/keypair'
import { encode } from '@session.js/mnemonic'
import { Session, ready } from '@session.js/client'
await ready

const mnemonic = encode(generateSeedHex())
console.log('Mnemonic', mnemonic)

const session = new Session()
session.setMnemonic(mnemonic)
```

### Add your own mnemonic language

You generally really shouldn't do that, because you have to find a secure compatible words dictionary first that will work with the system. This is how you add language to mnemonic encoder/decoder:

```ts
import { decode, mnemonicLanguages, addMnemonicLanguage } from '@session.js/mnemonic'

mnemonicLanguages.russian = addMnemonicLanguage({
  prefixLen: 3,
  words: [/* ... */]
})
decode('любовь любовь любовь любовь любовь любовь любовь любовь любовь любовь любовь любовь любовь', 'russian')
```
