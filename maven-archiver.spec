%{?scl:%scl_package maven-archiver}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}maven-archiver
Version:        3.1.1
Release:        2.2%{?dist}
Epoch:          0
Summary:        Maven Archiver
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-archiver/
BuildArch:      noarch

Source0:        http://repo1.maven.org/maven2/org/apache/maven/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.zip

Patch0:         0001-Port-tests-to-Eclipse-Aether.patch
# Test fails with OpenJDK on Linux
# Reported upstream: https://issues.apache.org/jira/browse/MSHARED-448
Patch1:         0002-MSHARED-448-Skip-failing-assertion.patch

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(commons-io:commons-io)
BuildRequires:  %{?scl_prefix}mvn(junit:junit)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-artifact)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-core)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-model)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  %{?scl_prefix}mvn(org.assertj:assertj-core)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-utils)

%description
The Maven Archiver is used by other Maven plugins
to handle packaging

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
Javadoc for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q
%patch0 -p1
%patch1 -p1

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Thu Jun 22 2017 Michael Simacek <msimacek@redhat.com> - 0:3.1.1-2.2
- Mass rebuild 2017-06-22

* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 0:3.1.1-2.1
- Automated package import and SCL-ization

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jun 20 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:3.1.1-1
- Update to upstream version 3.1.1

* Thu Apr 28 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:3.0.2-1
- Update to upstream version 3.0.2

* Wed Apr 13 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:3.0.1-1
- Update to upstream version 3.0.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0:3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 19 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:3.0.0-1
- Update to upstream version 3.0.0
- Remove legacy obsoletes/provides

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Oct 27 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.6-1
- Update to upstream version 2.6

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:2.5-10
- Use Requires: java-headless rebuild (#1067528)

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.5-9
- Fix unowned directory

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 19 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.5-7
- Build with xmvn

* Tue Feb 19 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.5-6
- Add missing license files

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0:2.5-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 16 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:2.5-2
- Add versioned BR/R on plexus-archiver and rebuild

* Wed Feb 15 2012 Alexander Kurtakov <akurtako@redhat.com> 0:2.5-1
- Update to latest upstream release.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 6 2011 Alexander Kurtakov <akurtako@redhat.com> 0:2.4.2-1
- Update to 2.4.2 upstream release.

* Mon Sep 19 2011 Tomas Radej <tradej@redhat.com> - 0:2.4.1-7
- Fixed dep on maven-core artifact
- Minor fixes

* Wed Jun 8 2011 Alexander Kurtakov <akurtako@redhat.com> 0:2.4.1-6
- Build with maven 3.x.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 8 2010 Alexander Kurtakov <akurtako@redhat.com> 0:2.4.1-4
- Add missing BR.

* Mon Nov 8 2010 Alexander Kurtakov <akurtako@redhat.com> 0:2.4.1-3
- Remove tests as they don't compile.

* Mon May 31 2010 Alexander Kurtakov <akurtako@redhat.com> 0:2.4.1-2
- BR java-devel >= 1:1.6.0.

* Sat May 29 2010 Alexander Kurtakov <akurtako@redhat.com> 0:2.4.1-1
- Update to 2.4.1.

* Wed Dec 23 2009 Alexander Kurtakov <akurtako@redhat.com> 0:2.4-1
- Update to 2.4.

* Mon Dec 21 2009 Alexander Kurtakov <akurtako@redhat.com> 0:2.2-3
- BR maven-surefire-provider-junit.

* Mon Aug 31 2009 Alexander Kurtakov <akurtako@redhat.com> 0:2.2-2
- Fix line length.
- Own only specific fragment and pom.

* Wed May 20 2009 Fernando Nasser <fnasser@redhat.com> 0:2.2-1
- Fix license
- Update instructions to obtain sources
- Refresh source tar ball

* Thu Jul 26 2007 Deepak Bhole <dbhole@redhat.com> 0:2.2-0jpp.1
- Initial build
