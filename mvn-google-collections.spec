#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-google-collections
Version  : 1.0
Release  : 2
URL      : https://repo1.maven.org/maven2/com/google/collections/google-collections/1.0/google-collections-1.0.jar
Source0  : https://repo1.maven.org/maven2/com/google/collections/google-collections/1.0/google-collections-1.0.jar
Source1  : https://repo1.maven.org/maven2/com/google/collections/google-collections/1.0/google-collections-1.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-google-collections-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-google-collections package.
Group: Data

%description data
data components for the mvn-google-collections package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/collections/google-collections/1.0
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/com/google/collections/google-collections/1.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/collections/google-collections/1.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/google/collections/google-collections/1.0


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/google/collections/google-collections/1.0/google-collections-1.0.jar
/usr/share/java/.m2/repository/com/google/collections/google-collections/1.0/google-collections-1.0.pom
