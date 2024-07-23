# Typing indicator

Session.js allows you to show/hide typing indicator in 1-1 conversations. You should only call this method if user explicitly agreed to share typing state with recipient(s).

```ts
import { Session, ready } from '@session.js/client'
await ready

const mnemonic = 'love love love love love love love love love love love love love'
const session = new Session()
session.setMnemonic(mnemonic)

await session.showTypingIndicator({
  conversation: '057aeb66e45660c3bdfb7c62706f6440226af43ec13f3b6f899c1dd4db1b8fce5b'
})
```

Typing indicators last for 20 seconds, after that clients will hide it until the next showTypingIndicator call.

Hide typing indicator early:

```ts
await session.hideTypingIndicator({
  conversation: '057aeb66e45660c3bdfb7c62706f6440226af43ec13f3b6f899c1dd4db1b8fce5b'
})
```

## Events about typing indicators

See [events page](./events.md#messagetypingindicator)