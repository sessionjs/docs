# Profile customization

Session allows you to set display name and avatar for your Session ID. This article explains how to customize your profile using Session.js

!!! Info "See also"
    - [How Session profiles work?](./principles/users.md#how-session-profiles-work)

!!! warning

    Session.js currently does not support syncing profile between devices, you will likely run into problems if you try to use up-to-date official Session clients and Session.js at the same time. This is because they've switched from ConfigurationMessage to SharedDataConfig message which is generated in libsession-util code which is written in C/C++. Help is needed to resolve this issue, from someone who knows both C and JS

## Display name

Initially you can set display name in setMnemonic method which takes display name as optional second argument.

```ts
import { Session, ready } from '@session.js/client'
await ready

const mnemonic = 'love love love love love love love love love love love love love'
const displayName = 'My Session bot'

const session = new Session()
session.setMnemonic(mnemonic, displayName)
```

or you can change it later:

```ts
await session.setDisplayName('My new Session bot name')
```

## Avatar

Just like regular attachments, avatars size is limited to 10 mb. It is recommended to use widely-supported image formats, such as JPEG and PNG to avoid compatability issues with other clients. Session.js does not perform any validation.

```ts
const filename = '/Users/kitty/Desktop/avatar.jpeg'
const file = await fs.readFile(filename)
const avatar: ArrayBuffer = file.buffer

await session.setAvatar(avatar)
```