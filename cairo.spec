#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cairo
Version  : 1.14.12
Release  : 52
URL      : https://www.cairographics.org/releases/cairo-1.14.12.tar.xz
Source0  : https://www.cairographics.org/releases/cairo-1.14.12.tar.xz
Summary  : Multi-platform 2D graphics library
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 MIT MPL-1.1
Requires: cairo-bin
Requires: cairo-lib
Requires: cairo-doc
BuildRequires : docbook-xml
BuildRequires : freetype-dev32
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glib-dev32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : grep
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libXrender-dev
BuildRequires : libXrender-dev32
BuildRequires : libjpeg-turbo-dev
BuildRequires : libjpeg-turbo-dev32
BuildRequires : libpng-dev
BuildRequires : libpng-dev32
BuildRequires : librsvg-dev
BuildRequires : librsvg-dev32
BuildRequires : libxcb-dev
BuildRequires : libxcb-dev32
BuildRequires : libxslt-bin
BuildRequires : mesa-dev
BuildRequires : mesa-dev32
BuildRequires : pkgconfig(32fontconfig)
BuildRequires : pkgconfig(32glib-2.0)
BuildRequires : pkgconfig(32ice)
BuildRequires : pkgconfig(32pixman-1)
BuildRequires : pkgconfig(32x11)
BuildRequires : pkgconfig(32xcb)
BuildRequires : pkgconfig(32xext)
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(pixman-1)
BuildRequires : pkgconfig(valgrind)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)
BuildRequires : systemd-dev
BuildRequires : systemd-dev32
BuildRequires : zlib-dev32
Patch1: cve-2016-9082.patch
Patch2: madvise.patch

%description
Cairo - Multi-platform 2D graphics library
http://cairographics.org
What is cairo
=============
Cairo is a 2D graphics library with support for multiple output
devices. Currently supported output targets include the X Window
System (via both Xlib and XCB), quartz, win32, and image buffers,
as well as PDF, PostScript, and SVG file output. Experimental backends
include OpenGL, BeOS, OS/2, and DirectFB.

%package bin
Summary: bin components for the cairo package.
Group: Binaries

%description bin
bin components for the cairo package.


%package dev
Summary: dev components for the cairo package.
Group: Development
Requires: cairo-lib
Requires: cairo-bin
Provides: cairo-devel

%description dev
dev components for the cairo package.


%package dev32
Summary: dev32 components for the cairo package.
Group: Default
Requires: cairo-lib32
Requires: cairo-bin
Requires: cairo-dev

%description dev32
dev32 components for the cairo package.


%package doc
Summary: doc components for the cairo package.
Group: Documentation

%description doc
doc components for the cairo package.


%package lib
Summary: lib components for the cairo package.
Group: Libraries

%description lib
lib components for the cairo package.


%package lib32
Summary: lib32 components for the cairo package.
Group: Default

%description lib32
lib32 components for the cairo package.


%prep
%setup -q -n cairo-1.14.12
%patch1 -p1
%patch2 -p1
pushd ..
cp -a cairo-1.14.12 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1512654240
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong "
%configure --disable-static --disable-gtk-doc --enable-xlib=yes --enable-xcb=yes --enable-ft=yes --enable-fc=yes --enable-gl --enable-xlib-xcb
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static --disable-gtk-doc --enable-xlib=yes --enable-xcb=yes --enable-ft=yes --enable-fc=yes --enable-gl --enable-xlib-xcb   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%install
export SOURCE_DATE_EPOCH=1512654240
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

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cairo-trace

