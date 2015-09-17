# ABE\_h #
ABE\_h stands for Archive, Backup and Exchange of data in a human readable form. It's little more then a proof-of-concept for
archiving/sending data that has to be humanly usable even in the event of major network and/or application failures.

It's the central part of a system (which would include files, meta-data, etc.) that should enable a usable and realistic
access to critical data using only the tools commonly available on any computer by a large number of users:
- a file archiver (for compressed file extraction)
- a text editor
- a pdf viewer

## What does it look like ?
Using json for illustration, given the following record of a fictional book-sharing site:
```json
{ "id": "33540dd9-093b-4428-b9fb-f2233262a0bf", "p_i": "1146dc4e-533e-4e53-95c6-bb2775407fe6", "b_a": "Lawrence Snyder", "b_n": "mi sit", "isbn": "968163323-7", "ps": 993, "ls": 232, "p_s": 141, "p_n": "Alan Black", "p_e": "ablack9@woothemes.com", "p_j": "VP Product Management" }
```

This would be a human readable form of it (uninteresting data may be omitted):

> **mi sit**,  *Lawrence Snyder* (isbn:968163323-7), 993 pages
> - Record ID : 33540dd9-093b-4428-b9fb-f2233262a0bf
> - Shared by Alan Black (VP Product Management)
>   - *ablack9@woothemes.com*
>   - 141 friends
> - **232** likes


## How is it stored ?
Output is a simple markdown file, with the markdown formatted output and the original code in code blocks.

Code or text can be filtered out, which means PDF text outputs of the data can be generated with ease.
