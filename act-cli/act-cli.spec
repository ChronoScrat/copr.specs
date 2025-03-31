%global debug_package %{nil}
%global _missing_build_ids_terminate_build 0

Name:           act-cli
# renovate: datasource=github-releases depName=nektos/act
Version:        v0.2.75
Release:        1%{?dist}
Summary:        Run your GitHub Actions locally
License:        MIT

URL:            https://github.com/nektos/%{name}
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  git
BuildRequires:  golang
BuildRequires:  make

Requires:       (podman or moby or docker or docker-ce or docker-ce-cli or docker-ee)

%description
Run your GitHub Actions locally

%prep
%autosetup -c

%build
ver=$(echo %{version} | tr -d "v")
mv act-${ver}/* .
go build \
    -trimpath \
    -buildmode=pie \
    -mod=readonly \
    -modcacherw \
    -ldflags "-linkmode=external -X main.version=%{version}"

%install
install -Dm 0755 act %{buildroot}%{_bindir}/act-cli
install -Dm 0644 LICENSE %{buildroot}%{_datadir}/licenses/%{name}/LICENSE

%files
%{_bindir}/act-cli
%license %{_datadir}/licenses/%{name}/LICENSE

%changelog
%autochangelog
