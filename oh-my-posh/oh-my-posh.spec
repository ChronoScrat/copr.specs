%global debug_package %{nil}
%global _missing_build_ids_terminate_build 0

Name:           oh-my-posh
# renovate: datasource=github-releases depName=JanDeDobbeleer/oh-my-posh
Version:        v26.2.0
Release:        1%{?dist}
Summary:        The most customisable and low-latency cross platform/shell prompt renderer 
License:        MIT

URL:            https://github.com/JanDeDobbeleer/oh-my-posh
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

%global trimmed_version %(echo %{version} | tr -d "v")

BuildRequires: golang
BuildRequires: git

Requires:      %{name}-cli >= %{version}-%{release}

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
mkdir -p %{buildroot}%{_datadir}/%{name}/themes/
install -Dm 0755 src/src %{buildroot}%{_bindir}/oh-my-posh
install -Dm 0644 COPYING %{buildroot}%{_datadir}/licenses/oh-my-posh/COPYING
install -Dm 0644 themes/* %{buildroot}%{_datadir}/%{name}/themes/


%package cli
Summary:        The binary for oh-my-posh
Recommends:     %{name}-themes

%description cli
The binary executable for oh-my-posh. Part of the oh-my-posh metapackage.

%files cli
%{_bindir}/oh-my-posh
%license %{_datadir}/licenses/oh-my-posh/COPYING


%package themes
Summary:        Themes for oh-my-posh
BuildArch:      noarch
Requires:       %{name}-cli = %{version}-%{release}

%description themes
Themes bundled with oh-my-posh. Part of the oh-my-posh metapackage.

%files themes
%{_datadir}/%{name}/themes/

# Empty metapackage
%files

%changelog
%autochangelog
