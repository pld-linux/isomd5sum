Summary:	Utilities for working with md5sum implanted in ISO images
Name:		isomd5sum
Version:	1.0.2
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/System
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	587c37904592ea99f61d8535ad69b7fe
URL:		http://git.fedoraproject.org/
BuildRequires:	popt-devel
BuildRequires:	python-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The isomd5sum package contains utilities for implanting and verifying
an md5sum implanted into an ISO9660 image.

%package devel
Summary:	Development headers and library for using isomd5sum
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
This contains header files and a library for working with the
isomd5sum implanting and checking.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING
%attr(755,root,root) %{_bindir}/implantisomd5
%attr(755,root,root) %{_bindir}/checkisomd5
%{py_sitedir}/pyisomd5sum.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%{_libdir}/*.a
