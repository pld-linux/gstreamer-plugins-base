#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc
%bcond_without	libvisual	# don't build libvisual plugin
%bcond_without	tremor		# ivorbisdec plugin (Tremor integer Ogg Vorbis decoder)
%bcond_with	v4l1		# Video4Linux 1 plugin (for Linux < 2.6.35 or so)

%define		gstname		gst-plugins-base
%define		vmajor		1.0
%define		gst_req_ver	1.8.0

Summary:	GStreamer Streaming-media framework base plugins
Summary(pl.UTF-8):	Podstawowe wtyczki do środowiska obróbki strumieni GStreamer
Name:		gstreamer-plugins-base
Version:	1.8.0
Release:	2
License:	LGPL v2+
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/gst-plugins-base/%{gstname}-%{version}.tar.xz
# Source0-md5:	20cc8231609318310f2a55f64c86cbb4
URL:		http://gstreamer.freedesktop.org/
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.14
%{?with_apidocs:BuildRequires:	docbook-dtd412-xml}
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	glib2-devel >= 1:2.40
BuildRequires:	glibc-misc
BuildRequires:	gobject-introspection-devel >= 1.31.1
BuildRequires:	gstreamer-devel >= %{gst_req_ver}
BuildRequires:	gtk+3-devel >= 3.10
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.12}
BuildRequires:	iso-codes
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	orc-devel >= 0.4.23
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	python >= 2.1
BuildRequires:	tar >= 1:1.22
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
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	opus-devel >= 0.9.4
BuildRequires:	pango-devel >= 1:1.22.0
BuildRequires:	rpmbuild(macros) >= 1.98
%{?with_tremor:BuildRequires:	tremor-devel}
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXv-devel
# old GIR format
BuildConflicts:	gstreamer-plugins-base-devel < 0.10.30
Requires:	glib2 >= 1:2.40
Requires:	gstreamer >= %{gst_req_ver}
Requires:	orc >= 0.4.23
Suggests:	iso-codes
# here go all the obsoleted gstreamer plugins
Obsoletes:	gstreamer-artsd
Obsoletes:	gstreamer-audio-effects
Obsoletes:	gstreamer-audiofile
Obsoletes:	gstreamer-audiosink-esd
Obsoletes:	gstreamer-avi
Obsoletes:	gstreamer-cdplayer
Obsoletes:	gstreamer-colorspace
Obsoletes:	gstreamer-festival
Obsoletes:	gstreamer-hal
Obsoletes:	gstreamer-interfaces
Obsoletes:	gstreamer-interleave
Obsoletes:	gstreamer-kio
Obsoletes:	gstreamer-libdvdnav
Obsoletes:	gstreamer-libfame
Obsoletes:	gstreamer-media-info
Obsoletes:	gstreamer-mikmod
Obsoletes:	gstreamer-misc
Obsoletes:	gstreamer-musicbrainz
Obsoletes:	gstreamer-mythtv
Obsoletes:	gstreamer-oneton
Obsoletes:	gstreamer-play
Obsoletes:	gstreamer-plugins
Obsoletes:	gstreamer-qcam
Obsoletes:	gstreamer-snapshot
Obsoletes:	gstreamer-swfdec
Obsoletes:	gstreamer-tcp
Obsoletes:	gstreamer-tuner
Obsoletes:	gstreamer-v4l
Obsoletes:	gstreamer-vbidec
Obsoletes:	gstreamer-videosink-xv
Obsoletes:	gstreamer-videotest
Obsoletes:	gstreamer-xine
Obsoletes:	gstreamer-xoverlay
Obsoletes:	gstreamer-yuv4mjpeg
Obsoletes:	gtk-loaders-gstreamer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		gstlibdir 	%{_libdir}/gstreamer-%{vmajor}
%define		gstincludedir	%{_includedir}/gstreamer-%{vmajor}

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
Requires:	glib2-devel >= 1:2.32
Requires:	gstreamer-devel >= %{gst_req_ver}
Obsoletes:	gstreamer-interfaces-devel
Obsoletes:	gstreamer-media-info-devel
Obsoletes:	gstreamer-mixer-devel
Obsoletes:	gstreamer-navigation-devel
Obsoletes:	gstreamer-play-devel
Obsoletes:	gstreamer-plugins-devel
Obsoletes:	gstreamer-tuner-devel
Obsoletes:	gstreamer-xoverlay-devel

