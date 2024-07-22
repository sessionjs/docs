# Bun local network

Default network that uses Bun's capabilities to fetch Session servers. It is intended to be used in the same process in the same environment as @session.js/client.

If you're looking for network that works on proxy server (to host instance part on client side and do requests to Session servers via server side), use [bun remote network](./bun-remote.md). One such case is browser Session client, because browsers do not support connecting to Session servers.

## Use with Session.js

Simply **do not provide any network to `network` option in Session class constructor** and this will be the default. You can optionally provide it as:

```ts
import { Session, ready } from '@session.js/client'
import { BunNetwork } from '@session.js/bun-network'
await ready

new Session({ network: new BunNetwork() })
```