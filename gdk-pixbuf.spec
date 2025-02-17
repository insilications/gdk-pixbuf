#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : gdk-pixbuf
Version  : 2.42.6
Release  : 304
URL      : file:///aot/build/clearlinux/packages/gdk-pixbuf/gdk-pixbuf-v2.42.6.tar.gz
Source0  : file:///aot/build/clearlinux/packages/gdk-pixbuf/gdk-pixbuf-v2.42.6.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: gdk-pixbuf-bin = %{version}-%{release}
Requires: gdk-pixbuf-data = %{version}-%{release}
Requires: gdk-pixbuf-lib = %{version}-%{release}
Requires: gdk-pixbuf-locales = %{version}-%{release}
Requires: gdk-pixbuf-man = %{version}-%{release}
Requires: librsvg-lib
Requires: shared-mime-info
BuildRequires : binutils-dev
BuildRequires : boost-dev
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : cairo-dev
BuildRequires : cairo-staticdev
BuildRequires : dbus
BuildRequires : dbus-broker
BuildRequires : dbus-dev
BuildRequires : dbus-glib
BuildRequires : dbus-glib-dev
BuildRequires : docbook-utils
BuildRequires : docbook-xml
BuildRequires : doxygen
BuildRequires : glib-dev
BuildRequires : glib-lib
BuildRequires : glib-staticdev
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : graphviz
BuildRequires : graphviz-dev
BuildRequires : grep
BuildRequires : gtk+-data
BuildRequires : gtk+-dev
BuildRequires : gtk+-lib
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : gtk3-dev
BuildRequires : gtk3-lib
BuildRequires : gtk4
BuildRequires : gtk4-dev
BuildRequires : gtk4-lib
BuildRequires : libX11-data
BuildRequires : libX11-dev
BuildRequires : libX11-lib
BuildRequires : libXrender-dev
BuildRequires : libdrm-dev
BuildRequires : libdrm-staticdev
BuildRequires : libffi-dev
BuildRequires : libffi-staticdev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libjpeg-turbo-staticdev
BuildRequires : libpng-dev
BuildRequires : libpng-staticdev
BuildRequires : librsvg
BuildRequires : librsvg-dev
BuildRequires : librsvg-staticdev
BuildRequires : libxcb-dev
BuildRequires : libxslt
BuildRequires : libxslt-bin
BuildRequires : libxslt-dev
BuildRequires : lzo
BuildRequires : lzo-dev
BuildRequires : lzo-staticdev
BuildRequires : mesa-dev
BuildRequires : mm-common
BuildRequires : mm-common-dev
BuildRequires : openjpeg
BuildRequires : openjpeg-dev
BuildRequires : openjpeg-staticdev
BuildRequires : pixman-dev
BuildRequires : pixman-staticdev
BuildRequires : pkg-config
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libffi)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(x11)
BuildRequires : python-graphviz
BuildRequires : qemu
BuildRequires : shared-mime-info
BuildRequires : shared-mime-info-dev
BuildRequires : systemd
BuildRequires : systemd-dev
BuildRequires : tiff
BuildRequires : tiff-dev
BuildRequires : tiff-staticdev
BuildRequires : xauth
BuildRequires : xcb-proto
BuildRequires : xcb-proto-dev
BuildRequires : xcb-util-cursor-dev
BuildRequires : xcb-util-dev
BuildRequires : xcb-util-keysyms-dev
BuildRequires : xcb-util-renderutil-dev
BuildRequires : xcb-util-wm-dev
BuildRequires : xcb-util-xrm-dev
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
BuildRequires : zlib
BuildRequires : zlib-dev
BuildRequires : zlib-staticdev
BuildRequires : zstd-dev
BuildRequires : zstd-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: mime-fallback.patch

%description
The code in this directory implements optimized, filtered scaling
for pixmap data.

%package bin
Summary: bin components for the gdk-pixbuf package.
Group: Binaries
Requires: gdk-pixbuf-data = %{version}-%{release}

%description bin
bin components for the gdk-pixbuf package.


%package data
Summary: data components for the gdk-pixbuf package.
Group: Data

%description data
data components for the gdk-pixbuf package.


%package dev
Summary: dev components for the gdk-pixbuf package.
Group: Development
Requires: gdk-pixbuf-lib = %{version}-%{release}
Requires: gdk-pixbuf-bin = %{version}-%{release}
Requires: gdk-pixbuf-data = %{version}-%{release}
Provides: gdk-pixbuf-devel = %{version}-%{release}
Requires: gdk-pixbuf = %{version}-%{release}

%description dev
dev components for the gdk-pixbuf package.


%package lib
Summary: lib components for the gdk-pixbuf package.
Group: Libraries
Requires: gdk-pixbuf-data = %{version}-%{release}

%description lib
lib components for the gdk-pixbuf package.


%package locales
Summary: locales components for the gdk-pixbuf package.
Group: Default

%description locales
locales components for the gdk-pixbuf package.


%package man
Summary: man components for the gdk-pixbuf package.
Group: Default

%description man
man components for the gdk-pixbuf package.


%package staticdev
Summary: staticdev components for the gdk-pixbuf package.
Group: Default
Requires: gdk-pixbuf-dev = %{version}-%{release}

%description staticdev
staticdev components for the gdk-pixbuf package.


