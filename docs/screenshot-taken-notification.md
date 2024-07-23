# Screenshot taken notification

Session allows you to send "screenshot taken" notification. Usually clients will use platform's capabilities to track when screenshot was taken and call this method. On some platforms this is impossible.

```ts
import { Session, ready } from '@session.js/client'
await ready

const session = new Session()
session.setMnemonic('love love love love love love love love love love love love love')

await session.notifyScreenshotTaken({
  conversation: '057aeb66e45660c3bdfb7c62706f6440226af43ec13f3b6f899c1dd4db1b8fce5b'
})
```

## Events about taken notifications

See [events page](./events.md#screenshottaken)