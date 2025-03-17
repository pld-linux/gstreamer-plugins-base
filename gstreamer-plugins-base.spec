# TODO: install_plugins_helper
#
# Conditional build:
%bcond_without	apidocs		# hotdoc based API documentation (requires opengl library enabled)
%bcond_without	libvisual	# libvisual plugin
%bcond_without	opengl		# OpenGL support (gstgl library and opengl plugin)
%bcond_without	tremor		# ivorbisdec plugin (Tremor integer Ogg Vorbis decoder)

%define		gstname		gst-plugins-base
%define		gstmver		1.0
%define		gst_ver		1.26.0

Summary:	GStreamer Streaming-media framework base plugins
Summary(pl.UTF-8):	Podstawowe wtyczki do środowiska obróbki strumieni GStreamer
Name:		gstreamer-plugins-base
Version:	1.26.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	https://gstreamer.freedesktop.org/src/gst-plugins-base/%{gstname}-%{version}.tar.xz
# Source0-md5:	6a05a446e974ea4707c5a596424a5312
URL:		https://gstreamer.freedesktop.org/
%{?with_apidocs:BuildRequires:	docbook-dtd412-xml}
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	glib2-devel >= 1:2.64.0
%if %(locale -a | grep -q '^C.UTF-8$'; echo $?)
BuildRequires:	glibc-localedb-all
%endif
BuildRequires:	glibc-misc
BuildRequires:	gobject-introspection-devel >= 1.31.1
BuildRequires:	gstreamer-devel >= %{gst_ver}
BuildRequires:	gtk+3-devel >= 3.10
%{?with_apidocs:BuildRequires:	hotdoc >= 0.11.0}
BuildRequires:	iso-codes
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	meson >= 1.4
BuildRequires:	ninja >= 1.5
BuildRequires:	orc-devel >= 0.4.41
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	python3 >= 1:3.2
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
##
## plugins
##
BuildRequires:	alsa-lib-devel >= 1.0.11
BuildRequires:	cdparanoia-III-devel >= 2:10.2
BuildRequires:	libogg-devel >= 2:1.0
BuildRequires:	libtheora-devel >= 1.1
%{?with_libvisual:BuildRequires:	libvisual-devel >= 0.4.0}
BuildRequires:	libvorbis-devel >= 1:1.3.1
BuildRequires:	opus-devel >= 0.9.4
BuildRequires:	pango-devel >= 1:1.22.0
%{?with_tremor:BuildRequires:	tremor-devel}
BuildRequires:	udev-glib-devel >= 1:143
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXv-devel
%if %{with opengl}
BuildRequires:	EGL-devel
BuildRequires:	Mesa-libgbm-devel
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	OpenGLESv2-devel
# examples only: clutter clutter-glx clutter-x11
#BuildRequires:	SDL-devel >= 1.2.0 clutter-devel >= 1.8 xorg-lib-libXcomposite-devel
BuildRequires:	graphene-devel >= 1.4.0
BuildRequires:	libdrm-devel >= 2.4.98
BuildRequires:	libpng-devel >= 1.0
BuildRequires:	libjpeg-devel
BuildRequires:	udev-glib-devel >= 1:147
# wayland-client >= 1.11, wayland-cursor >= 1.0
BuildRequires:	wayland-devel >= 1.11
BuildRequires:	wayland-egl-devel >= 1.0
BuildRequires:	wayland-protocols >= 1.15
%endif
# old GIR format
BuildConflicts:	gstreamer-plugins-base-devel < 0.10.30
Requires:	glib2 >= 1:2.64.0
Requires:	gstreamer >= %{gst_ver}
Requires:	orc >= 0.4.41
Suggests:	iso-codes
# here go all the obsoleted gstreamer plugins
Obsoletes:	gstreamer-SDL < 0.10
Obsoletes:	gstreamer-artsd < 0.10
Obsoletes:	gstreamer-audio-effects < 0.10
Obsoletes:	gstreamer-audiofile < 0.10
Obsoletes:	gstreamer-audiosink-esd < 1.0
Obsoletes:	gstreamer-avi < 0.10
Obsoletes:	gstreamer-cdplayer < 0.10
Obsoletes:	gstreamer-colorspace < 0.10
Obsoletes:	gstreamer-daala < 1.16
Obsoletes:	gstreamer-divx < 1.0
Obsoletes:	gstreamer-festival < 0.10
Obsoletes:	gstreamer-hal < 1.0
Obsoletes:	gstreamer-interfaces < 0.10
Obsoletes:	gstreamer-interleave < 0.10
Obsoletes:	gstreamer-kate < 1.24
Obsoletes:	gstreamer-kio < 0.10
Obsoletes:	gstreamer-libdvdnav < 0.10
Obsoletes:	gstreamer-libfame < 0.10
Obsoletes:	gstreamer-media-info < 0.10
Obsoletes:	gstreamer-mikmod < 0.10
Obsoletes:	gstreamer-mimic < 1.12
Obsoletes:	gstreamer-misc < 0.8-1
Obsoletes:	gstreamer-musicbrainz < 1.0
Obsoletes:	gstreamer-mythtv < 1.0
Obsoletes:	gstreamer-oneton < 0.10
Obsoletes:	gstreamer-play < 0.10
Obsoletes:	gstreamer-plugins < 0.10
Obsoletes:	gstreamer-qcam < 0.10
Obsoletes:	gstreamer-sdl < 1.0
Obsoletes:	gstreamer-snapshot < 0.10
Obsoletes:	gstreamer-swfdec < 1.2
Obsoletes:	gstreamer-tcp < 0.10
Obsoletes:	gstreamer-timidity < 1.0
Obsoletes:	gstreamer-tuner < 0.10
Obsoletes:	gstreamer-v4l < 0.10
Obsoletes:	gstreamer-vbidec < 0.10
Obsoletes:	gstreamer-video4linux < 1.0
Obsoletes:	gstreamer-videosink-xv < 0.10
Obsoletes:	gstreamer-videotest < 0.10
Obsoletes:	gstreamer-xine < 0.10
Obsoletes:	gstreamer-xoverlay < 0.10
Obsoletes:	gstreamer-xvid < 1.0
Obsoletes:	gstreamer-yuv4mjpeg < 0.10
Obsoletes:	gtk-loaders-gstreamer < 0.10
# compositor plugin used to be in -plugins-bad 1.14.x
Conflicts:	gstreamer-plugins-bad < 1.16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		gstlibdir 	%{_libdir}/gstreamer-%{gstmver}
%define		gstincludedir	%{_includedir}/gstreamer-%{gstmver}

