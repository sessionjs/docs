# Events

You can listen to a variety of events to trigger parts of your application that are responsible to react on them.

```ts
const session = new Session()
session.setMnemonic('love love love love love love love love love love love love love')
const onMessage = msg => { /**/ }
session.on('message', onMessage)
// alias: session.addEventListener('message', onMessage)

session.off('message', onMessage)
// alias: session.removeEventListener('message', onMessage)
```
## `message`

New message received in DM or closed group. For advanced users: this is only emitted for DataMessage i.e. VisibleMessage i.e. message that was sent by user to the chat. This does not include service messages and other events sent by Session clients. Look at this like on a message bubble.

```ts
type PrivateMessage = {
  type: 'private'
}
type ClosedGroupMessage = {
  type: 'group'
  groupId: string
}
type Message = (PrivateMessage | ClosedGroupMessage) & {
  id: string
  from: string
  text?: string
  attachments: MessageAttachment[]
  replyToMessage?: {
    timestamp: number
    author: string
    text?: string
    attachments?: QuotedAttachment[]
  }
  timestamp: number
  getEnvelope: () => EnvelopePlus
  getContent: () => SignalService.Content
  getReplyToMessage: () => Message['replyToMessage']
}

session.on('message', (message: Message) => {
  console.log(
    'From:', msg.from,
    'Is from closed group:', msg.type === 'group',
    'Group id:', msg.type === 'group' ? msg.groupId : 'Not group',
    'Text:', msg.text ?? 'No text',
  )
})
```

To reply to this message, you can use getReplyToMessage() method:

```ts
session.sendMessage({ 
  to: message.from,
  text: 'reply!',
  replyToMessage: message.getReplyToMessage() 
})
```

## `syncMessage`

This event is intended to let your instance know that the message was sent from your Session ID to another Session ID. This is useful when a person uses many devices and this event lets your client know that they sent message from another device.

**This event will be triggered on the instance that used sendMessage**

```ts
export type SyncMessage = Omit<Message, 'from'> & { to: string }
// interface is the same as above, but instead of `from` field we have `to` 
// which indicates Session ID that the user sent message to

session.on('syncMessage', (message: SyncMessage) => {
  console.log(
    'To:', msg.to,
    'Is to closed group:', msg.type === 'group',
    'Group id:', msg.type === 'group' ? msg.groupId : 'Not group',
    'Text:', msg.text ?? 'No text',
  )
})
```

## `syncDisplayName`

