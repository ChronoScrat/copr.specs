# Contributing

This repository is primarely focused on:
1. Tools I normally use that are not available in Fedora Packages, COPR or another Repository;
2. Personal packages that I use on my workstations

Beyond that, I cannot promise to add another package. However, if a package defined in this repository breakes, I will do my best to fix it.

You can contribute to that by (1) reporting issues and problems and (2) submitting fixes to the SPEC files.

## Using the devcontainer

This repositary has a devcontainer file that allows local testing of RPM builds before they are submitted to COPR - therefore avoiding multiple failed builds.
The problem with this stategy is that `rpkg`, the tool used to build the .srpm files required by `mock` behaves a little bit differently outside of COPR (namely, it doesn't download remote sources).

In order to build packages with remote sources inside of the devcontainer, a possible solution is to use the following flow:

```bash
mkdir /tmp/rpmbuild
rpkg spec --spec <PATH> --outdir /tmp/rpmbuild
spectool -g --directory /tmp/rpmbuild <PATH>
rpkg --path /tmp/rpmbuild srpm --outdir /tmp/rpmbuild
```

If the package has no remote sources (e.g.: backgrounds), you can build the .srpm file by calling:

```bash
mkdir /tmp/rpmbuild
rpkg srpm --spec <PATH> --outdir /tmp/rpmbuild
```

To build the package, we use `mock` (as it is done in COPR):

```bash
mock --spec /tmp/rpmbuild/<SPEC>.spec --sources /tmp/rpmbuild
```

If you wish to test another chroot for mock, pass the chroot's name to the `-r`. All chroots are availabe at `/etc/mock/`.