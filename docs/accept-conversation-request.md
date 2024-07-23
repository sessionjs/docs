# Accept conversation request

Conversation requests are purely visibility messages for now. Unaccepted conversation does not actually imply any limitations on recipient. Session clients will use that information to hide conversations or move them to main conversations list, but that's it. When you send message to conversation that hasn't been accepted yet, clients will typically assume that you've accepted it, even without calling this method. However, you can send "conversation accepted" message to someone without sending chat message using this method.

```ts
import { Session, ready } from '@session.js/client'
await ready

const session = new Session()
session.setMnemonic('love love love love love love love love love love love love love')

session.acceptConversationRequest({
  from: '057aeb66e45660c3bdfb7c62706f6440226af43ec13f3b6f899c1dd4db1b8fce5b'
})
```

## Events about accepted conversation requests

See [events page](./events.md#messagerequestapproved)