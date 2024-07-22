# Messages in Session

This article explains core principles behind Session's messages.

## How does messaging works in Session with its decentralization?

Just like PGP emails back in the day, Session and similar messengers use end-to-end encryption. Session uses your private key (decoded from mnemonic) to encrypt data of your message to base64 string which is sent to swarms. That way, swarms hosted by other people in network never receive your private key.

Swarm is a storage server for messages that is specifically designed to store encrypted messages. They are tied to pools of Session IDs, so your inbox might be on one swarm, while your recipient might be on another swarm. There are obviously many swarms available for a specific Session ID, you should choose random one to provide security. Swarms sync messages between each other, so you shouldn't store your message to all of them, just pick one of available. So before sending a message you must find a swarm that serves the specified Session ID.

To find swarm that serves for a specific Session ID, you should use a dedicated method `get_swarm` in request to Session Service Node, which returns list of available swarms. But even before that, you should get a list of service nodes that work right now and can return you a list of available swarms for specified Session ID. To get list of service nodes in Session network, you must pick one of Seed Nodes which is official Oxen foundation servers that serve as directory list of servers in decentralized network. 

There are three seed nodes hosted by Oxen foundation (developers of Session):
- seed1.getsession.org
- seed2.getsession.org
- seed3.getsession.org

You can pick any of them to request service nodes list and preferrably add mechanism that switches from seed1 to seed2 etc when one is unavailable.

All requests to swarms, service nodes, and seed nodes are made using JSON RPC format. All of them have their own self-signed certificate. For seed nodes, you should implement "certificate pinning", i.e. hardcode seeds servers certificates data directly in your code for maximum security. For service nodes and swarms, you will receive their certificates data in list requests.

[@session.js/client](https://github.com/sessionjs/client) handles all that logic for you. You can simply pass Session ID and message and it will send the message for you. Additionally, there is getSwarm method that does everything described above but returns swarm's ip address and port for your custom logic.

## How does storing messages on Swarms work?

As said previously, you have to find swarm for specific Session ID. Do not mistake it with your own swarm: when you want to send message to recipient, you should find and use recipient's swarm. Since Session is built on top of Signal protocol, it uses Signal's protobuf schema and Signal's messages classes to serialize message data and encrypt it locally using private key. Then it uses `store` method to save message in swarm storage.

[@session.js/client](https://github.com/sessionjs/client) allows you to create any number of instances in single JavaScript file that can send as many messages as you want with a simple yet flexible API.

## How does messages polling work?

Similar to messages storing, to poll messages Session client would first find working service node using seed nodes, then ask for swarm for that specific Session ID (pubkey) and make frequent JSON RPC requests with `retrieve` method to get messages. To keep track of new messages, you'll typically use last hashes parameter. While messages in Session do have a unique identifier that is unique across all clients — hash, it looks like it either had been added too late or borrowed from Signal, because many interactions that refer to specific message (such as reply to previously sent message, messages deletion etc) use timestamp instead of hash. You'll mostly use messages hashes only for polling-related logic.

[@session.js/client](https://github.com/sessionjs/client) wraps polling into a simple interface, at the same time allowing you to customize polling as you want with all encryption and low-level logic encapsulated and processed by the library.

## How do you delete messages in Session?

Since Session clients mostly strive to keep everything local, Session has come up with a smart decision to create "unsend" messages which are [control messages](#control-messages) that instruct Session clients to remove specific message from local database and stop showing it to that client's user. Session clients usually also send request with `delete` method to swarms to delete the message in their storage, in case recipient hasn't polled the message yet.

## How long do messages are stored in Session?

Swarms usually keep messages for 14 days, but some messages can be sent with expiring config.

## Control messages

All events in Session are called Messages, specifically they are sent in VisibleMessage class which, when deserialized, has one of these properties:
- DataMessage — chat bubble message. Reaction added/removed events are also sent as DataMessage, with reaction property and empty string body.
- DataMessage with syncTarget set (sent to your own swarm) — used by Session clients to sync between logged devices, basically tells that we have sent message to someone specified in syncTarget field
- UnsendMessage — delete message
- SharedConfigMessage — syncs profile including display name and avatar with all clients. Earlier, Session clients used ConfigurationMessage but now they'll display that one of your devices runs legacy outdated version if they receive ConfigurationMessage. Parameters are generated using libsession-util library written in c/c++
- ReadReceiptMessage — recipient seen your message
- TypingIndicatorMessage — recipient has started or stopped typing
- ConversationRequestMessage — response to yours (or someone else's) conversation request
- DataExtractionMessage — recipient saved attachment in your conversation or took screenshot