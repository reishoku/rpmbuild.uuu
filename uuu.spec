
Name: uuu
Version: 1.5.201
Release: 1%{dist}
Summary: Freescale/NXP I.MX Chip image deploy tools

SourceLicense: BSD
License: BSD
URL: https://github.com/nxp-imx/mfgtools
Source0: https://github.com/nxp-imx/mfgtools/releases/download/uuu_%{version}/uuu_source-uuu_%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: pkgconf
BuildRequires: pkgconf-pkg-config
BuildRequires: pkgconfig(tinyxml2)
BuildRequires: pkgconfig(bzip2)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libssl)
BuildRequires: pkgconfig(libcrypto)
BuildRequires: pkgconfig(libusb)
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(libcap)

# Requires: ''
# Requires:

%description
Freescale/NXP I.MX Chip image deploy tools.

%prep
%setup -q -n uuu-uuu_%{version}


%build
%define _vpath_srcdir .
%define __cmake_builddir redhat-linux-build
%{cmake} \
  -DCMAKE_BUILD_TYPE=Release
%{cmake_build}

%install
%{cmake_install}


%check


%files
%{_bindir}/uuu
%license LICENSE
%doc


%changelog
%autochangelog
