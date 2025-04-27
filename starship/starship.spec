%global debug_package %{nil}
%global _missing_build_ids_terminate_build 0


Name:           starship
# renovate: datasource=github-releases depName=starship/starship
Version:        v1.23.0
Release:        1%{?dist}
Summary:        The minimal, blazing-fast, and infinitely customizable prompt for any shell!
License:        ISC

URL:            https://github.com/starship/%{name}
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

%global trimmed_version %(echo %{version} | tr -d "v")

BuildRequires: rust
BuildRequires: cargo
BuildRequires: cmake
BuildRequires: git

%description
The minimal, blazing-fast, and infinitely customizable prompt for any shell!

%prep
%autosetup -n %{name}-%{trimmed_version}

%build
cargo build \
    --release \
    --locked

%install
install -Dm 0755 target/release/starship %{buildroot}%{_bindir}/starship
install -Dm 0644 LICENSE %{buildroot}%{_datadir}/licenses/%{name}/LICENSE

%files
%{_bindir}/starship
%license %{_datadir}/licenses/%{name}/LICENSE

%changelog
%autochangelog