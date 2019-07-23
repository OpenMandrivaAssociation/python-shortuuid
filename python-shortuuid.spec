%define	module	shortuuid
%define	rel	1

%if %mdkversion < 201100
%else
%endif

Summary:	Generator library for concise, unambiguous, and URL-safe UUIDs

Name:		python-%{module}
Version:	0.5.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/80/d7/2bfc9332e68d3e15ea97b9b1588b3899ad565120253d3fd71c8f7f13b4fe/shortuuid-0.5.0.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://github.com/stochastic-technologies/shortuuid/
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
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean

%files
%{py_puresitedir}/%{module}*