%description devel
Include files for GStreamer streaming-media framework plugins.

%description devel -l pl.UTF-8
Pliki nagłówkowe do wtyczek środowiska obróbki strumieni GStreamer.

%package apidocs
Summary:	GStreamer streaming-media framework plugins API documentation
Summary(pl.UTF-8):	Dokumentacja API wtyczek środowiska obróbki strumieni GStreamer
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
GStreamer streaming-media framework plugins API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API wtyczek środowiska obróbki strumieni GStreamer.

##
## Plugins
##

%package -n gstreamer-audiosink-alsa
Summary:	GStreamer plugins for the ALSA sound architecture
Summary(pl.UTF-8):	Wtyczki GStreamera do obsługi architektury ALSA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	gstreamer-audiosink = %{version}
Obsoletes:	gstreamer-alsa
Obsoletes:	gstreamer-audiosink-alsaspdif

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
Obsoletes:	gstreamer-audio-effects

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
Requires:	udev-glib >= 143

%description -n gstreamer-video4linux
GStreamer plugin for Video 4 Linux source.

%description -n gstreamer-video4linux -l pl.UTF-8
Wtyczka GStreamera dla źródła Video 4 Linux.

%package -n gstreamer-vorbis
Summary:	GStreamer plugin for encoding and decoding Ogg Vorbis audio files
Summary(pl.UTF-8):	Wtyczki do GStreamera kodujące i dekodujące pliki dźwiękowe Ogg Vorbis
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

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
%{__libtoolize}
%{__aclocal} -I m4 -I common/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_tremor:--disable-ivorbis} \
	%{!?with_libvisual:--disable-libvisual} \
	--disable-examples \
	--disable-silent-rules \
	--disable-static \
	--enable-experimental \
	--enable-gtk-doc%{!?with_apidocs:=no} \
	--enable-orc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# We don't need plugins' *.la files