%description
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related. Its plugin-based architecture means
that new data types or processing capabilities can be added simply by
installing new plugins.

%description -l pl.UTF-8
GStreamer to środowisko obróbki danych strumieniowych, bazujące na
grafie filtrów operujących na danych medialnych. Aplikacje używające
tej biblioteki mogą robić wszystko od przetwarzania dźwięku w czasie
rzeczywistym, do odtwarzania filmów i czegokolwiek innego związego z
mediami. Architektura bazująca na wtyczkach pozwala na łatwe dodawanie
nowych typów danych lub możliwości obróbki.

%package devel
Summary:	Include files for GStreamer streaming-media framework plugins
Summary(pl.UTF-8):	Pliki nagłówkowe do wtyczek środowiska obróbki strumieni GStreamer
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.64.0
Requires:	gstreamer-devel >= %{gst_ver}
Requires:	orc-devel >= 0.4.41
Obsoletes:	gstreamer-interfaces-devel < 0.10
Obsoletes:	gstreamer-media-info-devel < 0.10
Obsoletes:	gstreamer-mixer-devel < 0.10
Obsoletes:	gstreamer-navigation-devel < 0.10
Obsoletes:	gstreamer-play-devel < 0.10
Obsoletes:	gstreamer-plugins-devel < 0.10
Obsoletes:	gstreamer-tuner-devel < 0.10
Obsoletes:	gstreamer-xoverlay-devel < 0.10
# gst/video/gstvideoaggregator.h existed in -plugins-bad 1.14.x
Conflicts:	gstreamer-plugins-bad-devel < 1.16

%description devel
Include files for GStreamer streaming-media framework plugins.

