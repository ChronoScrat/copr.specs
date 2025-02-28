%global debug_package %{nil}
%global bgname aurora

Name:       aurora-backgrounds
Version:    0.1.0
Release:    1%{?dist}
License:    CC-BY-NC-SA-4.0
Summary:    Lakeside Time of Day backgrounds

URL:        https://github.com/chronoscrat/copr.specs
VCS:        {{{ git_dir_vcs }}}
Source:     {{{ git_dir_pack }}}

BuildArch:      noarch

%description
This package provides the Aurora Time of Day backgrounds. The dynamic backgrounds updates
according to the time of day. I could not find the original owner of the images.
Although this package will install the backgrounds in all Desktop Environments, the dynamic
feature is only available in GNOME (and Budgie).

%prep
{{{ git_dir_setup_macro }}}

%install
mkdir -p -m0755 \
    %{buildroot}%{_datadir}/backgrounds/%{bgname} \
    %{buildroot}%{_datadir}/gnome-background-properties

mv images/*.jxl %{buildroot}%{_datadir}/backgrounds/%{bgname}
mv aurora-dynamic.xml %{buildroot}%{_datadir}/backgrounds/%{bgname}
mv aurora-gnome.xml %{buildroot}%{_datadir}/gnome-background-properties

%files
%attr(0755,root,root) %{_datadir}/backgrounds/%{bgname}/*
%attr(0755,root,root) %{_datadir}/gnome-background-properties/aurora-gnome.xml

%changelog
%autochangelog