%{__rm} $RPM_BUILD_ROOT%{gstlibdir}/*.la
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgst*.la

%find_lang %{gstname}-%{vmajor}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{gstname}-%{vmajor}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README RELEASE
%attr(755,root,root) %{_bindir}/gst-device-monitor-%{vmajor}
%attr(755,root,root) %{_bindir}/gst-discoverer-%{vmajor}
%attr(755,root,root) %{_bindir}/gst-play-%{vmajor}
%attr(755,root,root) %{_libdir}/libgstallocators-%{vmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstallocators-%{vmajor}.so.0
%attr(755,root,root) %{_libdir}/libgstapp-%{vmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstapp-%{vmajor}.so.0
%attr(755,root,root) %{_libdir}/libgstaudio-%{vmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstaudio-%{vmajor}.so.0
%attr(755,root,root) %{_libdir}/libgstfft-%{vmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstfft-%{vmajor}.so.0
%attr(755,root,root) %{_libdir}/libgstpbutils-%{vmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstpbutils-%{vmajor}.so.0
%attr(755,root,root) %{_libdir}/libgstriff-%{vmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstriff-%{vmajor}.so.0
%attr(755,root,root) %{_libdir}/libgstrtp-%{vmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstrtp-%{vmajor}.so.0
%attr(755,root,root) %{_libdir}/libgstrtsp-%{vmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstrtsp-%{vmajor}.so.0
%attr(755,root,root) %{_libdir}/libgstsdp-%{vmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstsdp-%{vmajor}.so.0
%attr(755,root,root) %{_libdir}/libgsttag-%{vmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgsttag-%{vmajor}.so.0
%attr(755,root,root) %{_libdir}/libgstvideo-%{vmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstvideo-%{vmajor}.so.0
%{_mandir}/man1/gst-device-monitor-%{vmajor}.1*
%{_mandir}/man1/gst-discoverer-%{vmajor}.1*
%{_mandir}/man1/gst-play-%{vmajor}.1*
# plugins with no external dependencies
%attr(755,root,root) %{gstlibdir}/libgstapp.so
%attr(755,root,root) %{gstlibdir}/libgstaudioconvert.so
%attr(755,root,root) %{gstlibdir}/libgstaudiorate.so
%attr(755,root,root) %{gstlibdir}/libgstaudiotestsrc.so
%attr(755,root,root) %{gstlibdir}/libgstencodebin.so
%attr(755,root,root) %{gstlibdir}/libgstgio.so
%attr(755,root,root) %{gstlibdir}/libgstplayback.so
%attr(755,root,root) %{gstlibdir}/libgstsubparse.so
%attr(755,root,root) %{gstlibdir}/libgsttcp.so
%attr(755,root,root) %{gstlibdir}/libgsttypefindfunctions.so
%attr(755,root,root) %{gstlibdir}/libgstvideoconvert.so
%attr(755,root,root) %{gstlibdir}/libgstvideorate.so
%attr(755,root,root) %{gstlibdir}/libgstvideoscale.so
%attr(755,root,root) %{gstlibdir}/libgstvideotestsrc.so
%{_libdir}/girepository-1.0/GstAllocators-%{vmajor}.typelib
%{_libdir}/girepository-1.0/GstApp-%{vmajor}.typelib
%{_libdir}/girepository-1.0/GstAudio-%{vmajor}.typelib
%{_libdir}/girepository-1.0/GstFft-%{vmajor}.typelib
%{_libdir}/girepository-1.0/GstPbutils-%{vmajor}.typelib
%{_libdir}/girepository-1.0/GstRtp-%{vmajor}.typelib
%{_libdir}/girepository-1.0/GstRtsp-%{vmajor}.typelib
%{_libdir}/girepository-1.0/GstSdp-%{vmajor}.typelib
%{_libdir}/girepository-1.0/GstTag-%{vmajor}.typelib
%{_libdir}/girepository-1.0/GstVideo-%{vmajor}.typelib
%{_datadir}/gst-plugins-base

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgstallocators-%{vmajor}.so
%attr(755,root,root) %{_libdir}/libgstapp-%{vmajor}.so
%attr(755,root,root) %{_libdir}/libgstaudio-%{vmajor}.so
%attr(755,root,root) %{_libdir}/libgstfft-%{vmajor}.so
%attr(755,root,root) %{_libdir}/libgstpbutils-%{vmajor}.so
%attr(755,root,root) %{_libdir}/libgstriff-%{vmajor}.so
%attr(755,root,root) %{_libdir}/libgstrtp-%{vmajor}.so
%attr(755,root,root) %{_libdir}/libgstrtsp-%{vmajor}.so
%attr(755,root,root) %{_libdir}/libgstsdp-%{vmajor}.so
%attr(755,root,root) %{_libdir}/libgsttag-%{vmajor}.so
%attr(755,root,root) %{_libdir}/libgstvideo-%{vmajor}.so
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
%{_pkgconfigdir}/gstreamer-allocators-%{vmajor}.pc
%{_pkgconfigdir}/gstreamer-app-%{vmajor}.pc
%{_pkgconfigdir}/gstreamer-audio-%{vmajor}.pc
%{_pkgconfigdir}/gstreamer-fft-%{vmajor}.pc
%{_pkgconfigdir}/gstreamer-pbutils-%{vmajor}.pc
%{_pkgconfigdir}/gstreamer-plugins-base-%{vmajor}.pc
%{_pkgconfigdir}/gstreamer-riff-%{vmajor}.pc
%{_pkgconfigdir}/gstreamer-rtp-%{vmajor}.pc
%{_pkgconfigdir}/gstreamer-rtsp-%{vmajor}.pc
%{_pkgconfigdir}/gstreamer-sdp-%{vmajor}.pc
%{_pkgconfigdir}/gstreamer-tag-%{vmajor}.pc
%{_pkgconfigdir}/gstreamer-video-%{vmajor}.pc
%{_datadir}/gir-1.0/GstAllocators-%{vmajor}.gir
%{_datadir}/gir-1.0/GstApp-%{vmajor}.gir
%{_datadir}/gir-1.0/GstAudio-%{vmajor}.gir
%{_datadir}/gir-1.0/GstFft-%{vmajor}.gir
%{_datadir}/gir-1.0/GstPbutils-%{vmajor}.gir
%{_datadir}/gir-1.0/GstRtp-%{vmajor}.gir
%{_datadir}/gir-1.0/GstRtsp-%{vmajor}.gir
%{_datadir}/gir-1.0/GstSdp-%{vmajor}.gir
%{_datadir}/gir-1.0/GstTag-%{vmajor}.gir
%{_datadir}/gir-1.0/GstVideo-%{vmajor}.gir

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gst-plugins-base-libs-%{vmajor}
%{_gtkdocdir}/gst-plugins-base-plugins-%{vmajor}
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

%if %{with v4l1}
%files -n gstreamer-video4linux
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstvideo4linux.so
%endif

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
