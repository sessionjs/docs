# Events

You can listen to a variety of events to trigger parts of your application that are responsible to react on them.

```ts
const session = new Session()
const onMessage = msg => { /**/ }
session.on('message', onMessage)
// alias: session.addEventListener('message', onMessage)

session.off('message', onMessage)
// alias: session.removeEventListener('message', onMessage)
```
## `message`

New message received in DM or closed group. For advanced users: this is only emitted for DataMessage i.e. VisibleMessage i.e. message that was sent by user to the chat. This does not include service messages and other events sent by Session clients. Look at this like on a message bubble.

