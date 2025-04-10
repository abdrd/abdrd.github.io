---
title: Minimal VSCode/VSCodium Config
description: Minimal VSCode configuration/settings
tags:
  - editor
  - vscode
  - vscodium
  - config
  - development-environment
date: 10-11-2024
---

I created a simple configuration for VSCode/VSCodium. This configuration hides all the things that annoy me. It hides the title bar, status bar and any other bar. It hides the mini map. It removes the margin of line numbers. It removes file tabs.

I navigate my projects with keyboard shortcuts. For example, if I want to jump to a variable or a function, I press `Ctrl+Shift+O`. If I want to jump to the end of a line I press `fn+right`. If I want to navigate between the words of a camelCase identifier, I press `alt+left` (or `+right`). I can press `Ctrl+W` to close a window. I can use `Ctrl+Tab` to switch between windows or I can press `Ctrl+P` to select a file. I can ...

There is also this extension that I am very happy with. It is called `DanielBreiner.go-to-relative`. It allows you to jump an arbitrary amount of lines. Combining it with relative line mode is great. I can press `Ctrl+G` and then type any integer to jump to the line `currentLine + (input)`. For example, if you are on line 11, and you press `Ctrl+G` and then type 10, you go to line 21 (If you type -10, then you go to line 1).


This config also changes the background color to a beige (?) color which I think is the best theme (Similar to the default theme of the Acme editor by Rob Pike). I recommend using this config with a light theme such as Visual Studio Light.

The font is hardcoded in the config. You can of course change it to whatever you like.

![Io programming language's garbage collector](/assets/minimal-vscodium.png)
<small>Garbage collector of the <a href="https://iolanguage.org/index.html">Io</a> programming language</small>

Here is the gist link:

[https://gist.github.com/abdrd/2f13dc5c91a8732e95eb3af3d5255cfd](https://gist.github.com/abdrd/2f13dc5c91a8732e95eb3af3d5255cfd)
