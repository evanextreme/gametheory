# Game Theory

![Python package](https://github.com/evanextreme/CSCI455/workflows/Python%20package/badge.svg) ![LaTeX document](https://github.com/evanextreme/CSCI455/workflows/Build%20LaTeX%20document/badge.svg)

## About

Game Theory is a proof of concept piece of ransomware written by Evan Hirsh (@evanextreme)[https://github.com/evanextreme], Andrew Giannone (@atg5232)[https://github.com/atg5232], and Aidan Rubenstein (@ar2126)[https://github.com/ar2126] in Python for our CSCI455 project. It utilizes a phishing email entrypoint to get the user to install a macro, which then installs our windows executable file. The program encrypts the user's hard drive and prompts them to play a game of Snake to unencrypt their files. To avoid exploitation of the raw exe, we significantly handicapped the process, forcing the user to jump through multiple command line hoops to avoid unintentionally encrypting any files.

Credits to [@TokyoEdTech](https://github.com/tokyoedtech) for the implementation of Snake which we modified for usage in this program, and famed youtube channel [Game Theory](https://www.youtube.com/gametheory) for the voice clips and naming inspiration.

## Usage

