# In-memory storage

Default storage. It's not persistant, so it's ideal for one-time instances.

## Use with Session.js

You don't need to provide it to Session instance constructor, because it is used by default. You can optionally provide it as:

```ts
import { Session } from '@session.js/client'
import { InMemoryStorage } from '@session.js/client/storage'

new Session({ storage: new InMemoryStorage() })
```