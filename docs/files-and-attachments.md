# Files and attachments

This article explains how to send and download attachments with Session.js

!!! Info "See also"

    - [How files work in Session?](./principles/files.md)

## Sending

Attachments are passed as [File](https://developer.mozilla.org/en-US/docs/Web/API/File) interface, available both in browser and Bun. You must specify file name and content type in constructor.

You're fully responsible for validation of files content, type, name and file size. Keep in mind that Sesison file server will throw error if you're trying to upload files more than 10 MB.

### Sending local file as attachment

This only works in server environment, because browsers won't let you access user file system, at least not as simple to be shown in this guide.

```ts
import path from 'path'
import { Session, ready } from '@session.js/client'
await ready

const filename = '/Users/kitty/Desktop/image.jpg'
const buffer = await fs.readFile(filename)
const file = new File([buffer], path.basename(filename), { type: 'image/jpeg' })

const session = new Session()
session.setMnemonic('love love love love love love love love love love love love love')

await session.sendMessage({
  to: '057aeb66e45660c3bdfb7c62706f6440226af43ec13f3b6f899c1dd4db1b8fce5b',
  text: 'Image from file',
  attachments: [file]
})
```

### Sending file downloaded from URL

This will most likely work both in browser and server environments, unless domain that you're fetching has no [CORS headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) allowing your host to fetch the resourse.

```ts
import { Session, ready } from '@session.js/client'
await ready

const imageData = await fetch('https://picsum.photos/100/100').then(res => res.arrayBuffer())
const file = new File([imageData], 'image.jpeg', { type: 'image/jpeg' })

const session = new Session()
session.setMnemonic('love love love love love love love love love love love love love')

await session.sendMessage({
  to: '057aeb66e45660c3bdfb7c62706f6440226af43ec13f3b6f899c1dd4db1b8fce5b',
  text: 'Image from URL',
  attachments: [file]
})
```

### Sending file selected on the web page

This will only work in browser environment, because server has no [DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model) interfaces, such as `window` or `document`.

```ts
import { Session, ready } from '@session.js/client'
await ready

// This will try to find <input type="file"></input> on page and read selected files from it
const file = document.querySelector('input[type=file]').files[0]

const session = new Session()
session.setMnemonic('love love love love love love love love love love love love love')

await session.sendMessage({
  to: '057aeb66e45660c3bdfb7c62706f6440226af43ec13f3b6f899c1dd4db1b8fce5b',
  text: 'Image from browser',
  attachments: [file]
})
```

## Voice messages

Voice messages are a special kind of attachments. They are usually sent as mp3 files with special flag set in message constructor. Session.js allows you to pass voice message to message in a special field:

```ts
import { Session, ready } from '@session.js/client'
await ready

const filename = '/Users/kitty/Desktop/voice-message.mp3'
const buffer = await fs.readFile(filename)
const file = new File([buffer], path.basename(filename), { type: 'audio/mpeg' })

const session = new Session()
session.setMnemonic('love love love love love love love love love love love love love')

await session.sendMessage({
  to: '057aeb66e45660c3bdfb7c62706f6440226af43ec13f3b6f899c1dd4db1b8fce5b',
  voiceMessage: file
})
```

## Receiving

When you receive file in message, it will have url pointer and key to decrypt. Session.js provides a useful utility getFile which downloads that file from url pointer using provided network, decrypts and validates, returning you a [File](https://developer.mozilla.org/en-US/docs/Web/API/File) with name and content type.

```ts
session.on('message', message => {
  message.attachments.forEach(attachment => {
    const file = await session.getFile(attachment)
    console.log('Attachment name', file.name)
    console.log('Attachment size', file.size)
    console.log('Attachment type', file.type)
  })
})
```