%files dev
%defattr(-,root,root,-)
/usr/include/cairo/cairo-deprecated.h
/usr/include/cairo/cairo-features.h
/usr/include/cairo/cairo-ft.h
/usr/include/cairo/cairo-gl.h
/usr/include/cairo/cairo-gobject.h
/usr/include/cairo/cairo-pdf.h
/usr/include/cairo/cairo-ps.h
/usr/include/cairo/cairo-script-interpreter.h
/usr/include/cairo/cairo-script.h
/usr/include/cairo/cairo-svg.h
/usr/include/cairo/cairo-version.h
/usr/include/cairo/cairo-xcb.h
/usr/include/cairo/cairo-xlib-xrender.h
/usr/include/cairo/cairo-xlib.h
/usr/include/cairo/cairo.h
/usr/lib64/libcairo-gobject.so
/usr/lib64/libcairo-script-interpreter.so
/usr/lib64/libcairo.so
/usr/lib64/pkgconfig/cairo-egl.pc
/usr/lib64/pkgconfig/cairo-fc.pc
/usr/lib64/pkgconfig/cairo-ft.pc
/usr/lib64/pkgconfig/cairo-gl.pc
/usr/lib64/pkgconfig/cairo-glx.pc
/usr/lib64/pkgconfig/cairo-gobject.pc
/usr/lib64/pkgconfig/cairo-pdf.pc
/usr/lib64/pkgconfig/cairo-png.pc
/usr/lib64/pkgconfig/cairo-ps.pc
/usr/lib64/pkgconfig/cairo-script.pc
/usr/lib64/pkgconfig/cairo-svg.pc
/usr/lib64/pkgconfig/cairo-xcb-shm.pc
/usr/lib64/pkgconfig/cairo-xcb.pc
/usr/lib64/pkgconfig/cairo-xlib-xcb.pc
/usr/lib64/pkgconfig/cairo-xlib-xrender.pc
/usr/lib64/pkgconfig/cairo-xlib.pc
/usr/lib64/pkgconfig/cairo.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libcairo-gobject.so
/usr/lib32/libcairo-script-interpreter.so
/usr/lib32/libcairo.so
/usr/lib32/pkgconfig/32cairo-egl.pc
/usr/lib32/pkgconfig/32cairo-fc.pc
/usr/lib32/pkgconfig/32cairo-ft.pc
/usr/lib32/pkgconfig/32cairo-gl.pc
/usr/lib32/pkgconfig/32cairo-glx.pc
/usr/lib32/pkgconfig/32cairo-gobject.pc
/usr/lib32/pkgconfig/32cairo-pdf.pc
/usr/lib32/pkgconfig/32cairo-png.pc
/usr/lib32/pkgconfig/32cairo-ps.pc
/usr/lib32/pkgconfig/32cairo-script.pc
/usr/lib32/pkgconfig/32cairo-svg.pc
/usr/lib32/pkgconfig/32cairo-xcb-shm.pc
/usr/lib32/pkgconfig/32cairo-xcb.pc
/usr/lib32/pkgconfig/32cairo-xlib-xcb.pc
/usr/lib32/pkgconfig/32cairo-xlib-xrender.pc
/usr/lib32/pkgconfig/32cairo-xlib.pc
/usr/lib32/pkgconfig/32cairo.pc
/usr/lib32/pkgconfig/cairo-egl.pc
/usr/lib32/pkgconfig/cairo-fc.pc
/usr/lib32/pkgconfig/cairo-ft.pc
/usr/lib32/pkgconfig/cairo-gl.pc
/usr/lib32/pkgconfig/cairo-glx.pc
/usr/lib32/pkgconfig/cairo-gobject.pc
/usr/lib32/pkgconfig/cairo-pdf.pc
/usr/lib32/pkgconfig/cairo-png.pc
/usr/lib32/pkgconfig/cairo-ps.pc
/usr/lib32/pkgconfig/cairo-script.pc
/usr/lib32/pkgconfig/cairo-svg.pc
/usr/lib32/pkgconfig/cairo-xcb-shm.pc
/usr/lib32/pkgconfig/cairo-xcb.pc
/usr/lib32/pkgconfig/cairo-xlib-xcb.pc
/usr/lib32/pkgconfig/cairo-xlib-xrender.pc
/usr/lib32/pkgconfig/cairo-xlib.pc
/usr/lib32/pkgconfig/cairo.pc