%prep
%setup -q -n gdk-pixbuf
cd %{_builddir}/gdk-pixbuf
%patch1 -p1

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1628513296
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-partial-training"
export CFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export FCFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export FFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export CXXFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -fvisibility-inlines-hidden -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export LDFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -lpthread -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
## pgo use
## -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fPIC -Wl,-z,max-page-size=0x1000 -fvisibility=hidden -flto-partition=none
## gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common -funroll-loops
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export FCFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export FFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export CXXFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export LDFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -lpthread $PGO_USE"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
#
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/dri:/usr/lib64/haswell:/usr/lib64:/usr/lib:/usr/share"
#
export LIBRARY_PATH="$LIBRARY_PATH:/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/dri:/usr/lib64/haswell:/usr/lib64:/usr/lib:/usr/share"
#
export PATH="$PATH:/usr/local/cuda/bin:/usr/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
#
export CPATH="$CPATH:/usr/local/cuda/include"
#
## altflags_pgo end
if [ ! -f statuspgo ]; then
echo PGO Phase 1
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
meson --libdir=lib64 --prefix=/usr --buildtype=release -Ddefault_library=both  -Dtiff=enabled \
-Djpeg=enabled \
-Dpng=enabled \
-Dintrospection=enabled \
-Dgtk_doc=false \
-Dman=true \
-Ddocs=false \
-Dinstalled_tests=false builddir
ninja --verbose %{?_smp_mflags} -v -C builddir

meson test --verbose --num-processes 1 -C builddir || :
find builddir/ -type f,l -not -name '*.gcno' -not -name 'statuspgo*' -delete -print  || :
echo USED > statuspgo
fi
if [ -f statuspgo ]; then
echo PGO Phase 2
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
meson --libdir=lib64 --prefix=/usr --buildtype=release -Ddefault_library=both -Dtiff=enabled \
-Djpeg=enabled \
-Dpng=enabled \
-Dintrospection=enabled \
-Dgtk_doc=false \
-Ddocs=false \
-Dinstalled_tests=false  builddir
ninja --verbose %{?_smp_mflags} -v -C builddir
fi


%install
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gdk-pixbuf
## install_append content
cp %{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/lib*svg*.so %{buildroot}%{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/. || :
mkdir -p %{buildroot}%{_libdir}/gdk-pixbuf-2.0/2.10.0/ || :
# LD_LIBRARY_PATH=%{buildroot}%{_libdir} GDK_PIXBUF_MODULE_FILE=%{buildroot}%{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders.cache %{buildroot}%{_bindir}/gdk-pixbuf-query-loaders | sed "s@%{buildroot}@@g" > %{buildroot}%{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders.cache || :
LD_LIBRARY_PATH=%{buildroot}%{_libdir} GDK_PIXBUF_MODULE_FILE=%{buildroot}%{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders.cache %{buildroot}%{_bindir}/gdk-pixbuf-query-loaders %{buildroot}%{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/lib*.so | sed "s@%{buildroot}@@g" > %{buildroot}%{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders.cache || :
rm %{buildroot}%{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/lib*svg*.so || :
#sed -e 's/lib64/lib32/g' %{buildroot}%{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders.cache > %{buildroot}/usr/lib32/gdk-pixbuf-2.0/2.10.0/loaders.cache
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gdk-pixbuf-csource
/usr/bin/gdk-pixbuf-pixdata
/usr/bin/gdk-pixbuf-query-loaders
/usr/bin/gdk-pixbuf-thumbnailer

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/GdkPixbuf-2.0.typelib
/usr/lib64/girepository-1.0/GdkPixdata-2.0.typelib
/usr/share/gir-1.0/*.gir
/usr/share/thumbnailers/gdk-pixbuf-thumbnailer.thumbnailer

%files dev
%defattr(-,root,root,-)
/usr/include/gdk-pixbuf-2.0/gdk-pixbuf/gdk-pixbuf-animation.h
/usr/include/gdk-pixbuf-2.0/gdk-pixbuf/gdk-pixbuf-autocleanups.h
/usr/include/gdk-pixbuf-2.0/gdk-pixbuf/gdk-pixbuf-core.h
/usr/include/gdk-pixbuf-2.0/gdk-pixbuf/gdk-pixbuf-enum-types.h
/usr/include/gdk-pixbuf-2.0/gdk-pixbuf/gdk-pixbuf-features.h
/usr/include/gdk-pixbuf-2.0/gdk-pixbuf/gdk-pixbuf-io.h
/usr/include/gdk-pixbuf-2.0/gdk-pixbuf/gdk-pixbuf-loader.h
/usr/include/gdk-pixbuf-2.0/gdk-pixbuf/gdk-pixbuf-macros.h
/usr/include/gdk-pixbuf-2.0/gdk-pixbuf/gdk-pixbuf-marshal.h
/usr/include/gdk-pixbuf-2.0/gdk-pixbuf/gdk-pixbuf-simple-anim.h
/usr/include/gdk-pixbuf-2.0/gdk-pixbuf/gdk-pixbuf-transform.h
/usr/include/gdk-pixbuf-2.0/gdk-pixbuf/gdk-pixbuf.h
/usr/include/gdk-pixbuf-2.0/gdk-pixbuf/gdk-pixdata.h
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders.cache
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-ani.so
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-bmp.so
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-gif.so
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-icns.so
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-ico.so
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-pnm.so
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-qtif.so
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-tga.so
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-tiff.so
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-xbm.so
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-xpm.so
/usr/lib64/libgdk_pixbuf-2.0.so
/usr/lib64/pkgconfig/gdk-pixbuf-2.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgdk_pixbuf-2.0.so.0
/usr/lib64/libgdk_pixbuf-2.0.so.0.4200.7

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gdk-pixbuf-csource.1
/usr/share/man/man1/gdk-pixbuf-query-loaders.1

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libgdk_pixbuf-2.0.a

%files locales -f gdk-pixbuf.lang
%defattr(-,root,root,-)
