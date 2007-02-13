#
# Conditional build:
%bcond_without	gnomevfs	# don't build gnome-vfs plugin
%bcond_without	libvisual	# don't build libvisual plugin
#
%define		gstname		gst-plugins-base
%define		gst_major_ver	0.10
%define		gst_req_ver	0.10.10.1
#
Summary:	GStreamer Streaming-media framework base plugins
Summary(pl.UTF-8):	Podstawowe wtyczki do środowiska obróbki strumieni GStreamer
Name:		gstreamer-plugins-base
Version:	0.10.11
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/gst-plugins-base/%{gstname}-%{version}.tar.bz2
# Source0-md5:	2e78ff25635b31d948def7c2b2d79054
Patch0:		%{name}-bashish.patch
URL:		http://gstreamer.freedesktop.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.12.0
BuildRequires:	gstreamer-devel >= %{gst_req_ver}
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	gtk-doc >= 1.6
BuildRequires:	liboil-devel >= 1:0.3.8
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-PyXML
##
## plugins
##
BuildRequires:	alsa-lib-devel >= 1.0.11
BuildRequires:	cdparanoia-III-devel >= alpha9.8-6
BuildRequires:	freetype-devel >= 2.1.2
%{?with_gnomevfs:BuildRequires:	gnome-vfs2-devel >= 2.15.3}
BuildRequires:	libogg-devel >= 2:1.0
BuildRequires:	libtheora-devel >= 1.0-0.alpha3.1
%{?with_libvisual:BuildRequires:	libvisual-devel >= 0.4.0}
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXv-devel
Requires:	gstreamer >= %{gst_req_ver}
Obsoletes:	gstreamer-artsd
Obsoletes:	gstreamer-audio-effects
Obsoletes:	gstreamer-audiofile
Obsoletes:	gstreamer-audiosink-polypaudio
Obsoletes:	gstreamer-avi
Obsoletes:	gstreamer-cdplayer
Obsoletes:	gstreamer-colorspace
Obsoletes:	gstreamer-dirac
Obsoletes:	gstreamer-festival
Obsoletes:	gstreamer-interfaces
Obsoletes:	gstreamer-interleave
Obsoletes:	gstreamer-kio
Obsoletes:	gstreamer-libdvdnav
Obsoletes:	gstreamer-libfame
Obsoletes:	gstreamer-media-info
Obsoletes:	gstreamer-mikmod
Obsoletes:	gstreamer-misc
Obsoletes:	gstreamer-nas
Obsoletes:	gstreamer-oneton
Obsoletes:	gstreamer-play
Obsoletes:	gstreamer-plugins
Obsoletes:	gstreamer-qcam
Obsoletes:	gstreamer-snapshot
Obsoletes:	gstreamer-sndfile
Obsoletes:	gstreamer-tcp
Obsoletes:	gstreamer-tuner
Obsoletes:	gstreamer-v4l
Obsoletes:	gstreamer-vbidec
Obsoletes:	gstreamer-vcd
Obsoletes:	gstreamer-videosink-xv
Obsoletes:	gstreamer-videotest
Obsoletes:	gstreamer-xine
Obsoletes:	gstreamer-xoverlay
Obsoletes:	gstreamer-yuv4mjpeg
Obsoletes:	gtk-loaders-gstreamer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		gstlibdir 	%{_libdir}/gstreamer-%{gst_major_ver}
%define		gstincludedir	%{_includedir}/gstreamer-%{gst_major_ver}

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
#Requires:	gstreamer >= %{gst_req_ver}
# for locales
Requires:	%{name} = %{version}-%{release}

%description -n gstreamer-cdparanoia
Plugin for ripping audio tracks using cdparanoia under GStreamer.

%description -n gstreamer-cdparanoia -l pl.UTF-8
Wtyczka do ripowania ścieżek dźwiękowych pod GStreamerem za pomocą
cdparanoia.

%package -n gstreamer-gnomevfs
Summary:	GStreamer plugins for GNOME VFS input and output
Summary(pl.UTF-8):	Wtyczki wejścia i wyjścia GNOME VFS do GStreamera
Group:		Libraries
#Requires:	gstreamer >= %{gst_req_ver}
# for locales
Requires:	%{name} = %{version}-%{release}

%description -n gstreamer-gnomevfs
Plugins for reading and writing through GNOME VFS.

%description -n gstreamer-gnomevfs -l pl.UTF-8
Wtyczki do czytania i zapisywania poprzez GNOME VFS.

%package -n gstreamer-libvisual
Summary:	GStreamer libvisual plugin
Summary(pl.UTF-8):	Wtyczka libvisual do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-libvisual
GStreamer libvisual plugin.

%description -n gstreamer-libvisual -l pl.UTF-8
Wtyczka libvisual do GStreamera.

%package -n gstreamer-pango
Summary:	GStreamer pango plugins
Summary(pl.UTF-8):	Wtyczki pango do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-pango
This package contains textoverlay and timeoverlay GStreamer plugins.

