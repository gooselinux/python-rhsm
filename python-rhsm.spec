# If on Fedora 12 or RHEL 5 or earlier, we need to define these:
%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif


Name: python-rhsm
Version: 0.95.14
Release: 1%{?dist}

Summary: A Python library to communicate with a Red Hat Unified Entitlement Platform
Group: Development/Libraries
License: GPLv2
# How to create the source tarball:
#
# git clone git://git.fedorahosted.org/git/candlepin.git/
# cd client/python-rhsm
# tito build --tag python-rhsm-%{name}-%{version}-%{release} --tgz
Source0: %{name}-%{version}.tar.gz
URL: http://fedorahosted.org/candlepin
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires: m2crypto
Requires: python-simplejson
Requires: python-iniparse
BuildArch: noarch

BuildRequires: python2-devel
BuildRequires: python-setuptools


%description 
A small library for communicating with the REST interface of a Red Hat Unified
Entitlement Platform. This interface is used for the management of system
entitlements, certificates, and access to content.

%prep
%setup -q -n python-rhsm-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README

%dir %{python_sitelib}/rhsm

%{python_sitelib}/rhsm/*
%{python_sitelib}/rhsm-*.egg-info

%changelog


* Thu May 05 2011 Adrian Likins <alikins@redhat.com> 0.95.14-1
- add resolves line to spec (alikins@redhat.com)

* Thu May 05 2011 Adrian Likins <alikins@redhat.com> 0.95.7-1
- Resolves: #702403
- 700601: Don't set the Accept-Language if we don't have a valid locale
  (alikins@redhat.com)

* Tue Apr 05 2011 Bryan Kearney <bkearney@redhat.com> 0.95.6-1
- Resolves: #691788
- 691788: Fix bad check for missing order info. (dgoodwin@redhat.com)

* Fri Mar 25 2011 Bryan Kearney <bkearney@redhat.com> 0.95.5-1
- Resolves: #683550
- 683550: fix parsing empty cert extensions (jbowes@redhat.com)

* Tue Mar 08 2011 Devan Goodwin <dgoodwin@redhat.com> 0.95.4-1
- Add support for content tagging. (dgoodwin@redhat.com)

* Fri Feb 04 2011 Devan Goodwin <dgoodwin@redhat.com> 0.95.3-1
- 674078: send a full iso 8601 timestamp for activeOn pools query
  (jbowes@repl.ca)

* Tue Feb 01 2011 Devan Goodwin <dgoodwin@redhat.com> 0.95.2-1
- Add content metadata expire to certificate class. (dgoodwin@redhat.com)

* Fri Jan 28 2011 Chris Duryee (beav) <cduryee@redhat.com>
- Add new extensions to order (jbowes@redhat.com)
- remove shebang from certificate.py for rpmlint (jbowes@redhat.com)
- Adding activateMachine to connection api. (jharris@redhat.com)
- 668814: break out 404 and 500s into a different error (cduryee@redhat.com)
- Initialized to use tito. (jbowes@redhat.com)
- bump version (jbowes@redhat.com)

* Wed Jan 12 2011 jesus m. rodriguez <jesusr@redhat.com> 0.94.13-1
- 667829: handle proxy config options being absent from rhsm.conf (alikins@redhat.com)

* Fri Jan 07 2011 Devan Goodwin <dgoodwin@redhat.com> 0.94.12-1
- Related: #668006
- Remove a missed translation. (dgoodwin@redhat.com)
- Fix logger warning messages. (dgoodwin@redhat.com)


* Tue Dec 21 2010 Devan Goodwin <dgoodwin@redhat.com> 0.94.10-1
- Related: #661863
- Add certificate parsing library. (dgoodwin@redhat.com)
- Fix build on F12/RHEL5 and earlier. (dgoodwin@redhat.com)

* Fri Dec 17 2010 jesus m. rodriguez <jesusr@redhat.com> 0.94.9-1
- add comment on how to generate source tarball (jesusr@redhat.com)

* Fri Dec 17 2010 Devan Goodwin <dgoodwin@redhat.com> 0.94.8-1
- Adding GPLv2 license file. (dgoodwin@redhat.com)

* Fri Dec 17 2010 Devan Goodwin <dgoodwin@redhat.com> 0.94.7-1
- Related: #661863
- Add buildrequires for python-setuptools.

* Thu Dec 16 2010 Devan Goodwin <dgoodwin@redhat.com> 0.94.4-1
- Add python-rhsm tito.props. (dgoodwin@redhat.com)

* Thu Dec 16 2010 Devan Goodwin <dgoodwin@redhat.com> 0.94.3-1
- Refactor logging. (dgoodwin@redhat.com)
- Add a small README. (dgoodwin@redhat.com)

* Tue Dec 14 2010 Devan Goodwin <dgoodwin@redhat.com> 0.94.2-1
- Remove I18N code. (dgoodwin@redhat.com)
- Spec cleanup. (dgoodwin@redhat.com)
- Cleaning out unused log parsing functions (jharris@redhat.com)
- More tolerant with no rhsm.conf in place. (dgoodwin@redhat.com)
- Switch to python-iniparse. (alikins@redhat.com)

* Fri Dec 10 2010 Devan Goodwin <dgoodwin@redhat.com> 0.94.1-1
- Initial package tagging.