**This event will be triggered on the instance that used [setDisplayName](./profile.md#display-name)**

One of instances changed this Session ID assosiated profile display name.

```ts
session.on('syncDisplayName', newDisplayName => {
  console.log('My new display name is', newDisplayName)
})
```

## `syncAvatar`

**This event will be triggered on the instance that used [setAvatar](./profile.md#avatar)**

One of instances changed this Session ID assosiated profile display name.

```ts
session.on('syncDisplayName', newAvatar => {
  const newAvatarFile = await session.getFile(newAvatar) // => File
  console.log('My new avatar is', newAvatarFile)
})
```

## `messageDeleted`

**This event will be triggered on the instance that used [deleteMessage](./deleting-messages.md)**

Message has been deleted.

```ts
type MessageDeleted = {
  /** Timestamp of deleted message sent in that message constructor. Lookup message by timestamp in saved messages */
  timestamp: number,
  /** Sender of message that deleted it */
  from: string
}

session.on('messageDeleted', (messageDeleted: MessageDeleted) => {
  console.log(
    'Message with timestamp', messageDeleted.timestamp,
    'sent by', messageDeleted.from,
    'was deleted'
  )
})
```

## `messageRead`

Message has been read.

```ts
type MessageReadEvent = {
  /** Timestamp of read message sent in this message constructor. Lookup message by timestamp among locally saved messages */
  timestamp: number,
  /** Session ID of conversation where message was read */
  conversation: string
}

session.on('messageRead', (messageRead: MessageReadEvent) => {
  console.log(
    'Message with timestamp', messageRead.timestamp,
    'was read in conversation', messageRead.conversation
  )
})
```

## `messageTypingIndicator`

Typing indicator appeared or disappeared.

```ts
type MessageTypingIndicator = {
  /** If true, you should countdown from 20 and then treat it like recipient stopped typing */
  isTyping: boolean
  /** Session ID of conversation where typing indicator appeared or disappeared */
  conversation: string
}

session.on('messageTypingIndicator', (typingIndicator: MessageTypingIndicator) => {
  console.log(
    'Typing indicator', typingIndicator.isTyping ? 'appeared' : 'disappeared',
    'in conversation', typingIndicator.conversation
  )
})
```

## `screenshotTaken`

**This event will be triggered on the instance that used [notifyScreenshotTaken](./screenshot-taken-notification.md)**

"Screenshot taken" message was sent in conversation.

```ts
type ScreenshotTakenNotification = {
  /** Timestamp when screenshot was taken */
  timestamp: number
  /** Session ID of conversation where notification appeared */
  conversation: string
}

session.on('screenshotTaken', (notification: ScreenshotTakenNotification) => {
  console.log(
    '"Screenshot taken" notification appeared at', notification.timestamp, 
    'in conversation', notification.conversation
  )
})
```

## `mediaSaved`

**This event will be triggered on the instance that used [notifyMediaSaved](./media-saved-notification.md)**

"Attachment downloaded" message was sent in conversation.

```ts
type MediaSavedNotification = {
  /** Message's timestamp which has attachment that was downloaded */
  timestamp: number,
  /** Session ID of conversation where notification appeared */
  conversation: string
}

session.on('mediaSaved', (notification: MediaSavedNotification) => {
  console.log(
    '"Attachment downloaded" notification appeared about',
    'downloading attachment in message with timestamp', 
    notification.timestamp, 
    'in conversation', notification.conversation
  )
})
```

## `messageRequestApproved`

"Conversation request accepted" message was sent in conversation.

```ts
type Profile = {
  /** Name, displayed instead of your Session ID. Acts like nickname. All unicode characters are accepted except for `ￒ` (0xffd2) which is reserved by Session for mentions. Max length: 64 characters */
  displayName: string
  /** Image, displayed near display name in Session clients. Acts like profile picture. */
  avatar?: {
    /** URL to avatar, uploaded to Session file server */
    url: string
    /** 32 bytes key used for avatar encryption */
    key: Uint8Array
  }
}
type MessageRequestResponse = {
  profile: Profile,
  conversation: string
}

session.on('messageRequestApproved', (message: MessageRequestResponse) => {
  console.log(
    'Your conversation request was accepted by',
    message.conversation,
    message.profile.displayName
  )
})
```

## `call`

Call message was sent in conversation. Calls are not supported by Session.js yet.

```ts
type Call = {
  uuid: string
  type: SignalService.CallMessage.Type
  from: string
}

session.on('call', (call: Call) => {
  console.log(
    'You have received call-related message',
    call.from,
    call.type
  )
})
```

## `reactionAdded`

**This event will be triggered on the instance that used [addReaction](./reactions.md)**

Reaction was added on a message.

```ts
type ReactionMessage = {
  messageTimestamp: number
  messageAuthor: string
  reactionFrom: string
  /** Emoji as string. Any unicode character(s) may be in this field, length is practically unlimited, validation is not performed by the @session.js/client library. You should probably only display the reaction, if it's a single valid emoji */
  emoji: string
}

session.on('reactionAdded', (reaction: ReactionMessage) => {
  console.log(
    'New reaction added on message with timestamp',
    reaction.messageTimestamp,
    'sent by', reaction.messageAuthor,
    '—', reaction.reactionFrom,
    'reacted with', reaction.emoji
  )
})
```

## `reactionRemoved`

**This event will be triggered on the instance that used [removeReaction](./reactions.md)**

Reaction was added on a message.

```ts
type ReactionMessage = {
  messageTimestamp: number
  messageAuthor: string
  reactionFrom: string
  /** Emoji as string. Any unicode character(s) may be in this field, length is practically unlimited, validation is not performed by the @session.js/client library. You should probably only display the reaction, if it's a single valid emoji */
  emoji: string
}

session.on('reactionRemoved', (reaction: ReactionMessage) => {
  console.log(
    'Reaction removed from message with timestamp',
    reaction.messageTimestamp,
    'sent by', reaction.messageAuthor,
    '—', reaction.reactionFrom,
    'reaction was', reaction.emoji
  )
})
```