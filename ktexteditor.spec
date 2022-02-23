#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : ktexteditor
Version  : 5.91.0
Release  : 408
URL      : file:///aot/build/clearlinux/packages/ktexteditor/ktexteditor-v5.91.0.tar.gz
Source0  : file:///aot/build/clearlinux/packages/ktexteditor/ktexteditor-v5.91.0.tar.gz
Summary  : Advanced embeddable text editor
Group    : Development/Tools
License  : GPL-2.0
Requires: ktexteditor-data = %{version}-%{release}
Requires: ktexteditor-lib = %{version}-%{release}
Requires: ktexteditor-libexec = %{version}-%{release}
BuildRequires : breeze
BuildRequires : breeze-gtk
BuildRequires : breeze-icons
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : buildreq-qmake
BuildRequires : cairo-dev
BuildRequires : curl
BuildRequires : curl-dev
BuildRequires : curl-lib
BuildRequires : dbus
BuildRequires : dbus-dev
BuildRequires : extra-cmake-modules-data
BuildRequires : fontconfig
BuildRequires : fontconfig-dev
BuildRequires : fonts-clear
BuildRequires : frameworkintegration-dev
BuildRequires : frameworkintegration-lib
BuildRequires : frameworkintegration-license
BuildRequires : freetype
BuildRequires : freetype-dev
BuildRequires : graphite
BuildRequires : graphite-dev
BuildRequires : kactivities-dev
BuildRequires : karchive-dev
BuildRequires : kauth
BuildRequires : kauth-dev
BuildRequires : kbookmarks-dev
BuildRequires : kcodecs-dev
BuildRequires : kcompletion-dev
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kdecoration-dev
BuildRequires : kdecoration-lib
BuildRequires : kdoctools-dev
BuildRequires : keyutils
BuildRequires : keyutils-dev
BuildRequires : kglobalaccel-dev
BuildRequires : kguiaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kiconthemes-dev
BuildRequires : kio-dev
BuildRequires : kitemmodels-dev
BuildRequires : kitemviews-dev
BuildRequires : knewstuff-dev
BuildRequires : knotifyconfig-dev
BuildRequires : konsole
BuildRequires : kparts-dev
BuildRequires : krb5
BuildRequires : krb5-dev
BuildRequires : ktextwidgets-dev
BuildRequires : kwallet-dev
BuildRequires : libICE-dev
BuildRequires : libSM-dev
BuildRequires : libX11-data
BuildRequires : libX11-dev
BuildRequires : libX11-lib
BuildRequires : libXScrnSaver
BuildRequires : libXScrnSaver-dev
BuildRequires : libXScrnSaver-lib
BuildRequires : libXau-dev
BuildRequires : libXau-lib
BuildRequires : libXcomposite-dev
BuildRequires : libXcursor-dev
BuildRequires : libXcursor-lib
BuildRequires : libXdamage-dev
BuildRequires : libXdamage-lib
BuildRequires : libXdmcp-dev
BuildRequires : libXdmcp-lib
BuildRequires : libXext-dev
BuildRequires : libXext-lib
BuildRequires : libXfixes-dev
BuildRequires : libXfont2-dev
BuildRequires : libXft-dev
BuildRequires : libXft-lib
BuildRequires : libXi-dev
BuildRequires : libXi-lib
BuildRequires : libXinerama-dev
BuildRequires : libXmu-dev
BuildRequires : libXpm-dev
BuildRequires : libXrandr-dev
BuildRequires : libXrender-dev
BuildRequires : libXrender-lib
BuildRequires : libXres-dev
BuildRequires : libXt-dev
BuildRequires : libXtst-dev
BuildRequires : libXtst-lib
BuildRequires : libXv-dev
BuildRequires : libXxf86vm-dev
BuildRequires : libXxf86vm-lib
BuildRequires : libgcrypt-dev
BuildRequires : libgit2
BuildRequires : libgit2-dev
BuildRequires : libogg-dev
BuildRequires : libsndfile-dev
BuildRequires : libvorbis-dev
BuildRequires : libxcb-dev
BuildRequires : libxcb-lib
BuildRequires : libxml2-dev
BuildRequires : libxml2-staticdev
BuildRequires : m4
BuildRequires : mesa-dev
BuildRequires : openssh
BuildRequires : openssl-dev
BuildRequires : openssl-staticdev
BuildRequires : opus-dev
BuildRequires : pcre-dev
BuildRequires : pcre-staticdev
BuildRequires : pcre2-dev
BuildRequires : pcre2-staticdev
BuildRequires : pixman-dev
BuildRequires : pixman-staticdev
BuildRequires : pkg-config
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(libarchive)
BuildRequires : pkgconfig(libgcrypt)
BuildRequires : pkgconfig(liblzma)
BuildRequires : pkgconfig(libzstd)
BuildRequires : plasma-framework-dev
BuildRequires : polkit-qt-dev
BuildRequires : pypi-requests
BuildRequires : python3-dev
BuildRequires : python3-staticdev
BuildRequires : qtbase-dev
BuildRequires : setxkbmap
BuildRequires : sonnet-dev
BuildRequires : syntax-highlighting-dev
BuildRequires : syntax-highlighting-staticdev
BuildRequires : util-linux
BuildRequires : util-linux-dev
BuildRequires : wayland
BuildRequires : wayland-dev
BuildRequires : xauth
BuildRequires : xclip
BuildRequires : xdg-dbus-proxy
BuildRequires : xdg-desktop-portal
BuildRequires : xdg-desktop-portal-dev
BuildRequires : xdg-desktop-portal-gtk
BuildRequires : xdg-desktop-portal-kde
BuildRequires : xdg-user-dirs
BuildRequires : xdg-user-dirs-gtk
BuildRequires : xdg-utils
BuildRequires : xdotool
BuildRequires : xdpyinfo
BuildRequires : xf86-input-libinput
BuildRequires : xf86-video-amdgpu
BuildRequires : xf86-video-ati
BuildRequires : xf86-video-fbdev
BuildRequires : xf86-video-nouveau
BuildRequires : xf86-video-qxl
BuildRequires : xf86-video-vboxvideo
BuildRequires : xf86-video-vesa
BuildRequires : xf86-video-vmware
BuildRequires : xfontsel
BuildRequires : xhost
BuildRequires : xinit
BuildRequires : xinput
BuildRequires : xkbcomp
BuildRequires : xkeyboard-config
BuildRequires : xkill
BuildRequires : xmodmap
BuildRequires : xorg-server
BuildRequires : xorg-server-dev
BuildRequires : xorgproto
BuildRequires : xorgproto-dev
BuildRequires : xprop
BuildRequires : xrandr
BuildRequires : xrdb
BuildRequires : xrdp
BuildRequires : xrestop
BuildRequires : xscreensaver
BuildRequires : xsel
BuildRequires : xset
BuildRequires : xsetroot
BuildRequires : xvfb-run
BuildRequires : xwd
BuildRequires : xwininfo
BuildRequires : xz
BuildRequires : xz-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package data
Summary: data components for the ktexteditor package.
Group: Data

