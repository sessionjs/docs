# Sending messages

Sending messages with Session.js requires setting up [storage](./storage/index.md) and [network](./network/index.md). This article explains how to send messages in Session programmatically, including examples of sending attachments and quotes (replies).

## Quick start

If you're using Bun server runtime and willing to use non-persistant in-memory storage, go ahead with this simple template:

```ts
import { Session, ready } from '@session.js/client'
await ready

const mnemonic = 'love love love love love love love love love love love love love'
const displayName = 'My Session bot'

const session = new Session()
session.setMnemonic(mnemonic, displayName)

await session.sendMessage({
  to: '057aeb66e45660c3bdfb7c62706f6440226af43ec13f3b6f899c1dd4db1b8fce5b',
  text: 'Hello, world!'
})
```

## Getting sent message

Sometimes you want to save the result of sendMessage method to use later for methods such as [deleteMessage](./deleting-messages.md).

```ts
type ReturnTypeOfSendMessage = { 
  messageHash: string, 
  syncMessageHash: string, 
  timestamp: number 
}

const { messageHash, timestamp } = await session.sendMessage({
  to: '057aeb66e45660c3bdfb7c62706f6440226af43ec13f3b6f899c1dd4db1b8fce5b',
  text: 'Hello, world!'
})

console.log('Message hash', messageHash)
// mostly used for polling

console.log('Message timestamp', timestamp)
// used for referencing to this message in other methods
```

!!! Info "See also"
    - [How messages work in Session?](./principles/messages.md)
    - [What is sync message?](./principles/messages.md#control-messages)

## Attachments

Please go to [files and attachments page](./files-and-attachments.md#sending)

## Quotes/replies

Session allows you to quote messages partially to respond to them. Since reply validation would be too complex to perform on each message, everyone agreed that technically you can pass anything in quoted content, though some clients still won't show quoted message unless it really exist in conversation.

```ts
import { Session, ready } from '@session.js/client'
await ready

const session = new Session()
session.setMnemonic('love love love love love love love love love love love love love')

const { timestamp } = await session.sendMessage({
  to: '057aeb66e45660c3bdfb7c62706f6440226af43ec13f3b6f899c1dd4db1b8fce5b',
  text: 'Here is the first message!'
})

await session.sendMessage({
  to: '057aeb66e45660c3bdfb7c62706f6440226af43ec13f3b6f899c1dd4db1b8fce5b',
  text: 'Here is reply!',
  replyToMessage: {
    timestamp: timestamp,
    author: session.getSessionID(),
    text: 'Here is the first message!'
  }
})
```

When quoting message, you also must pass any attachments sent in that message. As you might've guessed, this becomes duplicative, so there is a special utility `getReplyToMessage()` to make our lifes a bit easier:

```ts
import { Session, ready } from '@session.js/client'
await ready

const session = new Session()
session.setMnemonic('love love love love love love love love love love love love love')

session.on('message', message => {
  // Reply to any incoming chat message
  await session.sendMessage({
    to: message.from,
    text: 'Replying to your message',
    replyToMessage: message.getReplyToMessage()
  })
})
```

To read more about events and `message` structure, go to [events](./events.md) page.