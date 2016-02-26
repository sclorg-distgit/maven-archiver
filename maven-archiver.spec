%global pkg_name maven-archiver
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        2.5
Release:        9.12%{?dist}
Epoch:          0
Summary:        Maven Archiver
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-archiver/
Source0:        http://repo1.maven.org/maven2/org/apache/maven/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.zip
BuildArch:      noarch

BuildRequires:  %{?scl_prefix_java_common}javapackages-tools
BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}maven-shared
BuildRequires:  %{?scl_prefix}maven-resources-plugin
BuildRequires:  %{?scl_prefix}maven-site-plugin
BuildRequires:  %{?scl_prefix}maven-doxia-sitetools
BuildRequires:  %{?scl_prefix}maven-shared-jar
BuildRequires:  %{?scl_prefix}plexus-interpolation
BuildRequires:  %{?scl_prefix}plexus-archiver >= 2.1-1
BuildRequires:  %{?scl_prefix}plexus-utils
BuildRequires:  %{?scl_prefix}apache-commons-parent


%description
The Maven Archiver is used by other Maven plugins
to handle packaging

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
Javadoc for %{pkg_name}.

%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%pom_add_dep org.apache.maven:maven-core
# tests don't compile with maven 2.2.1
rm -fr src/test/java/org/apache/maven/archiver/*.java
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Mon Feb 08 2016 Michal Srb <msrb@redhat.com> - 0:2.5-9.12
- Fix BR on maven-local & co.

* Mon Jan 11 2016 Michal Srb <msrb@redhat.com> - 0:2.5-9.11
- maven33 rebuild #2

* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 0:2.5-9.10
- maven33 rebuild

* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.5-9.9
- Add directory ownership on %%{_mavenpomdir} subdir

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 0:2.5-9.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 0:2.5-9.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.5-9.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.5-9.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.5-9.4
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.5-9.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.5-9.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.5-9.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 02.5-9
- Mass rebuild 2013-12-27

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.5-8
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

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