%description data
data components for the ktexteditor package.


%package dev
Summary: dev components for the ktexteditor package.
Group: Development
Requires: ktexteditor-lib = %{version}-%{release}
Requires: ktexteditor-data = %{version}-%{release}
Provides: ktexteditor-devel = %{version}-%{release}
Requires: ktexteditor = %{version}-%{release}

%description dev
dev components for the ktexteditor package.


%package lib
Summary: lib components for the ktexteditor package.
Group: Libraries
Requires: ktexteditor-data = %{version}-%{release}
Requires: ktexteditor-libexec = %{version}-%{release}

%description lib
lib components for the ktexteditor package.


%package libexec
Summary: libexec components for the ktexteditor package.
Group: Default

%description libexec
libexec components for the ktexteditor package.


%prep
%setup -q -n ktexteditor
cd %{_builddir}/ktexteditor

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1645634876
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags1 content
## altflags1
unset ASFLAGS
export CFLAGS="-DNDEBUG -ggdb3 -ggnu-pubnames -Og -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -static-libstdc++ -static-libgcc -pthread"
export ASMFLAGS="-DNDEBUG -ggdb3 -ggnu-pubnames -Og -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -static-libstdc++ -static-libgcc -pthread"
export CXXFLAGS="-DNDEBUG -ggdb3 -ggnu-pubnames -Og -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -static-libstdc++ -static-libgcc -pthread"
export FCFLAGS="-DNDEBUG -ggdb3 -ggnu-pubnames -Og -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -static-libstdc++ -static-libgcc -pthread"
export FFLAGS="-DNDEBUG -ggdb3 -ggnu-pubnames -Og -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -static-libstdc++ -static-libgcc -pthread"
export LDFLAGS="-DNDEBUG -ggdb3 -ggnu-pubnames -Og -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -static-libstdc++ -static-libgcc -pthread"
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
export MAKEFLAGS=%{?_smp_mflags}
%global _lto_cflags 1
%global _disable_maintainer_mode 1
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:/usr/share/pkgconfig"
export LD_LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/local/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
export CPATH="/usr/local/cuda/include"
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=1
export __GL_SYNC_DISPLAY_DEVICE=HDMI-0
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=HDMI-0
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH="/usr/share/defaults/fonts"
export GTK_IM_MODULE="xim"
export QT_IM_MODULE="cedilla"
export FREETYPE_PROPERTIES="truetype:interpreter-version=40"
export NO_AT_BRIDGE=1
export GTK_A11Y=none
export PLASMA_USE_QT_SCALING=1
export QT_AUTO_SCREEN_SCALE_FACTOR=0
export QT_ENABLE_HIGHDPI_SCALING=0
export QT_FONT_DPI=88
export GTK_USE_PORTAL=1
export DESKTOP_SESSION=plasma
## altflags1 end
%cmake ..   -DKDE_INSTALL_CONFDIR=/usr/share/xdg \
-DBUILD_TESTING:BOOL=OFF \
-DBUILD_SHARED_LIBS:BOOL=ON
make  %{?_smp_mflags}    V=1 VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1645634876
rm -rf %{buildroot}
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags1 content
## altflags1
unset ASFLAGS
export CFLAGS="-DNDEBUG -ggdb3 -ggnu-pubnames -Og -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -static-libstdc++ -static-libgcc -pthread"
export ASMFLAGS="-DNDEBUG -ggdb3 -ggnu-pubnames -Og -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -static-libstdc++ -static-libgcc -pthread"
export CXXFLAGS="-DNDEBUG -ggdb3 -ggnu-pubnames -Og -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -static-libstdc++ -static-libgcc -pthread"
export FCFLAGS="-DNDEBUG -ggdb3 -ggnu-pubnames -Og -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -static-libstdc++ -static-libgcc -pthread"
export FFLAGS="-DNDEBUG -ggdb3 -ggnu-pubnames -Og -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -static-libstdc++ -static-libgcc -pthread"
export LDFLAGS="-DNDEBUG -ggdb3 -ggnu-pubnames -Og -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -static-libstdc++ -static-libgcc -pthread"
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
export MAKEFLAGS=%{?_smp_mflags}
%global _lto_cflags 1
%global _disable_maintainer_mode 1
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:/usr/share/pkgconfig"
export LD_LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/local/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
export CPATH="/usr/local/cuda/include"
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=1
export __GL_SYNC_DISPLAY_DEVICE=HDMI-0
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=HDMI-0
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH="/usr/share/defaults/fonts"
export GTK_IM_MODULE="xim"
export QT_IM_MODULE="cedilla"
export FREETYPE_PROPERTIES="truetype:interpreter-version=40"
export NO_AT_BRIDGE=1
export GTK_A11Y=none
export PLASMA_USE_QT_SCALING=1
export QT_AUTO_SCREEN_SCALE_FACTOR=0
export QT_ENABLE_HIGHDPI_SCALING=0
export QT_FONT_DPI=88
export GTK_USE_PORTAL=1
export DESKTOP_SESSION=plasma
## altflags1 end
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/system-services/org.kde.ktexteditor.katetextbuffer.service
/usr/share/dbus-1/system.d/org.kde.ktexteditor.katetextbuffer.conf
/usr/share/katepart5/script/README.md
/usr/share/kdevfiletemplates/templates/ktexteditor-plugin.tar.bz2
/usr/share/kservices5/katepart.desktop
/usr/share/kservicetypes5/ktexteditor.desktop
/usr/share/kservicetypes5/ktexteditorplugin.desktop
/usr/share/polkit-1/actions/org.kde.ktexteditor.katetextbuffer.policy
/usr/share/qlogging-categories5/ktexteditor.categories
/usr/share/qlogging-categories5/ktexteditor.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KTextEditor/KTextEditor/AbstractAnnotationItemDelegate
/usr/include/KF5/KTextEditor/KTextEditor/AnnotationInterface
/usr/include/KF5/KTextEditor/KTextEditor/Application
/usr/include/KF5/KTextEditor/KTextEditor/Attribute
/usr/include/KF5/KTextEditor/KTextEditor/CodeCompletionInterface
/usr/include/KF5/KTextEditor/KTextEditor/CodeCompletionModel
/usr/include/KF5/KTextEditor/KTextEditor/CodeCompletionModelControllerInterface
/usr/include/KF5/KTextEditor/KTextEditor/Command
/usr/include/KF5/KTextEditor/KTextEditor/ConfigInterface
/usr/include/KF5/KTextEditor/KTextEditor/ConfigPage
/usr/include/KF5/KTextEditor/KTextEditor/Cursor
/usr/include/KF5/KTextEditor/KTextEditor/Document
/usr/include/KF5/KTextEditor/KTextEditor/DocumentCursor
/usr/include/KF5/KTextEditor/KTextEditor/Editor
/usr/include/KF5/KTextEditor/KTextEditor/InlineNote
/usr/include/KF5/KTextEditor/KTextEditor/InlineNoteInterface
/usr/include/KF5/KTextEditor/KTextEditor/InlineNoteProvider
/usr/include/KF5/KTextEditor/KTextEditor/LineRange
/usr/include/KF5/KTextEditor/KTextEditor/MainWindow
/usr/include/KF5/KTextEditor/KTextEditor/MarkInterface
/usr/include/KF5/KTextEditor/KTextEditor/Message
/usr/include/KF5/KTextEditor/KTextEditor/ModificationInterface
/usr/include/KF5/KTextEditor/KTextEditor/MovingCursor
/usr/include/KF5/KTextEditor/KTextEditor/MovingInterface
/usr/include/KF5/KTextEditor/KTextEditor/MovingRange
/usr/include/KF5/KTextEditor/KTextEditor/MovingRangeFeedback
/usr/include/KF5/KTextEditor/KTextEditor/Plugin
/usr/include/KF5/KTextEditor/KTextEditor/Range
/usr/include/KF5/KTextEditor/KTextEditor/SessionConfigInterface
/usr/include/KF5/KTextEditor/KTextEditor/TextHintInterface
/usr/include/KF5/KTextEditor/KTextEditor/View
/usr/include/KF5/KTextEditor/ktexteditor/abstractannotationitemdelegate.h
/usr/include/KF5/KTextEditor/ktexteditor/annotationinterface.h
/usr/include/KF5/KTextEditor/ktexteditor/application.h
/usr/include/KF5/KTextEditor/ktexteditor/attribute.h
/usr/include/KF5/KTextEditor/ktexteditor/codecompletioninterface.h
/usr/include/KF5/KTextEditor/ktexteditor/codecompletionmodel.h
/usr/include/KF5/KTextEditor/ktexteditor/codecompletionmodelcontrollerinterface.h
/usr/include/KF5/KTextEditor/ktexteditor/command.h
/usr/include/KF5/KTextEditor/ktexteditor/configinterface.h
/usr/include/KF5/KTextEditor/ktexteditor/configpage.h
/usr/include/KF5/KTextEditor/ktexteditor/cursor.h
/usr/include/KF5/KTextEditor/ktexteditor/document.h
/usr/include/KF5/KTextEditor/ktexteditor/documentcursor.h
/usr/include/KF5/KTextEditor/ktexteditor/editor.h
/usr/include/KF5/KTextEditor/ktexteditor/inlinenote.h
/usr/include/KF5/KTextEditor/ktexteditor/inlinenoteinterface.h
/usr/include/KF5/KTextEditor/ktexteditor/inlinenoteprovider.h
/usr/include/KF5/KTextEditor/ktexteditor/linerange.h
/usr/include/KF5/KTextEditor/ktexteditor/mainwindow.h
/usr/include/KF5/KTextEditor/ktexteditor/markinterface.h
/usr/include/KF5/KTextEditor/ktexteditor/message.h
/usr/include/KF5/KTextEditor/ktexteditor/modificationinterface.h
/usr/include/KF5/KTextEditor/ktexteditor/movingcursor.h
/usr/include/KF5/KTextEditor/ktexteditor/movinginterface.h
/usr/include/KF5/KTextEditor/ktexteditor/movingrange.h
/usr/include/KF5/KTextEditor/ktexteditor/movingrangefeedback.h
/usr/include/KF5/KTextEditor/ktexteditor/plugin.h
/usr/include/KF5/KTextEditor/ktexteditor/range.h
/usr/include/KF5/KTextEditor/ktexteditor/sessionconfiginterface.h
/usr/include/KF5/KTextEditor/ktexteditor/texthintinterface.h
/usr/include/KF5/KTextEditor/ktexteditor/view.h
/usr/include/KF5/KTextEditor/ktexteditor_export.h
/usr/include/KF5/KTextEditor/ktexteditor_version.h
/usr/lib64/cmake/KF5TextEditor/KF5TextEditorConfig.cmake
/usr/lib64/cmake/KF5TextEditor/KF5TextEditorConfigVersion.cmake
/usr/lib64/cmake/KF5TextEditor/KF5TextEditorTargets-none.cmake
/usr/lib64/cmake/KF5TextEditor/KF5TextEditorTargets.cmake
/usr/lib64/libKF5TextEditor.so
/usr/lib64/qt5/mkspecs/modules/qt_KTextEditor.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5TextEditor.so.5
/usr/lib64/libKF5TextEditor.so.5.92.0
/usr/lib64/qt5/plugins/kf5/parts/katepart.so

%files libexec
%defattr(-,root,root,-)
/usr/lib64/libexec/kauth/kauth_ktexteditor_helper