%description devel -l pl.UTF-8
Pliki nagłówkowe do wtyczek środowiska obróbki strumieni GStreamer.

%package apidocs
Summary:	GStreamer streaming-media framework plugins API documentation
Summary(pl.UTF-8):	Dokumentacja API wtyczek środowiska obróbki strumieni GStreamer
Group:		Documentation
Requires:	gstreamer-apidocs >= 1.18
Obsoletes:	gstreamer-plugins-gl-apidocs < 1.0
BuildArch:	noarch

%description apidocs
GStreamer streaming-media framework plugins API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API wtyczek środowiska obróbki strumieni GStreamer.

%package -n gstreamer-gl-libs
Summary:	GStreamer OpenGL plugins library
Summary(pl.UTF-8):	Biblioteka wtyczek OpenGL dla GStreamera
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	graphene >= 1.4.0
Requires:	libdrm >= 2.4.98
Requires:	libpng >= 1.0
Requires:	udev-glib >= 1:147
Requires:	wayland >= 1.11
Conflicts:	gstreamer-plugins-bad < 1.14
Obsoletes:	gstreamer-imagesink-gl < 1.0
Obsoletes:	gstreamer-opengl < 1.14
Obsoletes:	gstreamer-plugins-gl < 1.0

%description -n gstreamer-gl-libs
OpenGL plugins library for GStreamer streaming media framework,
together with actual OpenGL plugin.

%description -n gstreamer-gl-libs -l pl.UTF-8
Biblioteka wtyczek OpenGL dla szkieletu strumieni multimedialnych
GStreamer wraz z właściwą wtyczką OpenGL.

%package -n gstreamer-gl-devel
Summary:	Header files for GStreamer OpenGL library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki GStreamera OpenGL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	EGL-devel
Requires:	Mesa-libgbm-devel
Requires:	OpenGL-GLX-devel
Requires:	OpenGLESv2-devel
Requires:	gstreamer-gl-libs = %{version}-%{release}
Requires:	udev-glib-devel >= 1:147
Requires:	wayland-devel >= 1.11
Requires:	wayland-egl-devel >= 1.0
Requires:	xorg-lib-libX11-devel
Conflicts:	gstreamer-plugins-bad-devel < 1.14
Obsoletes:	gstreamer-plugins-gl-devel < 1.0

%description -n gstreamer-gl-devel
Header files for GStreamer OpenGL library.

%description -n gstreamer-gl-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki GStreamera OpenGL.

##
## Plugins
##

%package -n gstreamer-audiosink-alsa
Summary:	GStreamer plugins for the ALSA sound architecture
Summary(pl.UTF-8):	Wtyczki GStreamera do obsługi architektury ALSA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	gstreamer-audiosink = %{version}
Obsoletes:	gstreamer-alsa < 0.10
Obsoletes:	gstreamer-audiosink-alsaspdif < 0.10.21

%description -n gstreamer-audiosink-alsa
Input and output plugin for the ALSA soundcard driver architecture.

%description -n gstreamer-audiosink-alsa -l pl.UTF-8
Wtyczka wejścia i wyjścia ze sterowników dźwiękowych architektury ALSA
do GStreamera.

%package -n gstreamer-audio-effects-base
Summary:	GStreamer base audio effects plugins
Summary(pl.UTF-8):	Podstawowe wtyczki efektów dźwiękowych do GStreamera
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	gstreamer-audio-effects < 0.10

%description -n gstreamer-audio-effects-base
GStreamer base audio effects plugins.

%description -n gstreamer-audio-effects-base -l pl.UTF-8
Podstawowe wtyczki efektów dźwiękowych do GStreamera.

%package -n gstreamer-cdparanoia
Summary:	GStreamer plugin for CD audio input using CDParanoia IV
Summary(pl.UTF-8):	Wtyczka do GStreamera odtwarzająca płyty CD-Audio przy użyciu CDParanoia IV
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cdparanoia-III-libs >= 2:10.2

%description -n gstreamer-cdparanoia
Plugin for ripping audio tracks using cdparanoia under GStreamer.

%description -n gstreamer-cdparanoia -l pl.UTF-8
Wtyczka do ripowania ścieżek dźwiękowych pod GStreamerem za pomocą
cdparanoia.