%files doc
%defattr(-,root,root,-)
/usr/share/gtk-doc/html/cairo/bindings-errors.html
/usr/share/gtk-doc/html/cairo/bindings-fonts.html
/usr/share/gtk-doc/html/cairo/bindings-memory.html
/usr/share/gtk-doc/html/cairo/bindings-overloading.html
/usr/share/gtk-doc/html/cairo/bindings-path.html
/usr/share/gtk-doc/html/cairo/bindings-patterns.html
/usr/share/gtk-doc/html/cairo/bindings-return-values.html
/usr/share/gtk-doc/html/cairo/bindings-streams.html
/usr/share/gtk-doc/html/cairo/bindings-surfaces.html
/usr/share/gtk-doc/html/cairo/cairo-Error-handling.html
/usr/share/gtk-doc/html/cairo/cairo-FreeType-Fonts.html
/usr/share/gtk-doc/html/cairo/cairo-Image-Surfaces.html
/usr/share/gtk-doc/html/cairo/cairo-PDF-Surfaces.html
/usr/share/gtk-doc/html/cairo/cairo-PNG-Support.html
/usr/share/gtk-doc/html/cairo/cairo-Paths.html
/usr/share/gtk-doc/html/cairo/cairo-PostScript-Surfaces.html
/usr/share/gtk-doc/html/cairo/cairo-Quartz-(CGFont)-Fonts.html
/usr/share/gtk-doc/html/cairo/cairo-Quartz-Surfaces.html
/usr/share/gtk-doc/html/cairo/cairo-Raster-Sources.html
/usr/share/gtk-doc/html/cairo/cairo-Recording-Surfaces.html
/usr/share/gtk-doc/html/cairo/cairo-Regions.html
/usr/share/gtk-doc/html/cairo/cairo-SVG-Surfaces.html
/usr/share/gtk-doc/html/cairo/cairo-Script-Surfaces.html
/usr/share/gtk-doc/html/cairo/cairo-Transformations.html
/usr/share/gtk-doc/html/cairo/cairo-Types.html
/usr/share/gtk-doc/html/cairo/cairo-User-Fonts.html
/usr/share/gtk-doc/html/cairo/cairo-Version-Information.html
/usr/share/gtk-doc/html/cairo/cairo-Win32-Fonts.html
/usr/share/gtk-doc/html/cairo/cairo-Win32-Surfaces.html
/usr/share/gtk-doc/html/cairo/cairo-XCB-Surfaces.html
/usr/share/gtk-doc/html/cairo/cairo-XLib-Surfaces.html
/usr/share/gtk-doc/html/cairo/cairo-XLib-XRender-Backend.html
/usr/share/gtk-doc/html/cairo/cairo-cairo-device-t.html
/usr/share/gtk-doc/html/cairo/cairo-cairo-font-face-t.html
/usr/share/gtk-doc/html/cairo/cairo-cairo-font-options-t.html
/usr/share/gtk-doc/html/cairo/cairo-cairo-matrix-t.html
/usr/share/gtk-doc/html/cairo/cairo-cairo-pattern-t.html
/usr/share/gtk-doc/html/cairo/cairo-cairo-scaled-font-t.html
/usr/share/gtk-doc/html/cairo/cairo-cairo-surface-t.html
/usr/share/gtk-doc/html/cairo/cairo-cairo-t.html
/usr/share/gtk-doc/html/cairo/cairo-drawing.html
/usr/share/gtk-doc/html/cairo/cairo-fonts.html
/usr/share/gtk-doc/html/cairo/cairo-support.html
/usr/share/gtk-doc/html/cairo/cairo-surfaces.html
/usr/share/gtk-doc/html/cairo/cairo-text.html
/usr/share/gtk-doc/html/cairo/cairo.devhelp2
/usr/share/gtk-doc/html/cairo/home.png
/usr/share/gtk-doc/html/cairo/index-1.10.html
/usr/share/gtk-doc/html/cairo/index-1.12.html
/usr/share/gtk-doc/html/cairo/index-1.14.html
/usr/share/gtk-doc/html/cairo/index-1.2.html
/usr/share/gtk-doc/html/cairo/index-1.4.html
/usr/share/gtk-doc/html/cairo/index-1.6.html
/usr/share/gtk-doc/html/cairo/index-1.8.html
/usr/share/gtk-doc/html/cairo/index-all.html
/usr/share/gtk-doc/html/cairo/index.html
/usr/share/gtk-doc/html/cairo/language-bindings.html
/usr/share/gtk-doc/html/cairo/left-insensitive.png
/usr/share/gtk-doc/html/cairo/left.png
/usr/share/gtk-doc/html/cairo/right-insensitive.png
/usr/share/gtk-doc/html/cairo/right.png
/usr/share/gtk-doc/html/cairo/style.css
/usr/share/gtk-doc/html/cairo/up-insensitive.png
/usr/share/gtk-doc/html/cairo/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/cairo/libcairo-trace.so
/usr/lib64/cairo/libcairo-trace.so.0
/usr/lib64/cairo/libcairo-trace.so.0.0.0
/usr/lib64/libcairo-gobject.so.2
/usr/lib64/libcairo-gobject.so.2.11400.12
/usr/lib64/libcairo-script-interpreter.so.2
/usr/lib64/libcairo-script-interpreter.so.2.11400.12
/usr/lib64/libcairo.so.2
/usr/lib64/libcairo.so.2.11400.12

%files lib32
%defattr(-,root,root,-)
/usr/lib32/cairo/libcairo-trace.so
/usr/lib32/cairo/libcairo-trace.so.0
/usr/lib32/cairo/libcairo-trace.so.0.0.0
/usr/lib32/libcairo-gobject.so.2
/usr/lib32/libcairo-gobject.so.2.11400.12
/usr/lib32/libcairo-script-interpreter.so.2
/usr/lib32/libcairo-script-interpreter.so.2.11400.12
/usr/lib32/libcairo.so.2
/usr/lib32/libcairo.so.2.11400.12
