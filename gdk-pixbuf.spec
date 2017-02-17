#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gdk-pixbuf
Version  : 2.36.5
Release  : 31
URL      : http://ftp.gnome.org/pub/GNOME/sources/gdk-pixbuf/2.36/gdk-pixbuf-2.36.5.tar.xz
Source0  : http://ftp.gnome.org/pub/GNOME/sources/gdk-pixbuf/2.36/gdk-pixbuf-2.36.5.tar.xz
Summary  : Image loading and scaling, Not Installed
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0 LGPL-2.1
Requires: gdk-pixbuf-bin
Requires: gdk-pixbuf-lib
Requires: gdk-pixbuf-doc
Requires: gdk-pixbuf-locales
Requires: gdk-pixbuf-data
BuildRequires : docbook-xml
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : gettext
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libjpeg-turbo-dev32
BuildRequires : libpng-dev32
BuildRequires : librsvg
BuildRequires : librsvg-dev
BuildRequires : librsvg-dev32
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(32glib-2.0)
BuildRequires : pkgconfig(32gobject-2.0)
BuildRequires : pkgconfig(32x11)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(libffi)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(x11)
BuildRequires : qemu

%description


%package bin
Summary: bin components for the gdk-pixbuf package.
Group: Binaries
Requires: gdk-pixbuf-data

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
Requires: gdk-pixbuf-lib
Requires: gdk-pixbuf-bin
Requires: gdk-pixbuf-data
Provides: gdk-pixbuf-devel

%description dev
dev components for the gdk-pixbuf package.


%package dev32
Summary: dev32 components for the gdk-pixbuf package.
Group: Default
Requires: gdk-pixbuf-lib32
Requires: gdk-pixbuf-bin
Requires: gdk-pixbuf-data
Requires: gdk-pixbuf-dev

%description dev32
dev32 components for the gdk-pixbuf package.


%package doc
Summary: doc components for the gdk-pixbuf package.
Group: Documentation

%description doc
doc components for the gdk-pixbuf package.


%package lib
Summary: lib components for the gdk-pixbuf package.
Group: Libraries
Requires: gdk-pixbuf-data

%description lib
lib components for the gdk-pixbuf package.


%package lib32
Summary: lib32 components for the gdk-pixbuf package.
Group: Default
Requires: gdk-pixbuf-data

%description lib32
lib32 components for the gdk-pixbuf package.


%package locales
Summary: locales components for the gdk-pixbuf package.
Group: Default

%description locales
locales components for the gdk-pixbuf package.


%prep
%setup -q -n gdk-pixbuf-2.36.5
pushd ..
cp -a gdk-pixbuf-2.36.5 build32
popd

