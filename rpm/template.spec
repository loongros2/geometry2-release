%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-tf2-ros-py
Version:        0.39.1
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS tf2_ros_py package

License:        BSD
URL:            http://www.ros.org/wiki/tf2_ros
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-rolling-builtin-interfaces
Requires:       ros-rolling-geometry-msgs
Requires:       ros-rolling-rclpy
Requires:       ros-rolling-sensor-msgs
Requires:       ros-rolling-std-msgs
Requires:       ros-rolling-tf2-msgs
Requires:       ros-rolling-tf2-py
Requires:       ros-rolling-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-rolling-sensor-msgs
%endif

%description
This package contains the ROS Python bindings for the tf2 library

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/rolling"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Tue Oct 15 2024 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 0.39.1-1
- Autogenerated by Bloom

* Thu Oct 03 2024 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 0.39.0-1
- Autogenerated by Bloom

* Fri Jul 19 2024 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 0.38.2-1
- Autogenerated by Bloom

* Tue Jul 09 2024 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 0.38.1-1
- Autogenerated by Bloom

* Mon Jun 17 2024 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 0.38.0-1
- Autogenerated by Bloom

* Wed May 29 2024 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 0.37.1-1
- Autogenerated by Bloom

* Fri Apr 26 2024 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 0.37.0-1
- Autogenerated by Bloom

* Wed Apr 10 2024 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 0.36.2-1
- Autogenerated by Bloom

* Thu Mar 28 2024 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 0.36.1-1
- Autogenerated by Bloom

* Wed Mar 06 2024 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 0.36.0-2
- Autogenerated by Bloom

