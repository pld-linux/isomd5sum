Summary:	Utilities for working with md5sum implanted in ISO images
Summary(pl.UTF-8):	Narzędzia do obsługi sum MD5 wszczepionych w obrazy ISO
Name:		isomd5sum
Version:	1.0.2
Release:	3
Epoch:		1
License:	GPL v2+
Group:		Applications/System
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	587c37904592ea99f61d8535ad69b7fe
Patch0:		%{name}-smallfixes.patch
URL:		http://git.fedoraproject.org/
BuildRequires:	popt-devel
BuildRequires:	python-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The isomd5sum package contains utilities for implanting and verifying
an md5sum implanted into an ISO9660 image.

%description -l pl.UTF-8
Ten pakiet zawiera narzędzia do wszczepiania i sprawdzania sum MD5
wszczepionych w obrazy ISO9660.

%package devel
Summary:	Development headers and library for using isomd5sum
Summary(pl.UTF-8):	Pliki nagłówkowe i biblioteka do używania isomd5sum
Group:		Development/Libraries
# doesn't require base

%description devel
This contains header files and a library for working with the
isomd5sum implanting and checking.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe i bibliotekę do wszczepiania i
sprawdzania sum MD5 obrazów ISO.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/checkisomd5
%attr(755,root,root) %{_bindir}/implantisomd5
%attr(755,root,root) %{py_sitedir}/pyisomd5sum.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/lib*isomd5.h
%{_libdir}/lib*isomd5.a
