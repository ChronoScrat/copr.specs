%global debug_package %{nil}
%global bgname lakeside

Name:       lakeside-backgrounds
Version:    0.1.0
Release:    1%{?dist}
License:    CC-BY-NC-SA-4.0
Summary:    Lakeside Time of Day backgrounds

URL:        https://github.com/chronoscrat/copr.specs
VCS:        {{{ git_dir_vcs }}}
Source:     {{{ git_dir_pack }}}

BuildArch:      noarch

%description
This package provides the Lakeside Time of Day backgrounds. The dynamic backgrounds updates
according to the time of day. The images are from a project created by Louis Coyle.
Although this package will install the backgrounds in all Desktop Environments, the dynamic
feature is only available in GNOME (and Budgie).

%prep
{{{ git_dir_setup_macro }}}

%install
mkdir -p -m0644 \
    %{buildroot}/%{_datadir}/backgrounds/%{bgname} \
    %{buildroot}%{_datadir}/gnome-background-properties

mv images/Lakeside-*.jxl %{buildroot}/%{_datadir}/backgrounds/%{bgname}
mv lakeside-dynamic.xml %{buildroot}/%{_datadir}/backgrounds/%{bgname}
mv lakeside-gnome.xml %{buildroot}%{_datadir}/gnome-background-properties

%files
%dir %{buildroot}/%{_datadir}/backgrounds/%{bgname}
%{buildroot}/%{_datadir}/backgrounds/%{bgname}/Lakeside-*.jxl
%{buildroot}/%{_datadir}/backgrounds/%{bgname}/lakeside-dynamic.xml
%{buildroot}%{_datadir}/gnome-background-properties/lakeside-gnome.xml

%changelog
%autochangelog