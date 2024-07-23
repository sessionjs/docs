# Reactions

Session allows you to react on a message with any existing emoji. Technically, you can react with any number of unicode characters, but some clients will not display a reaction if it's not a single valid emoji.

## Add reaction

```ts
import { Session, ready } from '@session.js/client'
await ready

session.on('message', message => {
  session.addReaction({
    messageTimestamp: message.timestamp,
    messageAuthor: message.from,
    emoji: '👽'
  })
})
```

## Remove reaction

```ts
session.removeReaction({
  messageTimestamp: message.timestamp,
  messageAuthor: message.from,
  emoji: '👽'
})
```

## Events about added/removed reaction

See [events page](./events.md#reactionadded)