# Media saved notification

Session allows you to send "media saved" notification. Clients send this message upon user interaction.

!!! Info "See also"

    - [What happens when you click to "download media" button in Session?](./principles/files.md#what-happens-when-you-click-to-download-media-button-in-session)

```ts
import { Session, ready } from '@session.js/client'
await ready

const session = new Session()
session.setMnemonic('love love love love love love love love love love love love love')

let messageTimestamp: number
session.on('message', message => {
  messageTimestamp = message.timestamp
})

// ... Some time later ...

await session.notifyMediaSaved({
  conversation: '057aeb66e45660c3bdfb7c62706f6440226af43ec13f3b6f899c1dd4db1b8fce5b',
  savedMessageTimestamp: messageTimestamp
})
```

## Events about taken notifications

See [events page](./events.md#screenshottaken)