%define	module	shortuuid
%define name	python-%{module}
%define version 0.2
%define	rel	1

%if %mdkversion < 201100
%define release %mkrel %{rel}
%else
%define	release %{rel}
%endif

Summary:	Generator library for concise, unambiguous, and URL-safe UUIDs
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/s/%{module}/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://github.com/stochastic-technologies/shortuuid/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	python-setuptools

%description
shortuuid is a simple python library that generates concise,
unambiguous, URL-safe UUIDs.

Often, one needs to use non-sequential IDs in places where users will
see them, but the IDs must be as concise and easy to use as
possible. shortuuid solves this problem by generating uuids using
Python's built-in uuid module and then translating them to base57
using lowercase and uppercase letters and digits, and removing
similar-looking characters such as l, 1, I, O and 0.

%prep
%setup -q -n %{module}-%{version}

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%py_sitedir/%{module}*



%changelog
* Mon Jun 25 2012 Lev Givon <lev@mandriva.org> 0.2-1
+ Revision: 806809
- imported package python-shortuuid

