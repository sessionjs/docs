# SOGS

SOGS (Session Open Group Server) is a type of Session communication channel, a community of users (with no limit on number of participants). It's not hosted on Session nodes, in contrast to Session groups, instead it is hosted on SOGS owner's server, but it is onion routed and end-to-end encrypted. If allows flexible management of rights and can be used for public announcements channels and chats.

Looking for a way to host SOGS yourself? Check out [bunsogs](https://github.com/vityaSchel/bunsogs/) from author of Session.js

## Interacting with SOGS

Use @session.js/sogs package with utilities for SOGS and @session.js/client to interact with SOGS.

### Example: Get info about room

To make request to SOGS you must initialize Session instance. This library handles authorization and encryption in connection to SOGS for you.

```
bun add @session.js/client
```

```ts
import { Session, ready } from '@session.js/client'
await ready

const mnemonic = 'love love love love love love love love love love love love love'
const displayName = 'My Session bot'

const session = new Session()
session.setMnemonic(mnemonic, displayName)

// Example SOGS link: https://sogs.hloth.dev/sessionjs?public_key=8948f2d9046a40e7dbc0a4fd7c29d8a4fe97df1fa69e64f0ab6fc317afb9c945
const sogsUrl = 'https://sogs.hloth.dev'
const sogsRoom = 'sessionjs'
const sogsPublicKey = '8948f2d9046a40e7dbc0a4fd7c29d8a4fe97df1fa69e64f0ab6fc317afb9c945'

await session.sendSogsRequest({
  host: sogsUrl,
  serverPk: sogsPublicKey,
  endpoint: '/room/' + sogsRoom,
  method: 'GET',
  blind: false
})
/*
->
{
  active_users: 1,
  active_users_cutoff: 604800,
  admins: [ "15b8543369273587555a8bd935156a76bbf9752f1dac4a8d998c2d6ddc712eb921" ],
  created: 1723208687.896,
  description: "Channel about Session.js framework",
  image_id: 3,
  info_updates: 5,
  message_sequence: 34,
  moderators: [],
  name: "Session.js announcements",
  token: "sessionjs",
  pinned_messages: [],
  read: true,
  write: false,
  upload: false,
  moderator: false,
  admin: false,
}
*/
```

### Example: Get messages

To decrypt message, you can use `decryptSogsMessageData` method from @session.js/sogs which handles decryption for you

```
bun add @session.js/client @session.js/sogs
```

```ts
import { Session, ready } from '@session.js/client'
import { decryptSogsMessageData } from '@session.js/sogs'
await ready

const mnemonic = 'love love love love love love love love love love love love love'
const displayName = 'My Session bot'

const session = new Session()
session.setMnemonic(mnemonic, displayName)

// Example SOGS link: https://sogs.hloth.dev/sessionjs?public_key=8948f2d9046a40e7dbc0a4fd7c29d8a4fe97df1fa69e64f0ab6fc317afb9c945
const sogsUrl = 'https://sogs.hloth.dev'
const sogsRoom = 'sessionjs'
const sogsPublicKey = '8948f2d9046a40e7dbc0a4fd7c29d8a4fe97df1fa69e64f0ab6fc317afb9c945'

const messages = await session.sendSogsRequest({
  host: sogsUrl,
  serverPk: sogsPublicKey,
  endpoint: '/room/' + sogsRoom + '/messages/recent',
  method: 'GET',
  blind: false
})
const latestMessage = messages[messages.length - 1]
if(!latestMessage) {
  throw new Error('This room has no messages')
}
const message = decryptSogsMessageData(latestMessage.data)
console.log(message)
// -> (this is example)
/*
SignalService.Content {
  dataMessage: DataMessage {
    attachments: [],
    preview: [],
    body: "Hello!",
    timestamp: Long {
      low: 675798965,
      high: 404,
      unsigned: true
      <...>
    }
    profile: LokiProfile {
      displayName: "My Bot",
      profilePicture: "",
      <...>
    },
    <...>
  }
  <...>
}
*/
```

### Example: Send messages

❌ DO NOT use this to send spam ❌

🔪 SERIOUSLY 🔪🔪🔪🔪

```ts
import { Session, ready } from '@session.js/client'
import { decryptSogsMessageData } from '@session.js/sogs'
import { VisibleMessage } from '@session.js/schema'
await ready

const mnemonic = 'love love love love love love love love love love love love love'
const displayName = 'My Session bot'

const session = new Session()
session.setMnemonic(mnemonic, displayName)

// Example SOGS link: https://sogs.hloth.dev/sessionjs?public_key=8948f2d9046a40e7dbc0a4fd7c29d8a4fe97df1fa69e64f0ab6fc317afb9c945
const sogsUrl = 'https://sogs.hloth.dev'
const sogsRoom = 'sessionjs'
const sogsPublicKey = '8948f2d9046a40e7dbc0a4fd7c29d8a4fe97df1fa69e64f0ab6fc317afb9c945'

// Use blinding to hide your Session ID from others
// Blinding uses ID unique to each SOGS so that no one knows your Session ID
// (at least in theory, see https://github.com/VityaSchel/blinded-id-converter-website)
const blind = true

const msg = new VisibleMessage({
  body: reply,
  profile: session.getMyProfile(),
  timestamp: session.getNowWithNetworkOffset(),
  expirationType: null,
  expireTimer: null,
  identifier: crypto.randomUUID(),
  attachments: [],
  preview: [],
  quote: undefined
})

const { data, signature } = session.encodeSogsMessage({
  serverPk: sogsPublicKey,
  message: msg
  blind
})
const requestBody = JSON.stringify({ data, signature })
const messages = await session.sendSogsRequest({
  host: sogsUrl,
  serverPk: sogsPublicKey,
  endpoint: '/room/' + sogsRoom + '/message',
  method: 'POST',
  body: requestBody
  blind
})
// -> (this is example)
/*
{
  id: 9,
  session_id: "15f0240ef446562d2afad24a4cf24eaa1fee45655dc461de01309a5bcd5e24e943",
  posted: 1735849081.0190141,
  seqno: 9,
  data: "ChoKBkhlbGxvITin8avFwjKqBggKBk15IEJvdIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
  signature: "cIk52ceTRCMcfNi71V3FsphPPf4w9/jOZSUBAnZSgsCWnJMLx+xxXaL0OY6+LXwTin6GilFw71rZG1ax6czrAQ==",
  reactions: {},
}
*/
```