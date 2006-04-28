#
# Conditional build:
%bcond_without	gnomevfs	# don't build gnome-vfs plugin
%bcond_without	libvisual	# don't build libvisual plugin
#
%define		gstname		gst-plugins-base
%define		gst_major_ver	0.10
%define		gst_req_ver	0.10.5
#
Summary:	GStreamer Streaming-media framework base plugins
Summary(pl):	Podstawowe wtyczki do ¶rodowiska obróbki strumieni GStreamer
Name:		gstreamer-plugins-base
Version:	0.10.6
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/gst-plugins-base/%{gstname}-%{version}.tar.bz2
# Source0-md5:	d8069d1026896d1379072b520de20ebc
Patch0:		%{name}-bashish.patch
URL:		http://gstreamer.freedesktop.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.6.0
BuildRequires:	gstreamer-devel >= %{gst_req_ver}
BuildRequires:	gtk+2-devel >= 2:2.2.0
BuildRequires:	gtk-doc >= 1.3
BuildRequires:	liboil-devel >= 0.3.6
BuildRequires:	libtool
BuildRequires:	pkgconfig
##
## plugins
##
BuildRequires:	alsa-lib-devel >= 0.9.1
BuildRequires:	cdparanoia-III-devel
BuildRequires:	freetype-devel >= 2.1.2
%{?with_gnomevfs:BuildRequires:	gnome-vfs2-devel >= 2.0.4}
BuildRequires:	libogg-devel >= 2:1.0
BuildRequires:	libtheora-devel >= 1.0-0.alpha3.1
%{?with_libvisual:BuildRequires:	libvisual-devel >= 0.2.0}
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXv-devel
Requires:	gstreamer >= %{gst_req_ver}
Obsoletes:	gstreamer-artsd
Obsoletes:	gstreamer-audiofile
Obsoletes:	gstreamer-audiosink-polypaudio
Obsoletes:	gstreamer-avi
Obsoletes:	gstreamer-cdaudio
Obsoletes:	gstreamer-cdplayer
Obsoletes:	gstreamer-colorspace
Obsoletes:	gstreamer-dirac
Obsoletes:	gstreamer-festival
Obsoletes:	gstreamer-gdkpixbuf
Obsoletes:	gstreamer-interfaces
Obsoletes:	gstreamer-interleave
Obsoletes:	gstreamer-jack
Obsoletes:	gstreamer-kio
Obsoletes:	gstreamer-libdvdnav
Obsoletes:	gstreamer-libfame
Obsoletes:	gstreamer-media-info
Obsoletes:	gstreamer-mikmod
Obsoletes:	gstreamer-misc
Obsoletes:	gstreamer-mjpegtools
Obsoletes:	gstreamer-musicbrainz
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
Obsoletes:	gstreamer-v4l2
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

%description -l pl
GStreamer to ¶rodowisko obróbki danych strumieniowych, bazuj±ce na
grafie filtrów operuj±cych na danych medialnych. Aplikacje u¿ywaj±ce
tej biblioteki mog± robiæ wszystko od przetwarzania d¼wiêku w czasie
rzeczywistym, do odtwarzania filmów i czegokolwiek innego zwi±zego z
mediami. Architektura bazuj±ca na wtyczkach pozwala na ³atwe dodawanie
nowych typów danych lub mo¿liwo¶ci obróbki.

%package devel
Summary:	Include files for GStreamer streaming-media framework plugins
Summary(pl):	Pliki nag³ówkowe do wtyczek ¶rodowiska obróbki strumieni GStreamer
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

%description devel -l pl
Pliki nag³ówkowe do wtyczek ¶rodowiska obróbki strumieni GStreamer.

##
## Plugins
##

%package -n gstreamer-audiosink-alsa
Summary:	GStreamer plugins for the ALSA sound architecture
Summary(pl):	Wtyczki GStreamera do obs³ugi architektury ALSA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	gstreamer-audiosink = %{version}
Obsoletes:	gstreamer-alsa

%description -n gstreamer-audiosink-alsa
Input and output plugin for the ALSA soundcard driver architecture.

%description -n gstreamer-audiosink-alsa -l pl
Wtyczka wej¶cia i wyj¶cia ze sterowników d¼wiêkowych architektury ALSA
do GStreamera.

%package -n gstreamer-audio-effects-base
Summary:	GStreamer base audio effects plugins
Summary(pl):	Podstawowe wtyczki efektów d¼wiêkowych do GStreamera
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	gstreamer-audio-effects

%description -n gstreamer-audio-effects-base
GStreamer base audio effects plugins.

%description -n gstreamer-audio-effects-base -l pl
Podstawowe wtyczki efektów d¼wiêkowych do GStreamera.

