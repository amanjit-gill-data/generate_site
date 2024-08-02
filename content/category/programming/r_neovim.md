title: How I set up Neovim as an alternative to RStudio.
date: 2024-07-25
modified: 2024-07-26 
status: draft

RStudio is impressive. But Neovim has spoiled me to the extent that I now demand _total_ control over every aspect of my development environment. RStudio offers Vim mode and allows customisation through `.json` configuration files, but the flexibility of Neovim is too attractive to ignore - even if it takes me hours or days to configure it. 

Now I'll describe the steps I took to set up an R development environment in Neovim. I'm on Linux (Ubuntu 22.04 LTS).

### Basic Neovim configuration

I started with my [existing Neovim configuration](https://github.com/amanjit-gill-data/nvim-config-linux), which was set up for Python, LaTeX and Markdown. I'm currently using Neovim version 0.10. 

I don't use a plugin manager. When Neovim starts, it looks through specific directories for plugins. So I simply clone the plugins' git repos into a directory where I know they'll be found by Neovim. I've written notes on this [here](https://github.com/amanjit-gill-data/nvim-config-linux/blob/main/notes/config_notes.md), and I've written a bash script that helps me install, update and remove plugins [here](https://github.com/amanjit-gill-data/nvim-pluggie/blob/main/pluggie.sh).

### R installation 

To ensure my projects are reproducible, I have multiple versions of R on my machine. I'll write a separate post on how I manage this, but for now, the only thing that matters is that the R executable is in the `$PATH`.


### R.nvim plugin 

The [R.nvim plugin](https://github.com/R-nvim/R.nvim) is an amazing plugin that gives you a panelled environment for R development; there's a console for REPL and an object explorer. It allows you a workflow that is somewhat similar to that of RStudio, but it's less resource-intensive and has lots of keybindings for navigation. I don't even know most of the keybindings yet, but the few I do know have made the switch from RStudio worth it. 

I loosely followed the [R.nvim documentation](https://github.com/R-nvim/R.nvim/blob/main/doc/R.nvim.txt)] to set it up. In essence:

1. Install dependencies. R.nvim needs the `nvimcom` package, which it will build the first time R.nvim is loaded. For the build to work, 

```
sudo apt install --no-install-recommends build-essential libcurl4-openssl-dev libssl-dev libxml2-dev
```