%package -n gstreamer-ivorbisdec
Summary:	GStreamer plugin for decoding Ogg Vorbis audio files using Tremor
Summary(pl.UTF-8):	Wtyczka GStreamera dekodująca pliki dźwiękowe Ogg Vorbis (przy użyciu Tremora)
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n gstreamer-ivorbisdec
Plugin for playing Ogg Vorbis audio files using Tremor.

%description -n gstreamer-ivorbisdec -l pl.UTF-8
Wtyczka do odtwarzania plików dźwiękowych Ogg Vorbis przy użyciu
Tremora.

%package -n gstreamer-libvisual
Summary:	GStreamer libvisual plugin
Summary(pl.UTF-8):	Wtyczka libvisual do GStreamera
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libvisual >= 0.4.0

%description -n gstreamer-libvisual
GStreamer libvisual plugin.

%description -n gstreamer-libvisual -l pl.UTF-8
Wtyczka libvisual do GStreamera.

%package -n gstreamer-opus
Summary:	GStreamer OPUS plugins
Summary(pl.UTF-8):	Wtyczki OPUS do GStreamera
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	opus >= 0.9.4

%description -n gstreamer-opus
This package contains GStreamer plugins encoding/decoding OPUS codec
streams.

%description -n gstreamer-opus -l pl.UTF-8
Ten pakiet zawiera wtyczki do GStreamera obsługujące strumienie kodeka
OPUS.

%package -n gstreamer-pango
Summary:	GStreamer pango plugins
Summary(pl.UTF-8):	Wtyczki pango do GStreamera
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	pango >= 1:1.22.0

%description -n gstreamer-pango
This package contains textoverlay and timeoverlay GStreamer plugins.

%description -n gstreamer-pango -l pl.UTF-8
Ten pakiet zawiera wtyczki textoverlay i timeoverlay do GStreamera.

%package -n gstreamer-theora
Summary:	GStreamer Ogg Theora plugin
Summary(pl.UTF-8):	Wtyczka Ogg Theora do GStreamera
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libtheora >= 1.1

%description -n gstreamer-theora
GStreamer Ogg Theora plugin.

%description -n gstreamer-theora -l pl.UTF-8
Wtyczka Ogg Theora do GStreamera.

%package -n gstreamer-video4linux
Summary:	GStreamer plugin for Video 4 Linux source
Summary(pl.UTF-8):	Wtyczka GStreamera dla źródła Video 4 Linux
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	udev-glib >= 1:143

%description -n gstreamer-video4linux
GStreamer plugin for Video 4 Linux source.

%description -n gstreamer-video4linux -l pl.UTF-8
Wtyczka GStreamera dla źródła Video 4 Linux.

%package -n gstreamer-vorbis
Summary:	GStreamer plugin for encoding and decoding Ogg Vorbis audio files
Summary(pl.UTF-8):	Wtyczki do GStreamera kodujące i dekodujące pliki dźwiękowe Ogg Vorbis
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libvorbis >= 1:1.3.1

%description -n gstreamer-vorbis
Plugins for creating and playing Ogg Vorbis audio files.

%description -n gstreamer-vorbis -l pl.UTF-8
Wtyczki do tworzenia i odtwarzania plików dźwiękowych Ogg Vorbis.

%package -n gstreamer-imagesink-x
Summary:	GStreamer XFree86/X.org output plugin
Summary(pl.UTF-8):	Wtyczka wyjścia obrazu XFree86/X.org dla GStreamera
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	gstreamer-videosink = %{version}

%description -n gstreamer-imagesink-x
Standard XFree86/X.org image sink.

%description -n gstreamer-imagesink-x -l pl.UTF-8
Standardowa wtyczka wyjścia obrazu XFree86/X.org dla GStreamera.

%package -n gstreamer-imagesink-xv
Summary:	GStreamer Xvideo output plugin
Summary(pl.UTF-8):	Wtyczka wyjścia obrazu Xvideo dla GStreamera
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	gstreamer-videosink = %{version}

%description -n gstreamer-imagesink-xv
XFree86/X.org image sink via Xvideo extension.