%description -n gstreamer-pango -l pl.UTF-8
Ten pakiet zawiera wtyczki textoverlay i timeoverlay do GStreamera.

%package -n gstreamer-theora
Summary:	GStreamer Ogg Theora plugin
Summary(pl.UTF-8):	Wtyczka Ogg Theora do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-theora
GStreamer Ogg Theora plugin.

%description -n gstreamer-theora -l pl.UTF-8
Wtyczka Ogg Theora do GStreamera.

%package -n gstreamer-vorbis
Summary:	GStreamer plugin for encoding and decoding Ogg Vorbis audio files
Summary(pl.UTF-8):	Wtyczki do GStreamera kodujące i dekodujące pliki dźwiękowe Ogg Vorbis
Group:		Libraries
#Requires:	gstreamer >= %{gst_req_ver}
# for locales in ogg module
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
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4 -I common/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_gnomevfs:--disable-gnome_vfs} \
	%{!?with_libvisual:--disable-libvisual} \
	--disable-static \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# We don't need plugins' *.la files
rm -f $RPM_BUILD_ROOT%{gstlibdir}/*.la

%find_lang %{gstname}-%{gst_major_ver}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{gstname}-%{gst_major_ver}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README RELEASE
%attr(755,root,root) %{_bindir}/gst-visualise-*
%attr(755,root,root) %{_libdir}/libgstaudio-*.so.*.*.*
%attr(755,root,root) %{_libdir}/libgstcdda-*.so.*.*.*
%attr(755,root,root) %{_libdir}/libgstinterfaces-*.so.*.*.*
%attr(755,root,root) %{_libdir}/libgstnetbuffer-*.so.*.*.*
%attr(755,root,root) %{_libdir}/libgstriff-*.so.*.*.*
%attr(755,root,root) %{_libdir}/libgstrtp-*.so.*.*.*
%attr(755,root,root) %{_libdir}/libgsttag-*.so.*.*.*
%attr(755,root,root) %{_libdir}/libgstvideo-*.so.*.*.*

%attr(755,root,root) %{gstlibdir}/libgstaudioconvert.so
%attr(755,root,root) %{gstlibdir}/libgstaudiorate.so
%attr(755,root,root) %{gstlibdir}/libgstaudiotestsrc.so
%attr(755,root,root) %{gstlibdir}/libgstdecodebin.so
%attr(755,root,root) %{gstlibdir}/libgstdecodebin2.so
%attr(755,root,root) %{gstlibdir}/libgstffmpegcolorspace.so
%attr(755,root,root) %{gstlibdir}/libgstgdp.so
%attr(755,root,root) %{gstlibdir}/libgstplaybin.so
%attr(755,root,root) %{gstlibdir}/libgstsubparse.so
%attr(755,root,root) %{gstlibdir}/libgsttcp.so
%attr(755,root,root) %{gstlibdir}/libgsttypefindfunctions.so
%attr(755,root,root) %{gstlibdir}/libgstvideo4linux.so
%attr(755,root,root) %{gstlibdir}/libgstvideorate.so
%attr(755,root,root) %{gstlibdir}/libgstvideoscale.so
%attr(755,root,root) %{gstlibdir}/libgstvideotestsrc.so
%{_mandir}/man1/gst-visualise-*.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgstaudio-*.so
%attr(755,root,root) %{_libdir}/libgstcdda-*.so
%attr(755,root,root) %{_libdir}/libgstinterfaces-*.so
%attr(755,root,root) %{_libdir}/libgstnetbuffer-*.so
%attr(755,root,root) %{_libdir}/libgstriff-*.so
%attr(755,root,root) %{_libdir}/libgstrtp-*.so
%attr(755,root,root) %{_libdir}/libgsttag-*.so
%attr(755,root,root) %{_libdir}/libgstvideo-*.so
%{_libdir}/libgstaudio-*.la
%{_libdir}/libgstcdda-*.la
%{_libdir}/libgstinterfaces-*.la
%{_libdir}/libgstnetbuffer-*.la
%{_libdir}/libgstriff-*.la
%{_libdir}/libgstrtp-*.la
%{_libdir}/libgsttag-*.la
%{_libdir}/libgstvideo-*.la
%{gstincludedir}/gst/audio
%{gstincludedir}/gst/cdda
%{gstincludedir}/gst/floatcast
%{gstincludedir}/gst/interfaces
%{gstincludedir}/gst/netbuffer
%{gstincludedir}/gst/riff
%{gstincludedir}/gst/rtp
%{gstincludedir}/gst/tag
%{gstincludedir}/gst/video
%{_pkgconfigdir}/gstreamer-plugins-base-*.pc
%{_gtkdocdir}/gst-plugins-base-libs-*

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

%if %{with gnomevfs}
%files -n gstreamer-gnomevfs
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstgnomevfs.so
%endif

%if %{with libvisual}
%files -n gstreamer-libvisual
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstlibvisual.so
%endif

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
