# Bun remote network

This module wraps bun local network but exports two files: for browser enviornment and server environment. Don't worry, modern bundlers such as webpack, rollup and bun should automatically pick up right parts of code for each environment.

If you just want to run everything on one machine (both session instance and making requests to Session network), use [bun local network](./bun-local.md)

## Use with Session.js

Start by installing `@session.js/bun-network-remote` both on client-side and server-side. The package itself only does validation and connects client-side and server-side and all network management is bundled in another dependency `@session.js/bun-network` just like in [local connector](./bun-local.md).

Install it both in browser project and server proxy project:

```
bun add @session.js/bun-network-remote
```

### Client-side (where Session client runs)

```ts
import { Session, ready } from '@session.js/client'
import { BunNetworkRemoteClient } from '@session.js/bun-network-remote'
await ready

new Session({ 
  network: new BunNetworkRemoteClient({ 
    proxy: 'https://my-proxy.example.org:12345/' 
    // this endpoint must be accessible in your environment
    // i.e. if you're building Session client in browser, make sure
    // that my-proxy.example.org has a valid SSL certificate, CORS and SSL settings
  })
})
```

Client-side part will send POST requests to this URL with JSON body.

### Server-side (proxy server)

```ts
// Runtime must be Bun.sh
// Web server can be anything: Express, Fastify, Elysia, Bun's web server, etc...
// Validation is done internally and throws @session.js/error RuntimeValidation errors

import { Elysia } from 'elysia'
import { BunNetworkRemoteServer } from '@session.js/bun-network-remote'
const network = new BunNetworkRemoteServer()

new Elysia()
  .post('/', ({ body }) => network.onRequest(body))
  .listen(12345)
```