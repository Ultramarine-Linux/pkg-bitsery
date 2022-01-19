%undefine _disable_source_fetch
%define debug_package %{nil}
Name:           bitsery
Version:        5.2.2
Release:        1%{?dist}
Summary:        Header only C++ binary serialization library

License:        MIT
URL:            https://github.com/fraillt/bitsery/
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cmake gcc g++
#Requires:       

Provides:      pkgconfig(bitsery)

%description
Header only C++ binary serialization library. It is designed around the networking requirements for real-time data delivery, especially for games.

%prep
%autosetup -n %{name}-%{version}


%build
%cmake
%cmake_build


%install
rm -rf $RPM_BUILD_ROOT
%cmake_install


%files
%license LICENSE
%doc doc/
%{_libdir}/cmake/bitsery/

%{_includedir}/bitsery/

%changelog
* Wed Jan 19 2022 Cappy Ishihara <cappy@cappuchino.xyz>
- 
