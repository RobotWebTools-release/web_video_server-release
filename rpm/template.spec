Name:           ros-melodic-web-video-server
Version:        0.2.1
Release:        1%{?dist}
Summary:        ROS web_video_server package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/web_video_server
Source0:        %{name}-%{version}.tar.gz

Requires:       ffmpeg-devel
Requires:       ros-melodic-async-web-server-cpp
Requires:       ros-melodic-cv-bridge
Requires:       ros-melodic-image-transport
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-roslib
Requires:       ros-melodic-sensor-msgs
BuildRequires:  ffmpeg-devel
BuildRequires:  ros-melodic-async-web-server-cpp
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-cv-bridge
BuildRequires:  ros-melodic-image-transport
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-roslib
BuildRequires:  ros-melodic-sensor-msgs

%description
HTTP Streaming of ROS Image Topics in Multiple Formats

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Wed Jun 05 2019 Russell Toris <rctoris@wpi.edu> - 0.2.1-1
- Autogenerated by Bloom

* Wed Jan 30 2019 Russell Toris <rctoris@wpi.edu> - 0.2.0-0
- Autogenerated by Bloom

