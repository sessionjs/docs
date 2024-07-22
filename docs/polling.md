# Polling

Session.js allows you to poll messages on-demand and polling is opt-in, meaning you have to enable it in order to start receiving updates and new messages.

## Quick start

By default, if you don't provide `interval` in options to Poller class constructor, it will poll new messages each 2.5 seconds.

```ts
import { Session, Poller, ready } from '@session.js/client'
import { SnodeNamespaces, type Message } from '@session.js/types'
await ready

const mnemonic = 'love love love love love love love love love love love love love'

const session = new Session()
session.setMnemonic(mnemonic, 'Display name')

const poller = new Poller() // polls every 2.5 seconds
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

You can even attach multiple pollers to instance, for example, to configure interval of polling different namespaces:

```ts
// Poll DMs each 5 seconds
const dmMessagesPoller = new Poller({ interval: 5000, namespaces: new Set([SnodeNamespaces.UserMessages]) })
// Poll user profile each 60 seconds
const profilePoller = new Poller({ interval: 60000, namespaces: new Set([SnodeNamespaces.UserProfile]) })

session.addPoller(dmMessagesPoller)
session.addPoller(profilePoller)

session.on('message', () => { /*...*/ })
session.on('syncDisplayName', (displayName) => {
  console.log('Synced display name', displayName)
})
```

You can use methods `startPolling`, `stopPolling` and `setInterval` on Poller instance to control it. Read more in JSDoc hints in your code editor or IDE.

## Controlled polling on demand

To disable default interval of 2500 ms, pass `interval: null` to Poller constructor

```ts
const poller = new Poller({ interval: null })
session.addPoller(poller)

// ... Some time later ...

const messages = await poller.poll()
console.log('Received messages', messages)
```