# Files in Session

This article explains how attachments and files work in Session messenger.

## How to send an attachment with message in Session?

Session limits size of your attachments to 10 MB and uses special file server hosted by Oxen foundation that is used by all clients to upload and download encrypted files. Attachments always should have digest, key and size values that are checked by Session clients upon receiving and decrypting file. Files can have content-type, width, height, name, caption optional fields that Session clients will use to display information about file.

[@session.js/client](https://www.npmjs.com/package/@session.js/client) will handle that encryption logic for you, wrapping it to just attaching File interface to sendMessage method's options and getFile method.

## What happens when you click to "download media" button in Session?

Though there is no practical and respectful to user's privacy way for Session file server to know when you download media from conversation, your Session client will send "Media saved by you" message in conversation letting your recipient know you've downloaded attachment from their message. This is done locally upon interaction with download button.

[@session.js/client](https://www.npmjs.com/package/@session.js/client) allows you to download attachments without sending this message and, if you're building your own client, send these kind of messages to conversation with simple methods.