%package -n gstreamer-cdparanoia
Summary:	GStreamer plugin for CD audio input using CDParanoia IV
Summary(pl):	Wtyczka do GStreamera odtwarzaj±ca p³yty CD-Audio przy u¿yciu CDParanoia IV
Group:		Libraries
#Requires:	gstreamer >= %{gst_req_ver}
# for locales
Requires:	%{name} = %{version}-%{release}

%description -n gstreamer-cdparanoia
Plugin for ripping audio tracks using cdparanoia under GStreamer.

%description -n gstreamer-cdparanoia -l pl
Wtyczka do ripowania ¶cie¿ek d¼wiêkowych pod GStreamerem za pomoc±
cdparanoia.

%package -n gstreamer-gnomevfs
Summary:	GStreamer plugins for GNOME VFS input and output
Summary(pl):	Wtyczki wej¶cia i wyj¶cia GNOME VFS do GStreamera
Group:		Libraries
#Requires:	gstreamer >= %{gst_req_ver}
# for locales
Requires:	%{name} = %{version}-%{release}

%description -n gstreamer-gnomevfs
Plugins for reading and writing through GNOME VFS.

%description -n gstreamer-gnomevfs -l pl
Wtyczki do czytania i zapisywania poprzez GNOME VFS.

%package -n gstreamer-libvisual
Summary:	GStreamer libvisual plugin
Summary(pl):	Wtyczka libvisual do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-libvisual
GStreamer libvisual plugin.

%description -n gstreamer-libvisual -l pl
Wtyczka libvisual do GStreamera.

%package -n gstreamer-pango
Summary:	GStreamer pango plugins
Summary(pl):	Wtyczki pango do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-pango
This package contains textoverlay and timeoverlay GStreamer plugins.

%description -n gstreamer-pango -l pl
Ten pakiet zawiera wtyczki textoverlay i timeoverlay do GStreamera.

%package -n gstreamer-theora
Summary:	GStreamer Ogg Theora plugin
Summary(pl):	Wtyczka Ogg Theora do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-theora
GStreamer Ogg Theora plugin.

%description -n gstreamer-theora -l pl
Wtyczka Ogg Theora do GStreamera.

%package -n gstreamer-vorbis
Summary:	GStreamer plugin for encoding and decoding Ogg Vorbis audio files
Summary(pl):	Wtyczki do GStreamera koduj±ce i dekoduj±ce pliki d¼wiêkowe Ogg Vorbis
Group:		Libraries
#Requires:	gstreamer >= %{gst_req_ver}
# for locales in ogg module
Requires:	%{name} = %{version}-%{release}

%description -n gstreamer-vorbis
Plugins for creating and playing Ogg Vorbis audio files.

%description -n gstreamer-vorbis -l pl
Wtyczki do tworzenia i odtwarzania plików d¼wiêkowych Ogg Vorbis.

%package -n gstreamer-imagesink-x
Summary:	GStreamer XFree86/X.org output plugin
Summary(pl):	Wtyczka wyj¶cia obrazu XFree86/X.org dla GStreamera
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	gstreamer-videosink = %{version}

%description -n gstreamer-imagesink-x
Standard XFree86/X.org image sink.

%description -n gstreamer-imagesink-x -l pl
Standardowa wtyczka wyj¶cia obrazu XFree86/X.org dla GStreamera.

%package -n gstreamer-imagesink-xv
Summary:	GStreamer Xvideo output plugin
Summary(pl):	Wtyczka wyj¶cia obrazu Xvideo dla GStreamera
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	gstreamer-videosink = %{version}

%description -n gstreamer-imagesink-xv
XFree86/X.org image sink via Xvideo extension.

%description -n gstreamer-imagesink-xv -l pl
Wtyczka wyj¶cia obrazu Xvideo dla GStreamera.

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
%attr(755,root,root) %{gstlibdir}/libgstffmpegcolorspace.so
%attr(755,root,root) %{gstlibdir}/libgstplaybin.so
%attr(755,root,root) %{gstlibdir}/libgstsubparse.so
%attr(755,root,root) %{gstlibdir}/libgsttcp.so
%attr(755,root,root) %{gstlibdir}/libgsttypefindfunctions.so
%attr(755,root,root) %{gstlibdir}/libgstvideo4linux.so
%attr(755,root,root) %{gstlibdir}/libgstvideorate.so
%attr(755,root,root) %{gstlibdir}/libgstvideoscale.so
%attr(755,root,root) %{gstlibdir}/libgstvideotestsrc.so
%{_mandir}/man1/gst-visualise-*.1*
%{_gtkdocdir}/gst-plugins-base-plugins-*

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
