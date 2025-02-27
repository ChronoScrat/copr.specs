%global bgname lakeside-timed

Name:       lakeside-timed-backgrounds
Version:    0.1.0
Release:    %autorelease
License:    Apache-2.0
Summary:    Timed Lakeside Backgrounds

URL:        https://chronoscrat.github.io
VCS:        {{{ git_dir_vcs }}}
Source:     {{{ git_dir_pack }}}

%description
This package contains the Lakeside timed backgrounds

%prep
{{{ git_dir_setup_macro }}}

%install
%dir %{buildroot}/%{_datadir}/background/%{bgname}
install -Dm644 ./images/Lakeside-*.jxl %{buildroot}/%{_datadir}/backgrounds/%{bgname}/Lakeside-*.jxl

%files
%dir %{buildroot}/%{_datadir}/background/%{bgname}
%{buildroot}/%{_datadir}/backgrounds/%{bgname}/Lakeside-*.jxl

%changelog
%autochangelog