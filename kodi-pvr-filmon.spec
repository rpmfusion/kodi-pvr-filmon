%global commit ab9b5198feb7eb2ff94ea495414ff214c09c9391
%global short_commit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20170407

%global kodi_addon pvr.filmon
%global kodi_version 17.0

Name:           kodi-%(tr "." "-" <<<%{kodi_addon})
# Use Epoch to manage upgrades from older upstream
# (https://github.com/opdenkamp/xbmc-pvr-addons/)
Epoch:          1
Version:        1.4.9
Release:        1%{?dist}
Summary:        Kodi's Filmon client addon

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/kodi-pvr/%{kodi_addon}/
Source0:        https://github.com/kodi-pvr/%{kodi_addon}/archive/%{short_commit}/%{name}-%{short_commit}.tar.gz
# GPLv2 license file
Source1:        http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
# Fix jsoncpp library detection
Patch0:         %{name}-1.4.9-jsoncpp.patch

BuildRequires:  gcc-c++
BuildRequires:  jsoncpp-devel
BuildRequires:  kodi-platform-devel >= %{kodi_version}
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  platform-devel
Requires:       kodi >= %{kodi_version}
ExclusiveArch:  i686 x86_64

%description
Filmon PVR client. Supports live TV, recordings, EPG. Requires a Filmon
subscription.

Before enabling:
(a) in Filmon set channels as favorite to see them in Kodi
(b) enter your username and password in this addon's settings.

Note: recordings can take several minutes to appear after timer is completed.


%prep
%autosetup -n %{kodi_addon}-%{commit}

cp -p %{SOURCE1} .


%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir}/kodi/ .
%make_build


%install
%make_install


%files
%doc README.md %{kodi_addon}/changelog.txt
%license gpl-2.0.txt
%{_libdir}/kodi/addons/%{kodi_addon}/
%{_datadir}/kodi/addons/%{kodi_addon}/


%changelog
* Sat Apr 29 2017 Mohamed El Morabity <melmorabity@fedorapeople.org> - 1:1.4.9-1
- Update to latest stable release for Kodi 17

* Sun Jul 24 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:0.7.8-1
- Update to latest stable release for Kodi 16

* Mon Aug 24 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:0.5.9-1
- Initial RPM release
