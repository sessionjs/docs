# Mark message as read

Session.js allows you to mark message as read in 1-1 conversations. You should only call this method if user explicitly agreed to share read indicators with recipient(s).

```ts
import { Session, ready } from '@session.js/client'
await ready

const session = new Session()
session.setMnemonic('love love love love love love love love love love love love love')

session.on('message', message => {
  session.markMessagesAsRead({
    from: message.from,
    messagesTimestamps: [message.timestamp],
    readAt: Date.now() // optional
  })
})
```

You can mark multiple messages as read at once

```ts
session.on('message', message => {
  session.markMessagesAsRead({
    from: message.from,
    messagesTimestamps: [message1.timestamp, message2.timestamp, message3.timestamp],
    // we haven't provided readAt, so it will fallback to current time
  })
})
```

## Events about read messages

See [events page](./events.md#messageread)