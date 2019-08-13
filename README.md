# BitDust DevOps

Collection of tools, scripts and helpers for maintaining BitDust infrastracture and software development.
Also here you will learn how to start your own private BitDust network from scratch.

BitDust project development flow is based on two independent GIT repositories:

* [Development repository](https://github.com/bitdust-io/devel)
* [Stable repository](https://github.com/bitdust-io/public)


When changes in the development repo are considered to be "good enough" files are manually copied by one of the developers to the stable repo fork on his local machine and new commit must be created to start a new Pull Request.

This process can be considered as a new "Release" - BitDust software do not have any versioning of the releases because it is not required. After Pull Request is merged - release is done.

Every BitDust node periodically "check & fetch" fresh commits from the GIT repository where it was cloned from.
This way BitDust software on your local machine automatically "updates itself" and stays in sync with the "Stable" repository. Every BitDust contributor is responsible to deliver high-standard, super reliable and well-tested source code changes every time Pull Request is merged.

As a user of BitDust software you can disabled automatic updates at any moment in the program settings and always run only the code you cloned first time when you get into BitDust network.

You can also fork BitDust "stable" repo and clone locally your fork to quickly check and run main Python code. Just like any other github project you forked, your fork will be fully independent from the main repo - you will have to sync manually with main repo if you wish to stay on same version. This will work the best for all of the developers and also for those who wish to learn BitDust or particiapte in testing. Remember to always check and stay in sync with main network and refresh your code from [Stable repository](https://github.com/bitdust-io/public).

If you stay out of sync with other users your data is at risk! Remember to always check & pull your BitDust software sources and stay in sync with the main network by updating your code from [Stable repository](https://github.com/bitdust-io/public).

For non-developers and all other people willing to join BitDust network in a common way we maintain [BitDust Desktop](https://github.com/bitdust-io/desktop/releases) Application installer.

You go directly to [bitdust.io web site](https://bitdust.io) and download installer file - we provide link directly from [GitHub repo]([BitDust desktop](https://github.com/bitdust-io/desktop/). Application uses Electron Framework for GUI and will automatically clone from BitDust Stable repo for the first time you run application and keep your local sources in sync with the master branch.

As a user of BitDust software you can disabled automatic updates at any moment in the program settings and always run only the code you cloned first time when you get into BitDust network.

Below is a step-by-step guide for developers to deliver changes from the "Development" repository into the "Stable" repository.



## Prepare environment

To be able to run a new BitDust release you must fork and clone both repositories already.
Basically those actions you need to do only one time and just keep your repositories up-to-date with the main branches.

Here we assume your fork will be "origin" and main repository will be added as "upstream":

    # fork and clone development repo
    git clone git@github.com:<your GitHub username here>/devel.git bitdust.devel
    cd bitdust.devel
    git remote add upstream https://github.com/bitdust-io/devel.git
    cd ..

    # fork and clone stable repo
    git clone git@github.com:<your GitHub username here>/public.git bitdust
    cd bitdust
    git remote add upstream https://github.com/bitdust-io/public.git
    cd ..

    # clone devops repo
    git clone https://github.com/bitdust-io/devops.git bitdust.devops



## Runbook

To start a release you need to prepare source code changes inside your forked & cloned "Stable" repo.
You do not do any changes to the source code manually but use two helper scripts built for you.
Those scripts will take source code from "Development" repo you already cloned locally and prepare everything for you to start Pull Request in the "Stable" repo and publish latest source code.

To start you open a terminal window, change to `bitdust.devops` repository and run First script:

    git clone https://github.com/bitdust-io/devops.git bitdust.devops
    cd bitdust.devops/
    ./ci/release_prepare


This will prepare all files to be commited into "Stable" repository.
All modified/added/removed files will be displayed in your terminal output. That script is doing a bunch of things:

* copy files from "devel" to "stable" repo
* disable DEBUG mode in all Python files
* compare all files in both repositories
* updates `HISTORY.txt` file in "devel" repo


Now you must manually edit and prepare `CHANGELOG.txt` file inside your BitDust development repo. All you need to do is to provide a short info about your changes with a date and your name.

After running `release_prepare` you should see in your terminal console output a list of most recent commits.
You can simply Copy & Past those lines from your console to the top of `CHANGELOG.txt` file.
Look at `HISTORY.TXT` file in the root of development repo and use commit messages to build info in `CHANGELOG.txt` file.

    head -20 ../bitdust.devel/HISTORY.txt
    nano ../bitdust.devel/CHANGELOG.txt


Now you need to open another terminal window, go to the "Stable" repository and use Git command `git add ...` / `git rm ...` to confirm and prepare changes to be released.

First mark all modified files in git repo to be commited in the new release:

    cd ./bitdust
    git add -u .


Add all other new files to git manually - this is important to check here to not miss any files created recently in "devel" repo:

    git status
    git add <some new file>


If some files or folders were removed from "devel" repo - do not forget to also remove them from the "Stable" repo and mark those changes to be commited:

    git rm <some old file>


We are almost done!

Switch back your terminal to `bitdust.devops` repository and execute manually Second script:

    cd ../bitdust.devops/
    ./ci/release_start


That script will push all prepared changes to your forked repositories.

All you need now to do start the release is to create new [Pull Request](https://github.com/bitdust-io/public/pulls) towards "stable" repository via GitHub web site.

Make sure Travis build is green and people review your changes and everyone agree.

One of the developers must click Merge button finally and ...

Congratulations, YOU ARE LIVE!

Do not forget to update your fork right away to stay in sync:

    git pull upstream master
    git push origin master



#### Install/update telegraf configuration on monitoring machine

BitDust developers maintain few machines to "seed" the Main network - you can find those hosts in [networks.json](https://github.com/bitdust-io/public/blob/master/networks.json).

Those machines we monitor via Grafana dashboard we built and here is how we provision it:


Prepare environment
-------------------

```shell
    $ make venv
    $ cd ansible
    $ ansible-playbook telegraf.yml -i inventory/test -K --limit monitoring -e "application_name=monitoring"
```



#### Install/update telegraf configuration on Identity servers

This comman we use to update monitoring config on all Identity server machines:

```shell
    $ make venv
    $ cd ansible
    $ ansible-playbook telegraf.yml -i inventory/test -K --limit id_servers
```



#### Install/update telegraf configuration on suppliers

This comman we use to update monitoring config on all suppliers nodes we started to provide a storage:

```shell
    $ make venv
    $ cd ansible
    $ ansible-playbook telegraf.yml -i inventory/test -K --limit suppliers
```