%build
export LANG=C
export SOURCE_DATE_EPOCH=1487353306
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition -fstack-protector-strong "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition -fstack-protector-strong "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition -fstack-protector-strong "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition -fstack-protector-strong "
%configure --disable-static --enable-introspection \
--disable-installed-tests \
--enable-nls \
--disable-gio-sniffing \
--with-libjpeg \
--without-libjasper \
--with-libpng \
--without-libtiff \
--with-x11 \
--disable-static
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static --enable-introspection \
--disable-installed-tests \
--enable-nls \
--disable-gio-sniffing \
--with-libjpeg \
--without-libjasper \
--with-libpng \
--without-libtiff \
--with-x11 \
--disable-static   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1487353306
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
%find_lang gdk-pixbuf
## make_install_append content
cp %{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/lib*svg*.so %{buildroot}%{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/. ; LD_LIBRARY_PATH=%{buildroot}%{_libdir} %{buildroot}%{_bindir}/gdk-pixbuf-query-loaders %{buildroot}%{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/lib*.so | sed "s@%{buildroot}@@g" > %{buildroot}%{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders.cache ; rm %{buildroot}%{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/lib*svg*.so; sed -e 's/lib64/lib32/g' %{buildroot}%{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders.cache > %{buildroot}/usr/lib32/gdk-pixbuf-2.0/2.10.0/loaders.cache
## make_install_append end

%files
%defattr(-,root,root,-)
/usr/lib32/gdk-pixbuf-2.0/2.10.0/loaders.cache
/usr/lib32/girepository-1.0/GdkPixbuf-2.0.typelib
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders.cache

%files bin
%defattr(-,root,root,-)
/usr/bin/gdk-pixbuf-csource
/usr/bin/gdk-pixbuf-pixdata
/usr/bin/gdk-pixbuf-query-loaders
/usr/bin/gdk-pixbuf-thumbnailer

%files data
%defattr(-,root,root,-)
/usr/share/thumbnailers/gdk-pixbuf-thumbnailer.thumbnailer

%files dev
%defattr(-,root,root,-)
/usr/include/gdk-pixbuf-2.0/gdk-pixbuf-xlib/gdk-pixbuf-xlib.h
/usr/include/gdk-pixbuf-2.0/gdk-pixbuf-xlib/gdk-pixbuf-xlibrgb.h
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
/usr/lib64/girepository-1.0/GdkPixbuf-2.0.typelib
/usr/lib64/libgdk_pixbuf-2.0.so
/usr/lib64/libgdk_pixbuf_xlib-2.0.so
/usr/lib64/pkgconfig/gdk-pixbuf-2.0.pc
/usr/lib64/pkgconfig/gdk-pixbuf-xlib-2.0.pc
/usr/share/gir-1.0/*.gir

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libgdk_pixbuf-2.0.so
/usr/lib32/libgdk_pixbuf_xlib-2.0.so
/usr/lib32/pkgconfig/32gdk-pixbuf-2.0.pc
/usr/lib32/pkgconfig/32gdk-pixbuf-xlib-2.0.pc
/usr/lib32/pkgconfig/gdk-pixbuf-2.0.pc
/usr/lib32/pkgconfig/gdk-pixbuf-xlib-2.0.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
/usr/share/gtk-doc/html/gdk-pixbuf/GdkPixbufLoader.html
/usr/share/gtk-doc/html/gdk-pixbuf/annotation-glossary.html
/usr/share/gtk-doc/html/gdk-pixbuf/api-index-2-12.html
/usr/share/gtk-doc/html/gdk-pixbuf/api-index-2-14.html
/usr/share/gtk-doc/html/gdk-pixbuf/api-index-2-2.html
/usr/share/gtk-doc/html/gdk-pixbuf/api-index-2-26.html
/usr/share/gtk-doc/html/gdk-pixbuf/api-index-2-28.html
/usr/share/gtk-doc/html/gdk-pixbuf/api-index-2-30.html
/usr/share/gtk-doc/html/gdk-pixbuf/api-index-2-32.html
/usr/share/gtk-doc/html/gdk-pixbuf/api-index-2-36.html
/usr/share/gtk-doc/html/gdk-pixbuf/api-index-2-4.html
/usr/share/gtk-doc/html/gdk-pixbuf/api-index-2-6.html
/usr/share/gtk-doc/html/gdk-pixbuf/api-index-2-8.html
/usr/share/gtk-doc/html/gdk-pixbuf/api-index-deprecated.html
/usr/share/gtk-doc/html/gdk-pixbuf/api-index-full.html
/usr/share/gtk-doc/html/gdk-pixbuf/composite.png
/usr/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-Animations.html
/usr/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-File-Loading.html
/usr/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-File-saving.html
/usr/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-Image-Data-in-Memory.html
/usr/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-Inline-data.html
/usr/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-Module-Interface.html
/usr/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-Reference-Counting-and-Memory-Mangement.html
/usr/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-Scaling.html
/usr/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-The-GdkPixbuf-Structure.html
/usr/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-Utilities.html
/usr/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-Versioning.html
/usr/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-X-Drawables-to-Pixbufs.html
/usr/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-Xlib-Rendering.html
/usr/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-XlibRGB.html
/usr/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-csource.html
/usr/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-gdk-pixbuf-Xlib-initialization.html
/usr/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-gdk-pixbuf-from-drawables.html
/usr/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-gdk-pixbuf-rendering.html
/usr/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-query-loaders.html
/usr/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf.devhelp2
/usr/share/gtk-doc/html/gdk-pixbuf/home.png
/usr/share/gtk-doc/html/gdk-pixbuf/index.html
/usr/share/gtk-doc/html/gdk-pixbuf/left-insensitive.png
/usr/share/gtk-doc/html/gdk-pixbuf/left.png
/usr/share/gtk-doc/html/gdk-pixbuf/license.html
/usr/share/gtk-doc/html/gdk-pixbuf/right-insensitive.png
/usr/share/gtk-doc/html/gdk-pixbuf/right.png
/usr/share/gtk-doc/html/gdk-pixbuf/rn01.html
/usr/share/gtk-doc/html/gdk-pixbuf/rn02.html
/usr/share/gtk-doc/html/gdk-pixbuf/style.css
/usr/share/gtk-doc/html/gdk-pixbuf/up-insensitive.png
/usr/share/gtk-doc/html/gdk-pixbuf/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-ani.so
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-bmp.so
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-gif.so
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-icns.so
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-ico.so
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-jpeg.so
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-png.so
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-pnm.so
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-qtif.so
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-tga.so
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-xbm.so
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-xpm.so
/usr/lib64/libgdk_pixbuf-2.0.so.0
/usr/lib64/libgdk_pixbuf-2.0.so.0.3600.5
/usr/lib64/libgdk_pixbuf_xlib-2.0.so.0
/usr/lib64/libgdk_pixbuf_xlib-2.0.so.0.3600.5

%files lib32
%defattr(-,root,root,-)
/usr/lib32/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-ani.so
/usr/lib32/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-bmp.so
/usr/lib32/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-gif.so
/usr/lib32/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-icns.so
/usr/lib32/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-ico.so
/usr/lib32/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-jpeg.so
/usr/lib32/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-png.so
/usr/lib32/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-pnm.so
/usr/lib32/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-qtif.so
/usr/lib32/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-tga.so
/usr/lib32/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-xbm.so
/usr/lib32/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-xpm.so
/usr/lib32/libgdk_pixbuf-2.0.so.0
/usr/lib32/libgdk_pixbuf-2.0.so.0.3600.5
/usr/lib32/libgdk_pixbuf_xlib-2.0.so.0
/usr/lib32/libgdk_pixbuf_xlib-2.0.so.0.3600.5

%files locales -f gdk-pixbuf.lang
%defattr(-,root,root,-)

