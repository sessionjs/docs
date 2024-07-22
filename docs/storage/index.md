# Storage

You can use any existing storage adapter or [write your own](#creating-new-storage-adapter)

## Overview

<table>
<tr>
<td> Storage type </td> <td> Description </td>
</tr>
<tr>
<td><a href="./in-memory">In-memory</a></td>
<td><b>Default</b> storage that stores data in memory, that is reset after this process exits or tab is closed. Ideal for short living one-time bots or testing. It is not persistant.</td>
</tr>

<tr>
<td><a href="./file-keyval">Persistant file-based key=value storage with `fs`</a></td>
<td>Simple storage that stores everything in memory and periodically syncs it with locally stored file in key=value format. `filePath` is optional and defaults to `./storage.db` </td>
</tr>

</table>

## Creating new storage adapter

To implement your own storage, write class that implements Storage interface from `@session.js/types/storage`. Take a look at this example with in-memory storage

```ts
import type { Storage } from '@session.js/types'

export class MyInMemoryStorage implements Storage {
  storage: Map<string, string> = new Map()

  get(key: string) {
    return this.storage.get(key) ?? null
  }

  set(key: string, value: string) {
    this.storage.set(key, value)
  }

  delete(key: string) {
    this.storage.delete(key)
  }

  has(key: string) {
    return this.storage.has(key)
  }
}
```