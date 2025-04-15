%global debug_package %{nil}
%global _missing_build_ids_terminate_build 0

Name:           oh-my-posh
# renovate: datasource=github-releases depName=JanDeDobbeleer/oh-my-posh
Version:        v25.13.0
Release:        1%{?dist}
Summary:        The most customisable and low-latency cross platform/shell prompt renderer 
License:        MIT

URL:            https://github.com/JanDeDobbeleer/oh-my-posh
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

%global trimmed_version %(echo %{version} | tr -d "v")

BuildRequires: golang
BuildRequires: git

%description
Oh My Posh is a highly customisable and extensible cross shell prompt theme engine.

%prep
%autosetup -n oh-my-posh-%{trimmed_version}

%build
cd ./src/
go build \
    -trimpath \
    -buildmode=pie \
    -modcacherw \
    -ldflags "-linkmode=external -X main.version=%{version}"

%install
install -Dm 0755 src/src %{buildroot}%{_bindir}/oh-my-posh
install -Dm 0644 COPYING %{buildroot}%{_datadir}/licenses/oh-my-posh/COPYING

%files
%{_bindir}/oh-my-posh
%license %{_datadir}/licenses/oh-my-posh/COPYING

%changelog
%autochangelog