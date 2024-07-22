# Network

You can pick existing network connector or [write your own](#creating-new-network-connector)

## Overview

<table>
<tr>
<td> Network type </td> <td> Supports onion routing </td> <td> Description </td>
</tr>
<tr>
<td><a href="./bun-local.md">Bun (local)</a></td>
<td>❌</td>
<td> This network type is default and simpliest. It is intended to be used in the same process that @session.js/client instances run in. It's ideal if you just want to start and doing everything on server in one project without browser or other parts. </td>
</tr>

<tr>
<td><a href="./bun-remote.md">Bun (remote) for proxies</a></td>
<td>❌</td>
<td> This network might be useful if you're building client in environment that does not allow you sending requests to Session nodes with self-signed certificates. This option is ideal for browser clients, because it handles all network connection on backend proxy that forwards client-side encrypted data to snodes. Check out simple <a href="">browser example here</a>https://github.com/sessionjs/examples. </td>
</tr>

</table>

## Creating new network connector

To implement your own network, write class that implements Network interface from `@session.js/types/network` with onRequest method. It must cover all RequestTypes from `@session.js/types/network/request`. Take a look at this example:

```ts
import type { Network } from '@session.js/types'
import { 
  RequestType, 
  type RequestGetSwarmsBody, 
  type RequestPollBody, 
  type RequestStoreBody, 
  type RequestUploadAttachment 
} from '@session.js/types/network/request'

export class MyNetwork implements Network {
  onRequest(type: RequestType, body: object): Promise<object> {
    switch(type) {
      case RequestType.Store:
        return // typeof ResponseStore

      case RequestType.GetSnodes:
        return // typeof ResponseGetSnodes

      case RequestType.GetSwarms:
        return // typeof ResponseGetSwarms

      case RequestType.Poll:
        return // typeof ResponsePoll

      case RequestType.UploadAttachment:
        return // typeof ResponseUploadAttachment

      case RequestType.DownloadAttachment:
        return // typeof ArrayBuffer

      default:
        throw new Error('Invalid request type')
    }
  }
}
```

This is just an example in documentation, always develop against actual up-to-date RequestTypes enum in types package.