%description -n gstreamer-imagesink-xv -l pl.UTF-8
Wtyczka wyjścia obrazu Xvideo dla GStreamera.

%prep
%setup -q -n %{gstname}-%{version}

%build
%meson \
	--default-library=shared \
	-Dadder=enabled \
	-Dalsa=enabled \
	-Dapp=enabled \
	-Daudioconvert=enabled \
	-Daudiomixer=enabled \
	-Daudiorate=enabled \
	-Daudioresample=enabled \
	-Daudiotestsrc=enabled \
	-Dcdparanoia=enabled \
	-Dcompositor=enabled \
	-Ddebugutils=enabled \
	-Ddoc=%{__enabled_disabled apidocs} \
	-Ddrm=enabled \
	-Ddsd=enabled \
	-Dencoding=enabled \
	-Dexamples=disabled \
	-Dgio=enabled \
	-Dgio-typefinder=enabled \
	-Dgl=%{__enabled_disabled opengl} \
	-Dgl-graphene=enabled \
	-Dgl-jpeg=enabled \
	-Dgl-png=enabled \
	-Dglib_assert=false \
	-Dglib_checks=false \
	-Dglib_debug=disabled \
	-Dintrospection=enabled \
	-Diso-codes=enabled \
	-Dlibvisual=%{__enabled_disabled libvisual} \
	-Dnls=enabled \
	-Dogg=enabled \
	-Dopus=enabled \
	-Dorc=enabled \
	-Doverlaycomposition=enabled \
	-Dpango=enabled \
	-Dpbtypes=enabled \
	-Dplayback=enabled \
	-Dqt5=enabled \
	-Drawparse=enabled \
	-Dsubparse=enabled \
	-Dtests=disabled \
	-Dtheora=enabled \
	-Dtools=enabled \
	-Dtremor=%{__enabled_disabled tremor} \
	-Dvideoconvertscale=enabled \
	-Dvideorate=enabled \
	-Dvideotestsrc=enabled \
	-Dvolume=enabled \
	-Dvorbis=enabled \
	-Dx11=enabled \
	-Dxi=enabled \
	-Dxshm=enabled \
	-Dxvideo=enabled

%meson_build

%if %{with apidocs}
%meson_build build-libs-hotdoc-configs build-hotdoc-configs

cd build/docs
for config in *-doc.json plugin-*.json ; do
	LC_ALL=C.UTF-8 hotdoc run --conf-file "$config"
