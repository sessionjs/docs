# Getting started

Friendly reminder: this package can't be used and won't work with Node.js.

## Installation

By using this software, you are agreeing to abide by [Terms of use](https://github.com/sessionjs/client/blob/main/TERMS.md). Shortly: no abuse and spam, you're solely responsible for your actions with this software.

1. First install bun: https://bun.sh/
2. Create a new Bun project in any directory, using `bun init` or manually
3. Install session.js: `bun add @session.js/client`

Always make sure to await for initialization of library:

```ts
import { ready } from '@session.js/client'
await ready

// ...
```

Otherwise you might get errors like `sodium.crypto_sign_seed_keypair is not a function`

## Quick start

### Sending messages

```ts
import { Session, ready } from '@session.js/client'
await ready

const mnemonic = 'love love love love love love love love love love love love love'
const recipient = '054830367d369d94605247999a375dbd0a0f65fdec5de1535612bcb6d4de452c69'

const session = new Session()
session.setMnemonic(mnemonic, 'My username')
const response = await session.sendMessage({ 
  to: recipient, 
  text: 'Hello world' 
})

console.log('Sent message with id', response.messageHash)
```

!!! Info "See also"
    - [How to use instance with random mnemonic?](./mnemonic.md#generate-random-mnemonic)

### Sending images or files

Attach image from URL to your message:

```ts
const imageData = await fetch('https://picsum.photos/100/100').then(res => res.arrayBuffer())

const file = new File([imageData], 'image.jpg', { type: 'image/jpeg' })
await session.sendMessage({ 
  to: recipient,
  text: 'Image downloaded by URL:',
  attachments: [file]
})
```

Attach file from your file system to your message:

```ts
import path from 'path'
// <...>
const filename = '/Users/kitty/Desktop/image.jpg'
const buffer = await fs.readFile(filename)

const file = new File([buffer], path.basename(filename), { type: 'image/jpeg' })
await session.sendMessage({
  to: recipient, 
  text: 'Image from file:', 
  attachments: [file] 
})
```

### Polling messages

Check [polling page](./polling.md) for more info and examples on polling.

```ts
import { Session, Poller, ready } from '@session.js/client'
import { SnodeNamespaces, type Message } from '@session.js/types'
await ready

const mnemonic = 'love love love love love love love love love love love love love'

const session = new Session()
session.setMnemonic(mnemonic, 'Display name')

const poller = new Poller() // polls every 3 seconds
session.addPoller(poller)

session.on('message', (msg: Message) => {
  console.log('Received new message!', 
    'From:', msg.from,
    'Is from closed group:', msg.type === 'group',
    'Group id:', msg.type === 'group' ? msg.groupId : 'Not group',
    'Text:', msg.text ?? 'No text',
  )

  // If you want to access more properties and experiment with them, use getEnvelope and getContent
  msg.getContent() // => SignalService.Content <- useful message payload
  msg.getCnvelope() // => EnvelopePlus <- message metadata

  // If you want to download attachments, use:
  msg.attachments.forEach(async attachment => console.log(await session.getFile(attachment)))
})
```

## Examples

You can find fully complete examples in [examples repository](https://github.com/sessionjs/examples/)

- [Simple example](https://github.com/sessionjs/examples/tree/main/simple)
- [Browser](https://github.com/sessionjs/examples/tree/main/browser-simple)
