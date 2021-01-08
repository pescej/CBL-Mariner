%global debug_package %{nil}
%global gemdir %(IFS=: R=($(gem env gempath)); echo ${R[${#R[@]}-1]})
%global gem_name console
Summary:        Beautiful logging for Ruby
Name:           rubygem-console
Version:        1.10.1
Release:        1%{?dist}
License:        MIT
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          Development/Languages
URL:            https://rubygems.org/gems/%{gem_name}/versions/%{version}
Source0:        https://rubygems.org/downloads/%{gem_name}-%{version}.gem
BuildRequires:  ruby >= 2.5.0
Requires:       rubygem-fiber-local

%description
Provides beautiful console logging for Ruby applications.
Implements fast, buffered log output.

%prep
%setup -q -c -T

%build

%install
gem install -V --local --force --install-dir %{buildroot}/%{gemdir} %{SOURCE0}

%files
%defattr(-,root,root,-)
%{gemdir}

%changelog
