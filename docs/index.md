Session.js is JavaScript library for programmatic usage of [Session messenger by OXEN](https://getsession.org). Supports server and browser environment with built-in proxy network module. Shipped with TypeScript definitions. Tested with bun:test. Written with blazingly fast [Bun](https://bun.sh), a modern runtime for JavaScript and alternative to Node.js. **This package cannot be used with Node.js, it uses a better runtime instead of it**. It can also be used with most bundlers that support modern syntax.

Session.js allows you to create:

- Highly optimized Session bots (hundreds of bots in a single app)
- Custom Session clients (web-based and native with JS backend)
- Automation tools for Session

## Features

- On-demand polling — you decide when to get new messages and whether instance should poll them (and poll settings like frequency) or work just for sending
- Per-instance storage and network settings — you can attach persistant storage to instance or use in-memory storage for throwaway one-time instances
- Session.js can be used in browser, keeping private keys on client-side and doing network requests on server-side. See this in action with [my full-featured Session Web client](https://github.com/VityaSchel/session-web)!

## Getting started

Jump to [getting started](./getting-started.md) page to start using Session.js!

## Roadmap
- [X] Messages
  - [X] Automatic snodes fetching
  - [X] Automatic swarms selection
  - [ ] Manual snode/swarm control
  - [X] Data retrieving from swarms
  - [X] Messages polling
  - [X] Messages types
    - [X] Regular chat message
      - [X] Text
      - [X] Attachments
        - [X] Images
        - [X] Files
        - [X] Voice messages
        - [X] Quotes
        - [ ] Web links previews
    - [X] Service messages
      - [X] Sync message
      - [X] Configuration message
        - Uses legacy constructor for now
      - [X] Read message (ReadReceipt)
      - [X] Typing message
      - [X] Message request response
      - [X] Screenshot / media saved (DataExtraction)
      - [X] Delete message (Unsend)
      - [X] Call message
        - Just event to display placeholder warning about unsupported feature
  - [X] Reactions
  - [ ] Closed chats
  - [ ] Open groups (SOGS)
  - [ ] Expirable messages
- [ ] Calls
- [ ] Messages editing (SOGS)
- [X] Profile editing
  - [X] Display name
  - [X] Avatar
  - [X] Syncing between devices
- [X] ONS resolving
- [ ] Get rid of ByteBuffer and other lazy dependencies

</details>

## License

All code in Session.js (including any submodules) was written by Viktor Shchelochkov aka hloth and licensed under [MIT license](https://github.com/sessionjs/client/blob/main/LICENSE.md)

## Funding

You can donate here: [hloth.dev/donate](https://hloth.dev/donate)