done
%endif

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%if %{with apidocs}
install -d $RPM_BUILD_ROOT%{_docdir}/gstreamer-%{gstmver}
for d in build/docs/*-doc build/docs/plugin-* ; do
	[ ! -d "$d" ] || cp -pr "$d" $RPM_BUILD_ROOT%{_docdir}/gstreamer-%{gstmver}
done
%endif

%find_lang %{gstname}-%{gstmver}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	-n gstreamer-gl-libs -p /sbin/ldconfig
%postun	-n gstreamer-gl-libs -p /sbin/ldconfig

%files -f %{gstname}-%{gstmver}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README.md RELEASE
%attr(755,root,root) %{_bindir}/gst-device-monitor-%{gstmver}
%attr(755,root,root) %{_bindir}/gst-discoverer-%{gstmver}
%attr(755,root,root) %{_bindir}/gst-play-%{gstmver}
%attr(755,root,root) %{_libdir}/libgstallocators-%{gstmver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstallocators-%{gstmver}.so.0
%attr(755,root,root) %{_libdir}/libgstapp-%{gstmver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstapp-%{gstmver}.so.0
%attr(755,root,root) %{_libdir}/libgstaudio-%{gstmver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstaudio-%{gstmver}.so.0
%attr(755,root,root) %{_libdir}/libgstfft-%{gstmver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstfft-%{gstmver}.so.0
%attr(755,root,root) %{_libdir}/libgstpbutils-%{gstmver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstpbutils-%{gstmver}.so.0
%attr(755,root,root) %{_libdir}/libgstriff-%{gstmver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstriff-%{gstmver}.so.0
%attr(755,root,root) %{_libdir}/libgstrtp-%{gstmver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstrtp-%{gstmver}.so.0
%attr(755,root,root) %{_libdir}/libgstrtsp-%{gstmver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstrtsp-%{gstmver}.so.0
%attr(755,root,root) %{_libdir}/libgstsdp-%{gstmver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstsdp-%{gstmver}.so.0
%attr(755,root,root) %{_libdir}/libgsttag-%{gstmver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgsttag-%{gstmver}.so.0
%attr(755,root,root) %{_libdir}/libgstvideo-%{gstmver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstvideo-%{gstmver}.so.0
%{_mandir}/man1/gst-device-monitor-%{gstmver}.1*
%{_mandir}/man1/gst-discoverer-%{gstmver}.1*
%{_mandir}/man1/gst-play-%{gstmver}.1*
# plugins with no external dependencies
%attr(755,root,root) %{gstlibdir}/libgstapp.so
%attr(755,root,root) %{gstlibdir}/libgstaudioconvert.so
%attr(755,root,root) %{gstlibdir}/libgstaudiomixer.so
%attr(755,root,root) %{gstlibdir}/libgstaudiorate.so
%attr(755,root,root) %{gstlibdir}/libgstaudiotestsrc.so
%attr(755,root,root) %{gstlibdir}/libgstbasedebug.so
%attr(755,root,root) %{gstlibdir}/libgstcompositor.so
%attr(755,root,root) %{gstlibdir}/libgstdsd.so
%attr(755,root,root) %{gstlibdir}/libgstencoding.so
%attr(755,root,root) %{gstlibdir}/libgstgio.so
%attr(755,root,root) %{gstlibdir}/libgstoverlaycomposition.so
%attr(755,root,root) %{gstlibdir}/libgstpbtypes.so
%attr(755,root,root) %{gstlibdir}/libgstplayback.so
%attr(755,root,root) %{gstlibdir}/libgstrawparse.so
%attr(755,root,root) %{gstlibdir}/libgstsubparse.so
%attr(755,root,root) %{gstlibdir}/libgsttcp.so
%attr(755,root,root) %{gstlibdir}/libgsttypefindfunctions.so
%attr(755,root,root) %{gstlibdir}/libgstvideoconvertscale.so
%attr(755,root,root) %{gstlibdir}/libgstvideorate.so
%attr(755,root,root) %{gstlibdir}/libgstvideotestsrc.so
%{_libdir}/girepository-1.0/GstAllocators-%{gstmver}.typelib
%{_libdir}/girepository-1.0/GstApp-%{gstmver}.typelib
%{_libdir}/girepository-1.0/GstAudio-%{gstmver}.typelib
%{_libdir}/girepository-1.0/GstPbutils-%{gstmver}.typelib
%{_libdir}/girepository-1.0/GstRtp-%{gstmver}.typelib
%{_libdir}/girepository-1.0/GstRtsp-%{gstmver}.typelib
%{_libdir}/girepository-1.0/GstSdp-%{gstmver}.typelib
%{_libdir}/girepository-1.0/GstTag-%{gstmver}.typelib
%{_libdir}/girepository-1.0/GstVideo-%{gstmver}.typelib
%{_datadir}/gst-plugins-base

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgstallocators-%{gstmver}.so
%attr(755,root,root) %{_libdir}/libgstapp-%{gstmver}.so
%attr(755,root,root) %{_libdir}/libgstaudio-%{gstmver}.so
%attr(755,root,root) %{_libdir}/libgstfft-%{gstmver}.so
%attr(755,root,root) %{_libdir}/libgstpbutils-%{gstmver}.so
%attr(755,root,root) %{_libdir}/libgstriff-%{gstmver}.so
%attr(755,root,root) %{_libdir}/libgstrtp-%{gstmver}.so
%attr(755,root,root) %{_libdir}/libgstrtsp-%{gstmver}.so
%attr(755,root,root) %{_libdir}/libgstsdp-%{gstmver}.so
%attr(755,root,root) %{_libdir}/libgsttag-%{gstmver}.so
%attr(755,root,root) %{_libdir}/libgstvideo-%{gstmver}.so
%{gstincludedir}/gst/allocators
%{gstincludedir}/gst/app
%{gstincludedir}/gst/audio
%{gstincludedir}/gst/fft
%{gstincludedir}/gst/pbutils
%{gstincludedir}/gst/riff
%{gstincludedir}/gst/rtp
%{gstincludedir}/gst/rtsp
%{gstincludedir}/gst/sdp
%{gstincludedir}/gst/tag
%{gstincludedir}/gst/video
%{_pkgconfigdir}/gstreamer-allocators-%{gstmver}.pc
%{_pkgconfigdir}/gstreamer-app-%{gstmver}.pc
%{_pkgconfigdir}/gstreamer-audio-%{gstmver}.pc
%{_pkgconfigdir}/gstreamer-fft-%{gstmver}.pc
%{_pkgconfigdir}/gstreamer-pbutils-%{gstmver}.pc
%{_pkgconfigdir}/gstreamer-plugins-base-%{gstmver}.pc
%{_pkgconfigdir}/gstreamer-riff-%{gstmver}.pc
%{_pkgconfigdir}/gstreamer-rtp-%{gstmver}.pc
%{_pkgconfigdir}/gstreamer-rtsp-%{gstmver}.pc
%{_pkgconfigdir}/gstreamer-sdp-%{gstmver}.pc
%{_pkgconfigdir}/gstreamer-tag-%{gstmver}.pc
%{_pkgconfigdir}/gstreamer-video-%{gstmver}.pc
%{_datadir}/gir-1.0/GstAllocators-%{gstmver}.gir
%{_datadir}/gir-1.0/GstApp-%{gstmver}.gir
%{_datadir}/gir-1.0/GstAudio-%{gstmver}.gir
%{_datadir}/gir-1.0/GstPbutils-%{gstmver}.gir
%{_datadir}/gir-1.0/GstRtp-%{gstmver}.gir
%{_datadir}/gir-1.0/GstRtsp-%{gstmver}.gir
%{_datadir}/gir-1.0/GstSdp-%{gstmver}.gir
%{_datadir}/gir-1.0/GstTag-%{gstmver}.gir
%{_datadir}/gir-1.0/GstVideo-%{gstmver}.gir

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_docdir}/gstreamer-%{gstmver}/allocators-doc
%{_docdir}/gstreamer-%{gstmver}/applib-doc
%{_docdir}/gstreamer-%{gstmver}/audio-doc
%{_docdir}/gstreamer-%{gstmver}/gl-doc
%{_docdir}/gstreamer-%{gstmver}/gl-egl-doc
%{_docdir}/gstreamer-%{gstmver}/gl-wayland-doc
%{_docdir}/gstreamer-%{gstmver}/gl-x11-doc
%{_docdir}/gstreamer-%{gstmver}/pbutils-doc
%{_docdir}/gstreamer-%{gstmver}/riff-doc
%{_docdir}/gstreamer-%{gstmver}/rtplib-doc
%{_docdir}/gstreamer-%{gstmver}/rtsplib-doc
%{_docdir}/gstreamer-%{gstmver}/sdp-doc
%{_docdir}/gstreamer-%{gstmver}/tag-doc
%{_docdir}/gstreamer-%{gstmver}/video-doc
%{_docdir}/gstreamer-%{gstmver}/plugin-adder
%{_docdir}/gstreamer-%{gstmver}/plugin-alsa
%{_docdir}/gstreamer-%{gstmver}/plugin-app
%{_docdir}/gstreamer-%{gstmver}/plugin-audioconvert
%{_docdir}/gstreamer-%{gstmver}/plugin-audiomixer
%{_docdir}/gstreamer-%{gstmver}/plugin-audiorate
%{_docdir}/gstreamer-%{gstmver}/plugin-audioresample
%{_docdir}/gstreamer-%{gstmver}/plugin-audiotestsrc
%{_docdir}/gstreamer-%{gstmver}/plugin-basedebug
%{_docdir}/gstreamer-%{gstmver}/plugin-cdparanoia
%{_docdir}/gstreamer-%{gstmver}/plugin-compositor
%{_docdir}/gstreamer-%{gstmver}/plugin-dsd
%{_docdir}/gstreamer-%{gstmver}/plugin-encoding
%{_docdir}/gstreamer-%{gstmver}/plugin-gio
%{_docdir}/gstreamer-%{gstmver}/plugin-libvisual
%{_docdir}/gstreamer-%{gstmver}/plugin-ogg
%{_docdir}/gstreamer-%{gstmver}/plugin-opengl
%{_docdir}/gstreamer-%{gstmver}/plugin-opus
%{_docdir}/gstreamer-%{gstmver}/plugin-overlaycomposition
%{_docdir}/gstreamer-%{gstmver}/plugin-pango
%{_docdir}/gstreamer-%{gstmver}/plugin-pbtypes
%{_docdir}/gstreamer-%{gstmver}/plugin-playback
%{_docdir}/gstreamer-%{gstmver}/plugin-rawparse
%{_docdir}/gstreamer-%{gstmver}/plugin-subparse
%{_docdir}/gstreamer-%{gstmver}/plugin-tcp
%{_docdir}/gstreamer-%{gstmver}/plugin-theora
%{_docdir}/gstreamer-%{gstmver}/plugin-typefindfunctions
%{_docdir}/gstreamer-%{gstmver}/plugin-videoconvertscale
%{_docdir}/gstreamer-%{gstmver}/plugin-videorate
%{_docdir}/gstreamer-%{gstmver}/plugin-videotestsrc
%{_docdir}/gstreamer-%{gstmver}/plugin-volume
%{_docdir}/gstreamer-%{gstmver}/plugin-vorbis
%{_docdir}/gstreamer-%{gstmver}/plugin-ximagesink
%{_docdir}/gstreamer-%{gstmver}/plugin-xvimagesink
%endif

%if %{with opengl}
%files -n gstreamer-gl-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgstgl-%{gstmver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstgl-%{gstmver}.so.0
%{_libdir}/girepository-1.0/GstGL-%{gstmver}.typelib
%{_libdir}/girepository-1.0/GstGLEGL-%{gstmver}.typelib
%{_libdir}/girepository-1.0/GstGLWayland-%{gstmver}.typelib
%{_libdir}/girepository-1.0/GstGLX11-%{gstmver}.typelib
# plugin itself
%attr(755,root,root) %{gstlibdir}/libgstopengl.so

%files -n gstreamer-gl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgstgl-%{gstmver}.so
# currently only gl lib provides header in this location, so package top dirs here
%dir %{gstlibdir}/include
%dir %{gstlibdir}/include/gst
%{gstlibdir}/include/gst/gl
%{gstincludedir}/gst/gl
%{_datadir}/gir-1.0/GstGL-%{gstmver}.gir
%{_datadir}/gir-1.0/GstGLEGL-%{gstmver}.gir
%{_datadir}/gir-1.0/GstGLWayland-%{gstmver}.gir
%{_datadir}/gir-1.0/GstGLX11-%{gstmver}.gir
%{_pkgconfigdir}/gstreamer-gl-%{gstmver}.pc
%{_pkgconfigdir}/gstreamer-gl-egl-%{gstmver}.pc
%{_pkgconfigdir}/gstreamer-gl-prototypes-%{gstmver}.pc
%{_pkgconfigdir}/gstreamer-gl-wayland-%{gstmver}.pc
%{_pkgconfigdir}/gstreamer-gl-x11-%{gstmver}.pc
%endif

##
## Plugins
##

%files -n gstreamer-audiosink-alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstalsa.so

%files -n gstreamer-audio-effects-base
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstadder.so
%attr(755,root,root) %{gstlibdir}/libgstaudioresample.so
%attr(755,root,root) %{gstlibdir}/libgstvolume.so

%files -n gstreamer-cdparanoia
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstcdparanoia.so

%if %{with tremor}
%files -n gstreamer-ivorbisdec
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstivorbisdec.so
%endif

%if %{with libvisual}
%files -n gstreamer-libvisual
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstlibvisual.so
%endif

%files -n gstreamer-opus
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstopus.so

%files -n gstreamer-pango
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstpango.so

%files -n gstreamer-theora
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgsttheora.so

%files -n gstreamer-vorbis
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstvorbis.so
%attr(755,root,root) %{gstlibdir}/libgstogg.so

%files -n gstreamer-imagesink-x
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstximagesink.so

%files -n gstreamer-imagesink-xv
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstxvimagesink.so
