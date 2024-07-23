# Persistant file-based key=value storage with fs

Simple persistant storage that stores everything in memory and periodically syncs it with locally stored file in key=value format.

## Install

```
bun add @session.js/file-keyval-storage
```

## Use with Session.js

This type of storage only works in server environments, because it uses fs module to access user's file system. `filePath` is optional and defaults to ./storage.db

```ts
import { Session } from '@session.js/client'
import { FileKeyvalStorage } from '@session.js/file-keyval-storage'

new Session({
  storage: new FileKeyvalStorage({ 
    filePath: 'some-file-path.db' 
  })
})
```