# Deleting messages

Deleting messages in Session means deleting message from swarm (when recipient hasn't polled it yet so they won't be able to ever see it) and broadcasting UnsendMessage which instructs Session clients to remove polled message locally.

```ts
import { Session, ready } from '@session.js/client'
await ready

const session = new Session()
session.setMnemonic('love love love love love love love love love love love love love')

const { timestamp, messageHash } = await session.sendMessage({
  to: '057aeb66e45660c3bdfb7c62706f6440226af43ec13f3b6f899c1dd4db1b8fce5b',
  text: 'Hello world!'
})

// ... Some time later...

await session.deleteMessage({
  to: '057aeb66e45660c3bdfb7c62706f6440226af43ec13f3b6f899c1dd4db1b8fce5b',
  timestamp: timestamp,
  hash: messageHash
})
```

You can delete many messages at once in a batch request to save traffic and performance

```ts
await session.deleteMessages([
  {
    to: '057aeb66e45660c3bdfb7c62706f6440226af43ec13f3b6f899c1dd4db1b8fce5b',
    timestamp: timestamp1,
    hash: messageHash1
  },
  {
    to: '057aeb66e45660c3bdfb7c62706f6440226af43ec13f3b6f899c1dd4db1b8fce5b',
    timestamp: timestamp2,
    hash: messageHash2
  },
  {
    to: '057aeb66e45660c3bdfb7c62706f6440226af43ec13f3b6f899c1dd4db1b8fce5b',
    timestamp: timestamp3,
    hash: messageHash3
  },
])
```

!!! Info "See also"

    - [How do you delete messages in Session?](./principles/messages.md#how-do-you-delete-messages-in-session)

## Events about deleted messages

See [events page](./events.md#messagedeleted)