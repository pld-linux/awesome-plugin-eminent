%define	shortname	eminent
Summary:	Quick wmii-style dynamic tagging
Name:		awesome-plugin-%{shortname}
Version:	20101006
Release:	1
License:	GPL v2
Group:		X11/Window Managers/Tools
Source0:	eminent.lua
URL:		https://awesome.naquadah.org/wiki/Eminent
Requires:	awesome >= 3.4
Source1:	README
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Eminent is a small lua library that monkey-patches awful to provide
you with effortless and quick wmii-style dynamic tagging. Unlike
shifty, eminent does not aim to provide a comprehensive tagging
system, but tries to make dynamic tagging as simple as possible. In
fact, besides importing the eminent library, you do not have to change
your rc.lua at all, eminent does all the work for you.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/awesome/lib/%{shortname}
install %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/awesome/lib/%{shortname}
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install %{SOURCE1} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}
%{_datadir}/awesome/lib/%{shortname}
