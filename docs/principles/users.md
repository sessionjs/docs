# Users in Session

This article explains core principles behind Session's accounts.

## How accounts in Session messenger work?

In Session, there are no "accounts" in terms of persistant entities. Instead, there are inboxes where you receive your messages and can assosiate display name, avatar and ONS (link to Session ID) with. Technically, no one including you own your inbox. You can manage your inbox when you have access to it, and you have access when you have mnemonic (which is essentially a private key that is used to decrypt messages in that inbox).

## What is Session ID?

Session ID is your inbox address which is [x25519 32 bytes public key aka Curve25519](https://en.wikipedia.org/wiki/Curve25519). It is always prepended with `05`, which makes it 66 characters long (32 bytes -> 64 characters + `05` prefix).

Using @session.js/mnemonic and @session.js/keypair you can quickly generate random seeds, convert them to keypairs used by Session, get x25519 public key from it and encode to mnemonic that can be used in Session client.

```ts
import { generateSeedHex, getKeypairFromSeed } from '@session.js/keypair'
import { encode } from '@session.js/mnemonic'

const seedHex = generateSeedHex() // generate random 16 bytes seed that should be kept secure
const keypair = getKeypairFromSeed(seedHex) // derive public and private x25519 and ed25519 keys
const sessionID = keypair.x25519.publicKey // Session ID is x25519 public key
const mnemonic = encode(seedHex) // mnemonic is 13 words for accessing your Session
```

## How to register in Session?

Since there are no accounts, you can't register. Instead, your device generates a random private key (which can be displayed as encoded mnemonic), which is then converted to public key (which can be displayed as hex which is your Session ID). Public key allow another person to encrypt message, private key allows you to decrypt message. Obviously, you share public key (Session ID) so that other people can write you messages and never share private key (so that no one can read your messages except you).

[@session.js/client](https://github.com/sessionjs/client) handles all encryption logic for you.

## How to delete account in Session?

Since there are no accounts, you can't delete it. Moreover, as stated above, you can't even own it. You just hope that theoretically no one will ever guess your private key (or mnemonic) to read your messages and write messages from your inbox.

However, you can delete all data that is assosiated with your inbox. Read [how messages work in Session](./messages.md)

## What is ONS?

As said above, a person must have your public key (Session ID) to send you a message. Session IDs are hard to remember, as they're always 66 characters long and consist only of hex characters (a-f, 0-9). There is [Session Vanity ID generator](https://session-id.pages.dev/) which can get you somewhere about first 5 desired characters, but the rest 61 characters are still random. As you might have guessed, this generator just iterates over random private keys and derives public keys (Session ID) until a match is found, and, if we were able to generate all 66 characters, that would mean we can compromise any known Session ID's private key.

Usernames are a popular way to access each other's chats without remembering whole address. They are unique and simply act as a link to full address. Session has its own usernames system called Oxen Name System (ONS) which allows you to buy a mapping to your Session ID (plus a few other integrated lokinet projects) for 7 OXEN which at time of writing this article is about 1$. Payments are processed inside of Oxen blockchain, which makes it secure. ONS deserves whole another article, so for now just keep in mind that you can buy username in Session which simply acts like a link to your Session ID.

[@session.js/ons](https://github.com/sessionjs/ons) handles resolving ONS->Session ID encryption logic for you, so you just have to provide ONS and you'll receive Session ID.
Alternatively, there is [https://ons.sessionbots.directory/](https://ons.sessionbots.directory/) which is a registry of ONS names with local client-side quick search among all registered ONS names in Session network.

## How Session profiles work?

As previously discussed, there are no accounts in Session, so you can't get profile by account ID like in Telegram or any other centralized messenger or social media. Moreover, for privacy, Session clients shouldn't show profile display name and avatar unless user accepts conversation request or explicitly agrees to share profile with recipient. Instead of fetching it everytime, profiles in Session are saved locally in database for contacts.

Profile data comes with each visible chat message and with conversation request accepted message. So each time Session client sends a message to another user or accepts a request to talk, this message also contains your display name and avatar — that's how they're updated in local databases of other clients.

To be clear: **there is no way to get avatar or display name of specific Session ID unless they send that data inside of encrypted chat message bubble.** Until Session client received display name and avatar in either of these messages, it should display just Session ID.