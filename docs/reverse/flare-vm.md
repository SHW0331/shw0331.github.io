---
layout: default
title: flare-vm
parent: reverse
nav_order: 5
---

# install choco
- Set-ExecutionPolicy Bypass -Scope Process -Force
- [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
- choco -v

# install boxstarter
- choco install boxstarter
- Install-BoxstarterPackage -PackageName https://aka.ms/flarevm
