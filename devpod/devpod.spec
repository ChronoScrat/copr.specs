%global debug_package %{nil}
%global _missing_build_ids_terminate_build 0

Name:           devpod
# renovate: datasource=github-releases depName=loft-sh/devpod
Version:        v0.6.15
Release:        3%{?dist}
Summary:        Codespaces but open-source, client-only and unopinionated.

License:        MPL-2.0
URL:            https://github.com/loft-sh/%{name}
Source0:        %{url}/releases/download/%{version}/DevPod_linux_x86_64.tar.gz
ExclusiveArch:  x86_64

Requires:       libappindicator-gtk3
Requires:       webkit2gtk4.1

%description
Codespaces but open-source, client-only and unopinionated: Works with any IDE and lets you use any cloud, kubernetes or just localhost docker.

%prep
%autosetup -c

%install
# DevPod does not ship with a `StartupWMClass` key in the desktop file, which causes
# missing icons in GNOME's Dock and KDE's taskbar. Until fixed, we solve this issue here.
# https://github.com/loft-sh/devpod/issues/1776
echo "StartupWMClass=dev-pod-desktop" | tee -a usr/share/applications/DevPod.desktop
install -Dm0755 -t %{buildroot}%{_bindir} usr/bin/dev-pod-desktop
install -Dm0755 -t %{buildroot}%{_bindir} usr/bin/devpod-cli
install -Dm0644 -t %{buildroot}%{_datadir}/applications usr/share/applications/DevPod.desktop
install -Dm0644 -t %{buildroot}%{_datadir}/icons/hicolor/32x32/apps usr/share/icons/hicolor/32x32/apps/dev-pod-desktop.png 
install -Dm0644 -t %{buildroot}%{_datadir}/icons/hicolor/128x128/apps usr/share/icons/hicolor/128x128/apps/dev-pod-desktop.png 
install -Dm0644 -t %{buildroot}%{_datadir}/icons/hicolor/256x256@2/apps usr/share/icons/hicolor/256x256@2/apps/dev-pod-desktop.png 

%files
%{_bindir}/devpod-cli
%{_bindir}/dev-pod-desktop
%{_datadir}/icons/hicolor/32x32/apps/dev-pod-desktop.png
%{_datadir}/icons/hicolor/128x128/apps/dev-pod-desktop.png
%{_datadir}/icons/hicolor/256x256@2/apps/dev-pod-desktop.png
%{_datadir}/applications/DevPod.desktop

%changelog
%autochangelog
