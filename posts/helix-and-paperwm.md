---
title: Helix and PaperWM
date: 17-04-2025
tags:
  - tools
  - development environment
  - helix
  - paperwm
  - editor
  - config
  - window manager
---

## Helix

Approximately 3 months after I posted my VSCod(e/ium) config here, I started using the Helix text editor.
The experience with VSCode was nice, but I wanted more shortcuts. The problem was, shortcuts started to
become more complex. So, I thought maybe I should try a modal editor.

It wasn't the first time that I felt that way. In the past, I tried modal editors like Emacs and (Neo)Vim. I didn't like them, because of
all the config files. I needed a batteries-included editor with sane defaults. It was not a discovery; I already knew Helix existed.
I just didn't know it was exactly what I needed.

Helix is great. My config file is very small. To start using it, just install a language server for your language.
Learning Helix is not hard, and I like the selection-before-verb design choice. I find it more natural, maybe because
my native tongue is Turkish, in which the sentence order is SOV (Subject-Object-Verb); or maybe because
I get to see what object I'm going to manipulate.

Its UI is also very simple, and I like that very much.

I wasn't actually expecting to get used to the modal editing paradigm so quickly. But I have to say,
I'm not a Helix expert at this point. I just use basic editing capabilities. I believe I'll get better over time.
I am not rushing it.

Here is the website: [Helix](https://helix-editor.com/)

And here is a picture of my theme:

![Acme2 Helix theme](/assets/acme2_helix.png)

My config is a gist.

[Gist](https://gist.github.com/abdrd/6cde7efc4c47137537f29078de3ed3ab)

By the way, the crash I mentioned in the config is not happening anymore. I don't know what changed.
The executable is the same. Good news.

## PaperWM

Another tool I like is [PaperWM](https://github.com/paperwm/PaperWM/).

I tried i3 (and sway), and I didn't like them.
It's not their fault. I didn't really understand the difference between a window manager and
a desktop environment. I thought my GNOME Night Mode feature would work on i3.

The problem with i3 is, you need to do everything yourself. If you want to enable automatic
switching between the laptop monitor and the separate monitor in the event that the HDMI cable is unplugged,
you need to create a script for that. If you want to change display settings, you need `xrandr` (or `arandr`). I realized the significance
of desktop environments (especially GNOME). They apparently do a lot of stuff for me.

After giving up on i3 (and other tiling window managers), I searched for a solution that allowed
me to use my precious GNOME, while also allowing me to benefit from the advantages of TWMs.

I came across PaperWM, and I love it. One thing I wish it supported is a proper config file.
If I remember correctly, I found an XML file that resembled something that contained my settings.
It is not a big problem. I saved my settings in a plain text file.

*I remember asking ChatGPT why PaperWM does not have a config file, and it said something about
GNOME creating obstacles because of security reasons.*

PaperWM is great. I think it is even better than i3.

The settings:

```
General
--------

Pos win         : To Right
Def focus       : Center
Show scratch    : Always
Win pos bar     : DIS
Workspace ind   : DIS

Enable tpad     : DIS
UNCHANGED

0
0
0
0
0
0
0

UNCHANGED
UNCHANGED

------------
Workspaces
------------

Def bg      : ENB
UNCHANGED

------------
Keybindings
------------

(Just the custom settings)

Switch to the left window  : Ctrl+Ğ
Switch to the right window : Ctrl+Ü
Toggle fullscreen          : Shift+Ctrl+;
Increment window width     : Shift+Ctrl+!     (Ctrl+Shift+1)
Decrement window width     : Shift+Ctrl+'     (Ctrl+Shift+2)


---------
Winprops
---------

UNCHANGED

---------
Advanced
---------

An         : 0.00
Drift vp   : 2
Drift drag : 2
Top bar    : DIS
Focus icon : DIS
Open win   : DIS
Overv exit : None
Min win    : 5
Dimming    : 160

Previews   : DIS
Scale      : 15
Cl edg win : DIS
Hv edg win : DIS
Hover t.o. : 800
Continual  : DIS

Mini-map   : 0
Win scale  : 15
Max scale  : 95

Max hwidth : 100
Max. tile  : ENB
Mouse top  : ENB

RIGHT
LEFT
DOWN
DIS
DIS
DIS

Hsen       : 2.0
Hfric      : 0.3
Vsen       : 2.0
Vfric      : 0.1
```

Don't mind letters such as 'Ğ' and 'Ü'. Replace them with whatever.


While I was browsing my gists to bring the settings here, I came across the config file for
the GNOME extension `tilingshell`. Yeah, before PaperWM, I used it for a little while, but I don't
remember anything about it.


---

See you.

