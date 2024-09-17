title: How I keep my R projects reproducible.
date: 2024-08-02
modified: 2024-09-17

Unless you are very lucky, replacing your version of R with the most recent one, or continually upgrading your packages, will eventually break your projects. I am apparently not very lucky, because this has happened to me - my university upgraded its packages while I was mid-assignment, and my code suddenly stopped working. 

My own practices are not perfect. There are tools to help keep our projects reproducible that I haven't tried yet. But my point isn't that we should all be experts; my point is that we should _care_ about reproducibility and try harder to avoid the footguns that break our projects.

To that end, here is the fairly simple setup I've adopted for my Linux system, centred on two strategies:

1. Instead of maintaining a single installation of R by continually replacing it with the latest version, install multiple versions side by side. Use a specific version of R for each project, and stick to it. 

2. For each R version, you have a _site_ library and a _user_ library. You'll normally install new packages into the user library. But if you later upgrade those packages, you might break projects that relied on the older versions. So, instead of putting all your packages, for all your projects, into the one user library, give each project its own little library. This way, upgrading the packages you're using for one project won't break your other projects. 

### Multiple versions of R 

Posit offers downloads of many versions of R. I've taken the following steps from [here](https://docs.posit.co/resources/install-r.html#specify-r-version). Follow them for every version of R you want to install. 

1. Download the correct deb package for your operating system. For example, if you want version 4.4.0 for Ubuntu 22.04:

        :::text
        export R_VERSION=4.4.0
        curl -O https://cdn.rstudio.com/r/ubuntu-2204/pkgs/r-${R_VERSION}_1_amd64.deb
        

2. Install the downloaded package. All of your R installations will be isolated from one another - on Ubuntu, they will install into `/opt/R/4.4.0/`, `/opt/R/4.4.1`, etc.

        :::text
        sudo apt install ./r-${R_VERSION}_1_amd64.deb

3. Verify the installation by executing the binary. If you installed version 4.4.0, the binary will be located at `/opt/R/4.4.0/bin/R`.

        :::text
        /opt/R/${R_VERSION}/bin/R --version

4. If you like, create symlinks for this installation. Take care with older projects if you've decided to overwrite an existing `R` symlink to make it point to your newly installed version.

        :::text
        sudo ln -s /opt/R/${R_VERSION}/bin/R /usr/local/bin/R
        sudo ln -s /opt/R/${R_VERSION}/bin/Rscript /usr/local/bin/Rscript

### Project-specific libraries

I use `renv` to manage packages within each project. This is itself an R package. I install and use it according to the documentation [here](https://rstudio.github.io/renv/).

#### Install renv 

1. Launch R. If you have multiple versions installed, take care that you've launched the correct one. 

2. Install `renv` as you would any other package. 

        :::text 
        install.packages("renv")

If this is the first package you're installing, R might warn you that the _site_ library isn't writeable, then ask for your permission to install into the _user_ library instead - if this happens, say 'yes'.

#### Initialise renv in a project

The following is a brief, non-exhaustive, overview of how to use `renv` to track the packages used in a project. 

1. Launch the version of R you're using for this project. Ensure the current working directory is set to the root of your project - you can do this at the command line by navigating to the project root before launching R, or with `setwd()` at the R console. 

2. Initialise `renv`. This will create a `renv` directory, and a few other files, inside the project. Note: Unlike other packages, you don't need to call `library("renv")` in order to access `renv` functions.

        :::text
        renv::init()

3. One of the newly created files is `renv.lock`, a JSON file listing all the packages used in your project, and their versions. As you work on your project, you'll need to keep `renv.lock` updated by taking regular "snapshots" to capture new package installations, removals or updates.

        :::text 
        renv::snapshot()

At the command line, if you launch R from the project root, it should recognise and activate the project for you. Alternatively, use `setwd()` within R to set the current working directory to the project root, then call `renv::load()`. 

#### Reproduce the project elsewhere

If the project is shared with others or cloned to another machine, include the `renv` files - and then `renv` can be used to rebuild the project library at the new machine:

1. Ensure the required version of R is installed (look inside `renv.lock` to see which version is needed).

2. Launch R. Ensure that the current working directory is set to the root of the cloned project. 

3. Use `renv` to restore the project library. There's no need to have already installed `renv` - it will _bootstrap_ itself i.e. it will be installed into the project library along with the other project packages. 

        :::text 
        renv::restore() 

### Next steps 

As mentioned earlier, this isn't a perfect setup. But it's a start, and I intend to implement better practices as I learn more.

