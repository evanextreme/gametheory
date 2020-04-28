# Game Theory

![Python package](https://github.com/evanextreme/CSCI455/workflows/Python%20package/badge.svg) ![LaTeX document](https://github.com/evanextreme/CSCI455/workflows/Build%20LaTeX%20document/badge.svg)

## About

Game Theory is a proof of concept piece of ransomware written by Evan Hirsh ([@evanextreme](https://github.com/evanextreme)), Andrew Giannone ([@atg5232](https://github.com/atg5232)), and Aidan Rubenstein ([@ar2126](https://github.com/ar2126)) in Python for our CSCI455 project. It utilizes a phishing email entrypoint to get the user to install a macro, which then installs our windows executable file. The program encrypts the user's hard drive and prompts them to play a game of Snake to unencrypt their files. To avoid exploitation of the raw exe, we significantly handicapped the process, forcing the user to jump through multiple command line hoops to avoid unintentionally encrypting any files.

Credits to [@TokyoEdTech](https://github.com/tokyoedtech) for the implementation of Snake which we modified for usage in this program, and famed youtube channel [Game Theory](https://www.youtube.com/user/MatthewPatrick13) for the voice clips and naming inspiration.

## Usage

To test this software, first ensure you are on a test machine that does not have any important data. Then, download the document that would be attached to a phishing email [at this link](https://github.com/evanextreme/CSCI455/blob/master/phish/important_document.docm). Once this document is opened, follow the (malicious!) directions in the document that instruct you to click the ribbon notification to "Enable Editing" and then "Enable Content." This document was (safely) tested among some of the developer's peers and less technical friends and was consistently rated as highly convincing. The document will then download the most current version of the malware from an external server using an obfuscated VBA macro and will automatically execute it and begin the process of encrypting the machine's files.

## Notes on Phase 5

The most recent versions of Windows Defender on Windows 10 detect and warn the user about the macro in our document, which is unfortunate. The phase 2 obfuscated version still remains undetected by 49 / 61 modern antiviruses as tested by Virustotal.com and will remain undetected on older versions of Windows 10 that have not updated their security definitions (this is a non-trivial amount of users). Much work has been done to try to circumvent this detection, but nothing the group has tried has been fruitful so far.
