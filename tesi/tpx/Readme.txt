
Contents
 =========================

<<About TpX drawing tool>>

<<TpX usage>>

<<TpX output formats>>

<<Export formats>>

<<Import>>

<<TpX primitives>>

<<Bitmap objects>>

<<LaTeX preamble>>

<<LaTeX figure environment>>

<<Using mouse for editing>>

<<TpX command line options>>

<<Preview>>

<<Program settings>>

<<Picture properties>>

<<Some painting details>>

<<Lazarus version of TpX>>

<<Adding TpX to WinEdt menu>>

<<Image tool>>

<<TpX modifications log file>>

<<Acknowledgements>>

<<Links>>

About TpX drawing tool
 =========================

TpX is a lightweight, easy-to-use graphical editor for Windows
platform for creation of drawings and inclusion them into LaTeX files
in publication-ready form. It can also be used as a stand-alone editor
for vector graphics.

The output is a file (with extension .TpX) containing the drawing as
LaTeX code or as an \includegraphics link to an external file created
by the program. User can choose between several <<output formats>>.
TpX saves its own data in TeX file comments so that the drawing could
be loaded into TpX and edited again. This internal TpX format is based
on XML and could be understood and edited easily.

TpX can <<import>> EMF/WMF pictures created by other Windows
applications, including many applications producing scientific graphs.
It also can import simple SVG pictures. In most cases the result is
nice, though sometimes imported picture needs some manual editing. So
TpX can be used as a EMF-to-any and SVG-to-any converter.

TpX usage
 =========================

TpX is a GUI program. So be prepared to use mouse, menus, etc. The
primary use of TpX is for smooth inclution of vector graphics into
LaTeX documents.

TpX drawings are included in LaTeX files using \input command, like
\input{foo.TpX}.
It is necessary to use several LaTeX packages for TpX to be functional
(see <<TpX output formats>> and <<LaTeX preamble>>). One can start
from template document called Template.tex in TpX distribution.

It is possible to keep TpX drawings in a subdirectory. The command in
LaTeX file would be
\input{mypics/foo.TpX}
if subdirectory name is mypics. Set IncludePath in TpX file to
mypics/.

TpX can be used as a stand-alone editor for vector graphics without
targeting LaTeX. For example, some people use it to produce EMF
graphics for inclusion into popular office programs. It is possible to
create graphics in many export formats. However, note that TpX is not
able to embed fonts in most export formats. Moreover, one needs LaTeX
to produce nice-looking formulas. See <<Export formats>> for more
details.

TpX can be used from command line without GUI. See <<TpX command line
options>>.

TpX output formats
 =========================

TpX provides several output formats. Use "Picture properties" or
toolbar drop-down buttons to change the format. The format is chosen
separately for LaTeX and PdfLaTeX.

Not all of the formats are ideal, so the choice needs thoughtful
consideration. EPS and PDF are TpX defaults for LaTeX/DVI and PdfLaTeX
respectively. Also recommended is PGF or TikZ.

* LaTeX picture environment. This standard LaTeX environment is enhanced
 by epic.sty and bez123.sty LaTeX packages. Both packages are
 compatible with TeX/DVI and PdfLaTeX. The format is suitable for
 simple drawings only, because complicated drawings take a long time
 for TeX to process and can cause memory shortage. There are many
 limitations. For example, curved lines can not be dashed or dotted.
 Also, in general the result is of rather low quality.

* Encapsulated Postscript (EPS). The most popular format for advanced
 TeX graphics. EPS is saved as a separate file without text and is
 inserted into TpX file using \includegraphics command from graphicx
 LaTeX package. TpX surrounds \includegraphics command by picture
 environment to put text over the picture. Can not be used with
 PdfLaTeX.

* PDF. Included in TpX in the same fashion as EPS. Can only be used with
 PdfLaTeX, not LaTeX/DVI.

* PDF from EPS. PDF is created from EPS using GhostScript. Set the path
 to the program in <<"TpX Settings">>. (The format is called epstopdf
 for historical reasons).

* PGF. PGF code is kept in LaTeX pgfpicture environment similar to
 picture environment. Requires pgf package. Compatible with both
 LaTeX/DVI and PdfLaTeX.

* TikZ. TikZ is similar to PGF (and is based upon it), but is more
 readable. Requires tikz package.

* PSTricks. PSTricks code is kept in TeX pspicture environment similar
 to picture environment. Requires pstricks package. Not compatible with
 PdfLaTeX.

* Metapost. Graphic language similar to pstricks, but an external file
 is created and an external MetaPost program is needed. Set the path to
 the program in <<"TpX Settings">>. Compatible with both LaTeX/DVI and
 PdfLaTeX. TeX is used to typeset text labels in MetaPost. This could
 be turned off by setting MetaPostTeXText to 0. Use metapost.tex.inc
 file to configure LaTeX preamble used in MetaPost files
 (\documentclass command and \usepackage commands for needed packages).

* Bitmap (PNG, BMP). Requires graphicx LaTeX package. Obviously, bitmap
 is not vector graphics, so it is not scalable. TpX does not use LaTeX
 to write text in bitmaps, so they can not incorporate LaTeX formulas.
 PNG is compatible with both LaTeX/DVI and PdfLaTeX. Currently BMP is
 not compatible with PdfLaTeX. Currently bitmaps are not compatible
 with DVIPS and dvi2pdf; they are for DVI viewers only when used with
 LaTeX. Thus, bitmaps are most useful with PdfLaTeX.

* Enhanced Metafile (EMF). Can be used with LaTeX/DVI for preview (it is
 converted to bitmap for this purpose). Not compatible with PdfLaTeX.
 Recommended as <<export format>> only.

* None. Set format to 'none' if you do not need output.

All TeX packages used are available from CTAN [http://www.ctan.org/].

See also <<Export formats>>

Export formats
 =========================

To import TpX drawing into some other program, to embed fonts into
EPS/PDF or to publish drawing on the Web TpX export capabilities could
be used ("Save as.." in "File" menu). TpX can export to several
formats. Note that most export formats can not incorporate TeX fonts
and formulas (however, see below on "LaTeX EPS", and derived formats;
also note MetaPost which is LaTeX-aware).

* EPS. Type 1 font (.pfb) could be embedded. Set the path to a font in
 <<"TpX Settings">>.

* PDF. Currently font embedding is not implemented, so only Latin
 characters and Times are supported.

* PDF from EPS. PDF is created from EPS using GhostScript. Set the path
 to the program in <<"TpX Settings">>.

* Scalable Vector Graphics (SVG). A promising Web vector graphics
 format. Needs a viewer. Several popular vector graphics editors like
 Corel Draw or Adobe Illustrator can read it.

* Bitmap (PNG, BMP). PNG is more compact and could be viewed in most
 modern Web browsers so it is recommended.

* Enhanced Metafile (EMF). Standard Windows vector format. It can also
 be copied to Windows clipboard and then pasted into some other program
 (like MS Word, PowerPoint, Adobe Illustrator).

* LaTeX EPS (latex-dvips). EPS produced by running latex and dvips on
 TpX drawing. This format allows to include LaTeX formulas and embed
 fonts so it is the format of choice for high-quality stand-alone
 graphics. Attempt is made to ensure tight bounding box for the EPS.

* PDF from LaTeX EPS (latex-dvips-gs-pdf). The same as "LaTeX EPS" with
 additional run of GhostScript to produce PDF.

* LaTeX custom (latex-dvips-gs-<foo>). The same as "LaTeX EPS" with
 additional run of GhostScript to produce a custom image in a format
 supported by GhostScript. This is a format of choice to produce high-
 quality bitmaps with LaTeX formulas. Set GhostscriptCustomKeys to
 change the device and resolution.

* Metapost program.

* Metapost EPS output (MPS).

* LaTeX preview source. Parent LaTeX document and other files needed to
 create a DVI/PS preview. This is useful for debugging purposes.

* PdfLaTeX preview source. Parent pdfLaTeX document and other files
 needed to create a PDF preview.

See also <<TpX output formats>>

Import
 =========================

TpX can import Enhanced Metafile (EMF), though not 100% correctly.
Under Windows most reasonable programs, which produce graphs, can
either export them as EMF files, or copy to clipboard as EMF. To
capture EMF from clipboard, use "Tools">"Capture EMF". EMF can also be
just pasted from clipboard (though this is not recommended if physical
units must be preserved). TpX can also import old-style Windows
Metafiles (WMF).

Another TpX import format is Scalable Vector Graphics (SVG) based on
open international standard created by W3C [http://www.w3.org/]. As
the format is very rich TpX can understand only some basic subset of
it.

There is a possibility to use pstoedit utility to import EPS and PDF.
Set the path to the program in <<"TpX Settings">>. The utility could
be downloaded from http://pstoedit.com/.

TpX primitives
 =========================

Line (can include arrows)
Rectangle
Polyline
Polygon
Circle
Ellipse
Arc
Sector
Segment
Curve
Closed curve
Bezier path
Closed Bezier path
Text
Star
Symbol
<< Bitmap>>

Bitmap objects
 =========================

Bitmaps are included in TpX drawings as external files. TpX
understands JPEG, PNG and BMP images. Image files can be in the same
directory as the parent drawing or in a subdirectory. If inserted
bitmap is not in a subdirectory then "bitmaps" subdirectory is created
and the file is moved there.

In order to include bitmap in a LaTeX document TpX has to convert it
to EPS. Set the path to converter program in <<"TpX Settings">>
(Bitmap2EpsPath). It is recommended to use sam2p utility which could
be downloaded from http://www.inf.bme.hu/~pts/sam2p/. It is also
possible to use the widespread bmeps utility.

Bitmaps can not be used with 'tex' and 'metapost' output formats.

LaTeX preamble
 =========================

This is a sample preamble to include in parent LaTeX file. It uses
ifpdf package to switch between two different modes of running
PdfLaTeX. (Download ifpdf from CTAN [http://www.ctan.org/] if you do
not have one). Comment out unused packages or just delete the
corresponding commands.

\documentclass[a4paper,10pt]{article}
\usepackage{color}
\usepackage{ifpdf}
\ifpdf %if using pdfLaTeX in PDF mode
  \usepackage[pdftex]{graphicx}
  \DeclareGraphicsExtensions{.pdf,.png,.jpg,.jpeg,.mps}
  \usepackage{pgf}
  \usepackage{tikz}
\else %if using LaTeX or pdfLaTeX in DVI mode
  \usepackage{graphicx}
  \DeclareGraphicsExtensions{.eps,.bmp}
  \DeclareGraphicsRule{.emf}{bmp}{}{}% declare EMF filename extension
  \DeclareGraphicsRule{.png}{bmp}{}{}% declare PNG filename extension
  \usepackage{pgf}
  \usepackage{tikz}
  \usepackage{pstricks}
\fi
\usepackage{epic,bez123}
\usepackage{floatflt}% package for floatingfigure environment
\usepackage{wrapfig}% package for wrapfigure environment



LaTeX figure environment
 =========================

Possible options for LaTeX figure environment are:

* no figure (user must surround the \input command for TpX drawing by
 figure environment and supply the caption and label as usual)

* standard LaTeX figure environment

* floatingfigure from floatflt package

* wrapfigure from wrapfig package

Packages floatflt and wrapfig are available from CTAN
[http://www.ctan.org/]. Both implement floating figure.

Using mouse for editing
 =========================

TpX hot keys could be learned from the main menu. However, some
editing tasks could only be done with mouse. The list follows:

* Click object:  Select object (current selection would be lost)

* Shift-click object:  Add object to selection (current selection would
 be maintained)

* Double-click object:  Edit object properties

* Drag object:  Move object

* Drag control point:  Move control point of selected object to reshape
 it

* Ctrl-drag object:  Copy object and drag the copy

* Ctrl-click object/control point:  Add/delete control point of selected
 object

* Ctrl-Alt-click object:  Break path, making graphical object disjoint

* Wheel:  Move viewport vertically

* Shift-wheel:  Move viewport horizontally

* Ctrl-wheel:  Zoom viewport

* Alt-drag round control point of Bezier curve:   Determines whether the
 joint is kept smooth.

TpX command line options
 =========================

* -f, --file <file name> The name of input file (TpX, EMF, SVG, ...)

* -i, --texinput <LaTeX file> The name of parent LaTeX document

* -l, --texline <line number> The line number in parent LaTeX document

* -o, --output <file name> The name of output file

* -m, --format <format name>,<format name> The names of TpX <<output
 formats>> The formats are tex, pgf, pstricks, eps, png, bmp, metapost,
 emf, none for LaTeX/DVI and tex, pgf, pdf, png, metapost, epstopdf,
 none for PdfLaTeX.

* -x, --export <format name> The id of <<export format>>. The formats
 are svg, emf, eps, png, bmp, pdf, metapost, mps, epstopdf, latexeps,
 latexpdf, latexcustom, latexsrc, pdflatexsrc.

-f option can be absent. Just run TpX as
TpX.exe <options> <file name>.

When output file is not specified with -o option, TpX chooses file
name automatically.

When -i -l options are used the parent TeX file is scanned for
\input{<filename>.TpX} line. The line closest to specified line is
chosen. This is useful for calling TpX from LaTeX editor like WinEdt.
(See <<Adding TpX to WinEdt menu>> on how to use this with WinEdt.)

In presence of -o and/or -x option TpX runs without GUI.

Examples:

TpX.exe foo.TpX
- open foo.TpX in TpX program, GUI

TpX.exe foo.TpX -o
- refresh foo.TpX, no GUI

TpX.exe foo.svg -x png
- import foo.svg and export it as png with name foo-export.png, no GUI

TpX.exe foo.TpX -o foofoo.TpX -m pgf,png
- load foo.TpX and save it as foofoo.TpX using pgf and png output
formats, no GUI

Preview
 =========================

TpX drawing can be previewed in many formats. It can be previewed as a
part of LaTeX document (see <<TpX output formats>>) or as a stand-
alone image (see <<Export formats>>).

Stand-alone image is just exported and opened in a default program
associated with the image extension. Note that the fonts are normally
not embedded and the result is not as nice as it is with LaTeX. So use
this for quick preview or for drawings without complex text or
formulas.

Temporary LaTeX document is produced using one of the following
sequences:

* LaTeX -> DVI

* LaTeX -> DVI -> PS

* PdfLaTeX -> PDF

Make sure that the paths to the tools (LaTeX, PdfLaTeX, DVIPS) and
viewers needed are set in <<"TpX Settings">>.

LaTeX preamble is taken from the preview.tex.inc file. This is
basically a \documentclass command. Current version of TpX adds the
packages it needs (graphicx, color, pstricks, pgf, tikz, epic, bez123,
floatflt, wrapfig) automatically. However, make sure that other
relevant packages are included in LaTeX preamble. For example, if you
use AMS fonts, put \usepackage[psamsfonts]{amssymb} to the preamble.
Do not forget to include language and encoding stuff as needed. For
example,

\usepackage[english,russian]{babel}
\usepackage[cp1251]{inputenc}

Program settings
 =========================

Program settings can be changed in "TpX Settings" (in "Files" menu).
The settings are stored in TpX.ini. For the meaning of the settings
used to set initial properties for a new picture (like
PicScale_Default) see <<Picture properties>>.

* PicScale_Default: Default value of PicScale

* Border_Default: Default value of Border

* TeXFormat_Default: Default value of TeXFormat

* PdfTeXFormat_Default: Default value of PdfTeXFormat

* BitmapRes_Default: Default value of BitmapRes

* PicMagnif_Default: Default value of PicMagnif

* IncludePath_Default: Default value of IncludePath

* LineWidth_Default: Default value of LineWidth

* ArrowsSize_Default: Default value of ArrowsSize

* StarsSize_Default: Default value of StarsSize

* HatchingStep_Default: Default value of HatchingStep

* HatchingLineWidth_Default: Default value of HatchingLineWidth

* DottedSize_Default: Default value of DottedSize

* DashSize_Default: Default value of DashSize

* DefaultFontHeight_Default: Default value of DefaultFontHeight

* FontName_Default: Default value of FontName

* DefaultSymbolSize_Default: Default value of DefaultSymbolSize

* ApproximationPrecision_Default: Default value of
 ApproximationPrecision

* TeXCenterFigure_Default: Default value of TeXCenterFigure

* TeXFigure_Default: Default value of TeXFigure

* FontSizeInTeX_Default: Default value of FontSizeInTeX

* MetaPostTeXText_Default: Default value of MetaPostTeXText

* LatexPath: Path to LaTeX (latex.exe)

* PdfLatexPath: Path to PDFLaTeX (pdflatex.exe)

* DviPsPath: Path to DVIPS (dvips.exe)

* DviViewerPath: Path to DVI viewer (e.g. yap.exe). Leave this blank to
 use the default viewer

* PdfViewerPath: Path to PDF viewer (e.g. acrobat.exe). Leave this blank
 to use the default viewer

* PSViewerPath: Path to PostScript viewer (e.g. gsview32.exe). Leave
 this blank to use the default viewer

* SvgViewerPath: Path to SVG viewer (e.g. iexplore.exe). Leave this
 blank to use the default viewer

* PngViewerPath: Path to PNG viewer. Leave this blank to use the default
 viewer

* BmpViewerPath: Path to BMP viewer. Leave this blank to use the default
 viewer

* TextViewerPath: Path to text viewer (e.g. notepad.exe). Leave this
 blank to use the default viewer

* PostscriptPrinter: Postscript printer to create EPS files

* PostscriptPrinterUseOffset: Use offset when creating EPS files

* MetaPostPath: Path to MetaPost program (mpost.exe or mp.exe). Needed
 for exporting to MetaPost EPS (.mps)

* Font_pfb_Path: Path to Type 1 font (.pfb). Needed for embedding font
 into EPS

* PsToEditPath: Path to PsToEdit program (pstoedit.exe). Needed for
 converting EPS to EMF or SVG (used for EPS import)

* PsToEditFormat: Format for PsToEdit program for converting EPS to EMF
 or SVG (used for EPS import). Format can be emf or one of the better
 implementations (wemf, wemfc, wemfnss) which are available in
 registered version of PsToEdit. For SVG set plot-svg (free version) or
 svg (registered version)

* GhostscriptPath: Path to Ghostscript program (gswin32c.exe). Needed
 for EPS to PDF conversion, custom export (latexcustom) and previewing
 PS and PDF files in Open dialog

* GhostscriptCustomKeys: Ghostscript command line options used for
 custom export (latexcustom). Example: -r300 -sDEVICE=png256. List of
 possible devices taken literally from Ghostscript follows: bbox bit
 bitcmyk bitrgb bj10e bj200 bjc600 bjc800 bmp16 bmp16m bmp256 bmp32b
 bmpgray bmpmono bmpsep1 bmpsep8 cdeskjet cdj550 cdjcolor cdjmono
 declj250 deskjet devicen display djet500 djet500c eps9high eps9mid
 epson epsonc epswrite ibmpro ijs jetp3852 jpeg jpeggray laserjet lbp8
 lj250 ljet2p ljet3 ljet3d ljet4 ljet4d ljetplus m8510 mswindll
 mswinpr2 necp6 nullpage pbm pbmraw pcx16 pcx24b pcx256 pcxcmyk pcxgray
 pcxmono pdfwrite pgm pgmraw pgnm pgnmraw pj pjxl pjxl300 pkmraw png16
 png16m png256 pngalpha pnggray pngmono pnm pnmraw ppm ppmraw psdcmyk
 psdrgb psmono pswrite pxlcolor pxlmono r4081 spotcmyk st800 stcolor
 t4693d2 t4693d4 t4693d8 tek4696 tiff12nc tiff24nc tiff32nc tiffcrle
 tiffg3 tiffg32d tiffg4 tiffgray tifflzw tiffpack tiffsep uniprint

* Bitmap2EpsPath: Path to a program (like sam2p or bmeps) which converts
 bitmaps to EPS files. (It is used for including bitmaps into output
 graphics).

* RecentFiles: List of recent files

* ExtAssoc: Associate ".TpX" extension with TpX

* ShowGrid: Show grid

* GridOnTop: Grid on top

* ShowCrossHair: Show crosshair

* ShowRulers: Show rulers

* ShowScrollBars: Show scroll bars

* AreaSelectInside: Area select inside only

* UseSnap: Snap to grid

* UseAngularSnap: Angular snap (45 degrees)

* Mainform.Left: Main window left side position

* Mainform.Top: Main window top side position

* Mainform.Width: Main window width

* Mainform.Height: Main window height

* Mainform.Maximized: Main window state

Picture properties
 =========================

Picture properties are stored inside .TpX file. Default values (which
are used for the new drawings) are taken from <<"TpX Settings">>.
(FontName is left empty which means the use of FontName_Default).

* Caption: Text for LaTeX \caption

* Comment: Information about the picture

* Label: Id for LaTeX \label

* PicScale: Picture scale (mm per unit), physical size of the logical
 unit representing picture coordinates. (This unit is referred to as
 "sp" in hints for other picture properties). Use PicScale to scale
 picture without scaling line widths and other dimensions set in
 physical units.

* Border: Picture border (mm)

* TeXFormat: Format for including picture in TeX (tex, pgf, pstricks,
 eps, png, bmp, metapost, tikz, emf, none)

* PdfTeXFormat: Format for including picture in PdfTeX (tex, pgf, pdf,
 png, metapost, tikz, epstopdf, none)

* BitmapRes: Bitmap resolution in pixels per meter. Use BitmapRes to set
 resolution of exported PNG and BMP images). Conversion between pixels
 per meter (PPM) and pixels per inch (PPI): 100 PPI = 3937 PPM 300 PPI
 = 11811 PPM 600 PPI = 23622 PPM

* PicMagnif: Picture physical size magnification factor. Use PicMagnif
 to change the meaning of mm for quick rescaling of the picture

* IncludePath: Path to add before \includegraphics file name (like
 mypictures/)

* LineWidth: Basic line width (mm). Line widths for the drawing are set
 as fractions of this quantity

* ArrowsSize: Arrows size (sp)

* StarsSize: Stars size (sp)

* HatchingStep: Hatching step (mm)

* HatchingLineWidth: Hatching line width (fraction of LineWidth)

* DottedSize: Dotted line step size (mm)

* DashSize: Dashed line step size (mm)

* DefaultFontHeight: Default font height (sp)

* FontName: Font for text labels. Leave FontName empty to use
 FontName_Default

* DefaultSymbolSize: Default symbol size factor ("diameter", sp)

* ApproximationPrecision: Precision of various approximations like
 linearization of Bezier curves (mm)

* MiterLimit: Miter limit. Used to cut off too long spike miter join
 could have when the angle between two lines is sharp. If the ratio of
 miter length (distance between the outer corner and the inner corner
 of the miter) to line width is greater than miter limit, then bevel
 join is used instead of miter join. Default value of miter limit is
 10. This option is not applicable to TeX-picture and PsTricks formats.

* TeXCenterFigure: Center TeX figure by adding \centering before
 picture/includegraphics

* TeXFigure: TeX figure environment: none - no figure, figure - standard
 {figure} environment, floatingfigure - {floatingfigure} from floatflt
 package, wrapfigure - {wrapfigure} from wrapfig package

* TeXFigurePlacement: The optional argument [placement] determines where
 LaTeX will try to place your figure. There are four places where LaTeX
 can possibly put a float: h (Here) - at the position in the text where
 the figure environment appears t (Top) - at the top of a text page b
 (Bottom) - at the bottom of a text page p (Page of floats) - on a
 separate float page, which is a page containing no text, only floats
 Putting ! as the first argument in the square brackets will encourage
 LATEX to do what you say, even if the result's sub-optimal. Example:
 htbp

 For wrapfigure placement is one of r, l, i, o, R, L, I, O, for right,
 left, inside, outside, (here / FLOAT)

 The floatingfigure placement option may be either one of the
 following: r, l, p, or v. The options all overrule any present package
 option which may be in effect. The options have the following
 functions: r Forces the current floating figure to be typeset to the
 right in a paragraph l Forces the current floating figure to be
 typeset to the left in a paragraph p Forces the current floating
 figure to be typeset to the right in a paragraph if the page number is
 odd, and to the left if even v Applies the package option to the
 current figure, and if no package option is specified, it forces the
 current floating figure to be typeset to the right in a paragraph if
 the page number is odd, and to the left if even

* TeXFigurePrologue: Text to put before float

* TeXFigureEpilogue: Text to put after float

* TeXPicPrologue: Text to put before picture/includegraphics

* TeXPicEpilogue: Text to put after picture/includegraphics

* FontSizeInTeX: Put font size information into LaTeX/MetaPost output
 code. Set FontSizeInTeX to 0 to use the default font size of the
 parent LaTeX document (or default font size of MetaPost drawing)

* MetaPostTeXText: Use TeX text in MetaPost files

Some painting details
 =========================

Line join. Currently TpX uses only "miter line join" (not "bevel join"
or "round join").

Miter limit. Used to cut off too long spike miter join could have when
the angle between two lines is sharp. If the ratio of miter length
(distance between the outer corner and the inner corner of the miter)
to line width is greater than miter limit, then bevel join is used
instead of miter join. Default value of miter limit is 10. This option
is not applicable to LaTeX-picture and PsTricks formats.

Line cap. Currently TpX uses only "butt" line caps.

Fill rule. Currently TpX uses only "nonzero winding" fill rule (as
opposed to "even-odd" aka "alternate").

References:

* Scalable Vector Graphics (SVG) Specification by W3C
 http://www.w3.org/TR/SVG/

* PostScript Language Reference by Adobe Systems ("Red Book")
 http://www.adobe.com/products/postscript/resources.html

Lazarus version of TpX
 =========================

Lazarus is a cross platform clone of Delphi based on open source Free
Pascal compiler. Lazarus version of TpX has some limitations. Some of
the major known ones are

* Export of bitmap images (PNG, BMP) is not working (this feature needs
 conversion of Graphics32 package to Lazarus)

* Export of EMF images is not working

* Import of WMF images is not working

* No "Capture EMF"

* "Image tool" is not working

* Alignment of text labels is incorrect (correct alignment needs
 additional information about font dimensions)

Adding TpX to WinEdt menu
 =========================

* Edit TpX_menu.dat, replacing Path_to_TpX by the actual path to TpX.exe

* Start "Macros">"Execute Macro..."

* Choose install_TpX.edt

Default keyboard shortcut is Alt+P. You can change this in
"Options">"Menu Setup">"Tools">"TpX drawing tool"

Typing Alt+P in a TeX document with included TpX drawings will run
TpX.exe and load a drawing into it. The drawing closest to the current
cursor position will be opened. The TpX file containing drawing need
not exist.

WinEdt [http://www.winedt.com] is a powerful editor and shell for TeX
documents.

Image tool
 =========================

Image tool is an additional utility embedded into TpX program. It can
manipulate EMF images. A useful function is printing EMF images with
Postscript printer to get EPS file. EPS mode should be set for printer
for this to work.

TpX modifications log file
=========================================
  [+] Added, [-] Fixed, [*] Changed
=========================================

=========================================
2008-12-07 TpX Version 1.5
=========================================

[-] Command line export to latexsrc and pdflatexsrc
 did not add '.tex' extension to output file name.

[-] A bug in undo for freehand lines.

[-] Grouped objects lost their parent drawing (arrow-heads were 
 drawn incorrectly for objects in a group),

[-] Table editor in the "Edit coordinates" window was too narrow
 leading sometimes to disappearance of table columns.

=========================================
2008-11-17 TpX Version 1.5 beta 2
=========================================

[-] Fixed problems with TeXLive.

[-] There was a bug which caused TpX not to load the new
 document properties at program start.

[+] preview.tex.inc was simplified. TpX now adds the packages it
 needs automatically. Unneeded packages are not added now
 to preview document.

[*] MetaPost output does not use \textcolor in TeX text anymore.

[-] preserveAspectRatio='none' was not added when needed while
 writing bitmap to SVG.

[+] Freehand-drawn Bezier path is created with current properties 
 applied to it.

=========================================
2008-11-09 TpX Version 1.5 beta 
=========================================

[+] Now it is possible to use the default font size of the parent 
 LaTeX document by setting FontSizeInTeX property to 0
 (\fontsize...\selectfont would not be added to LaTeX code).

[-] PicMagnif was not taken into account when setting
 font size in MetaPost

[*] Lua module for generating TpX files (lTpX)
 replaced the old Python module (TpXpy)

[*] New version of TpX file format, version 5. Treatment
 of dotted lines has changed incompatibly (see below).

[*] Vertical alignment of text proved to be unreliable
 and hard to be made compatible across devices. 
 All text labels are now baseline aligned.

[+] More properties of graphical objects can be changed
 using toolbar (for all selected objects at once):
 arrow-heads, text labels, stars.

[-] WinEdt command in 'TpX_menu.dat' fixed to work correctly in 
 "soft breaks" regime

[+] Saving preview source

[+] Picking up, applying and clearing properties of graphical objects

[+] Improved SVG import

[+] Store "Snap to grid" and "Angular snap" state

[+] Store full window position including "maximized" state

[+] Objects group/ungroup operations.

[+] "Simplify Bezier" operation

[+] Bitmap objects (sam2p utility is used to convert bitmaps to EPS
  for inclusion into PostScript output)

[+] Request for showing (as a temporary file) the actual source 
 (if drawing has changed)

[-] Some objects did not show up on rubber canvas during drag / rotate 
 transformation operations

[+] 'Grid on top' setting

[+] Optionally remove crosshair

[-*] Fix for Bezier paths with PSTricks output. Use \moveto
 and \curveto instead of \psbezier

[*] Use dimen=middle for circles and sectors in PSTricks

[*] Set dashadjust=false in PSTricks for compatibility with other 
 output formats

[*] Dots in dotted lines are now square (they where rectangular).
 When loading old TpX files the width of dotted lines is
 adjusted to make them somewhat more similar to the previous
 appearance.

[+*] Freehand Bezier curve instead of freehand polyline

[+] "Delete small objects" operation

[-] Fixed latexeps, latexpdf and latexcustom export for 
pgf/tikz (images were too wide in some situations)

=========================================
2007-08-04 TpX Version 1.4
=========================================

[*] Arrows in "Object properties" dialog only for 
 relevant objects

[-] Incorrect \centering for TeXFigure=none

=========================================
2007-07-07 TpX Version 1.4 beta 
 + TpX Lazarus 1.4 alpha 2 released
=========================================

[*] TpX internals rewritten to a great extent.
 More modular source code

[+] Cross-platform variant of TpX implemented using Lazarus

[*-] New version of TpX file format, version 4. The format for 
 storing ellipses changed (angle now is measured 
 counterclockwise, which is more logical). PicUnutLength
 replaced by BitmapRes

[+*] Output formats (LaTeX picture, PSTricks, PGF, TikZ, MetaPost) 
 use the same coordinates as TpX drawing. This is useful for 
 generating code

[+] TikZ output format

[-] "Save as" dialog did not use default extension

[+] Local popup menu: Copy, Paste, Cut,
 Delete, Duplicate, Object properties,
 Convert to, Add point, Delete point, Break path

[+] More stable "LaTeX EPS"

[+*] Epstopdf perl script replaced by direct use of 
 GhostScript

[+] Better grid and ruler divisions

[*] Dotted lines in PSTricks output format are now similar to
 dotted lines in other formats

[+] Graphical objects alignment

[+*] More accurate addition of point to path

[+] Rectangles with rounded corners. (RX and RY
 properties of a rectangle).

[+] "Save as" now shows prompt when overwriting file

[+] "Simplify polyline/polygon" operation

[+] "Reverse points" operation

[+] "Connect paths" operation

[+] Breaking of paths with mouse (Ctrl+Alt+MouseClick)

[+] Arrow-heads for arcs

[*+] Better arrow-heads directions for curves

[*+] Picture properties added to undo

[+] HiResBoundingBox in EPS

[+] Mouse drag on empty space starts area selection mode

[+] Reverse points order in table editor

[+] Freehand polyline draw

[+] Drag-copy with Ctrl+Mouse

[*] Convert to grayscale is applied to selection if any 
 or the whole drawing otherwise

[-] Ellipse and rectangle duplication did not work

=========================================
2006-05-22 TpX Version 1.3 released
=========================================

=========================================
2006-04-06 TpX Version 1.3 beta 2 released
=========================================

[+] New export format "LaTeX EPS" with tight bounding box 
 (using dvips) and derivatives (PDF using epstopdf, various 
 GhostScript formats) 

[+] Custom system fonts for graphical objects
 (not applies to LaTeX output)

[*] Simpler hot keys for graphical objects

[+] Additional hot keys

[-] A bug in saving of arrow-heads information to TpX file

=========================================
2006-01-31 TpX Version 1.3 beta released
=========================================

[*] New version of TpX file format, version 3. The format for 
 storing rectangles changed

[-] \pgfsetmiterlimit fixed

[+] Preview EPS/PDF files in 'Open' dialog
 (if GhostscriptPath is set)

[+] View source

[*] Open and Import EMF/EPS dialogs merged

[*] When TeXCenterFigure is 1 and TeXFigure is none then
 the picture is surrounded by {center} environment

[+] A new kind of graphical primitive, "symbol"

[+] "Arrow-head size factor" property for arrow-heads

[+] "Star size factor" property for stars

[+] BezierPrecision setting

[+] 4 new shapes for stars

[+] Native import of simple SVG pictures

[+] New LaTeX and PdfLaTeX output format, 'none'

[-] ANSI-string text in EMF was incorrectly treated as Widestring

[+] Many new styles of arrow-heads

[+] Program now controls changes made to drawing (no more annoying 
 'save drawing' dialog when there were no changes)

[+] New command line options for running TpX without GUI

=========================================
2005-08-08 TpX Version 1.2 released
=========================================

[+] HatchingLineWidth option for drawing

[-] Delay in refreshing Bezier path position when moving
 control points

[*] Conversion of graphical object to another graphical object
 does not change its order

[*] Use ifpdf to detect whether PdfTeX running in PDF mode

=========================================
2005-07-20 TpX Version 1.2beta released
=========================================

[+] Classical Bezier paths

[+] Paste EMF/WMF from clipboard

[+] Picture info

[+] Edit coordinates of control points. Data could be copied and 
 pasted from another application

[+] "Image tool" for metafiles. Includes EPS printing

[+] TpXpy, Python module to generate TpX drawings

[+] Buttons to change basic properties of several objects

[+] PGF TeX format (suitable both for LaTeX and PdfLaTeX)

[-] Incorrectness in PSTricks circles and segments
 (line width was part of diameter)

[+] Rotated text

[*] New version of TpX format, v="2"
 (needed to take into account new text height convention)

[+] Text height convention changed. Now text height does not 
 include "internal leading" used for accents by Windows GDI

[-] Filling of Bezier paths in PSTricks was done
 incorrectly

[+] Dropdown menus for TeX preview buttons to change
 output format

[+] Conversion of graphical objects (like ellipse to
 spline, etc.)

[-] PicScale ??

[-] Fill rule was inconsistent between formats.
 Now TpX uses "nonzero winding" rule everywhere
 (not "even-odd" aka "alternate" fill rule)
 /See documentation on SVG, PS, PDF or Windows GDI
  about fill rule/

[*] Moving control points of rectangle or ellipse without
 changing direction of it's edges; more natural 
 moving control points of circular primitives

[+] LaTeX->DVI->PS preview

[+] Choose Windows font

[+] PDF compression

[+] Preserve text color when importing from EMF 

[+] Convert to grayscale

=========================================
2005-02-27 TpX Version 1.1 released
=========================================

[-] Incorrect drawing of polylines in bitmaps when
 first and last points coincide

[+] Miter limit for the whole picture. This could be used
 to remove strange spikes at line joins. Visible at Plot3D.TpX
 sample picture from TpX distribution

[+] Antialiased text in bitmaps (PNG, BMP)

[+] Import old Windows metafiles (WMF)

=========================================
2005-02-11 TpX Version 1.1beta released
=========================================

[+] ".TpX" extension could be associated with TpX

[*+] SVGMagnif replaced by PicMagnif and applies to all formats, 
 not just SVG. Could be used to scale the whole drawing,
 changing the meaning of millimeters (e.g. LineWidth, StarsSize)

[-] Incorrect text alignment when importing EMF

[-] Sometimes text was imported incorrectly from EMF

[+] EPS and PDF import using PsToEdit

[*] Use Windows temporary directory for temporary files

[-] Arrow-heads were drawn somewhat inaccurately

[+] "Recent files" menu

[+] Preview LaTeX, PdfLaTeX

[+] Preview EPS, PDF, SVG, PNG, BMP, EMF

[+] EPS and PDF are surrounded by TeX picture environment
 to produce consistent text labels. EPS and PDF are now defaults 
 for LaTeX and PdfLaTeX respectively

[+] 10 additional star shapes (previously there was only one 
 shape - circle)

[*] PicScale (scale in mm per world unit) instead of 
 PicWidth/PicHeight

[-] Unstable algorithm was used for calculation closed splines

[+] Scrollbars to move viewport

[+] Mouse wheel: move and zoom viewport

[+] Line (text) color, hatching color, fill color

[-] Incorrect vertical text alignment in TeX-picture, PSTricks 
 and MetaPost formats

[-] Incorrect font size in MetaPost format when using 
 btex...etex

[*] TeX font size selection using \fontsize{}{}\selectfont
 (TeX picture, PSTricks, MetaPost btex...etex)

=========================================
2004-10-31 TpX Version 1.0.1 released
=========================================

[+] PDF from EPS using epstopdf

[+] Type 1 fonts in EPS

[-] Incorrect help about WinEdt installation (edit TpX_menu.dat, 
 not install_TpX.edt)

[-] Ini file location was not linked to exe file path

[-] Error when running on Windows system with comma set as a 
 decimal point

=========================================
2004-10-24 TpX Version 1.0 released
=========================================


Acknowledgements
 =========================

Modules used in TpX:

  CADSYS 4.0
  Copyright (c) 2001 Piero Valagussa
  pivalag[@@@]tin.it

  Graphics32 library
  Copyright (c) 2000-2004 Alex Denisov and Contributors
  http://graphics32.org

  PowerPdf library, ver 0.9
  Takeshi Kanno
  http://www.est.hi-ho.ne.jp/takeshi_kanno/powerpdf/

  XML library
  Copyright (c) 2002 Ravil Batyrshin, Mikhail Vlasov (Aravil Software)
  http://www.torry.net/vcl/internet/html/mvrbxmlparsers.zip

  PNG Component
  Copyright (c) Gustavo Huffenbacher Daud,
  http://pngdelphi.sourceforge.net

  HTML Help Kit for Delphi,
  Copyright (c) 1999 The Helpware Group
  http://www.helpware.net

  MD5 Message-Digest for Delphi
  Copyright (c) 1997-1999 Medienagentur Fichtner & Meyer
  Written by Matthias Fichtner
  http://www.fichtner.net/delphi/md5.delphi.phtml

  StitchSAX 1.1 - Trivial SAX parser for Delphi
  Copyright (c) 2002, Roman Poterin
  poterin[@@@]mail.ru

  Paszlib
  Copyright (c) 1998,1999,2000,2001 by Jacques Nomssi Nzali
  http://www.nomssi.de/paszlib/paszlib.html

Links
 =========================

Some links to similar and related programs

  LaTeXDraw
  http://latexdraw.sourceforge.net/

  jPicEdt
  http://www.jpicedt.org/

  Xfig
  http://www.xfig.org/

  WinFIG
  http://www.schmidt-web-berlin.de/winfig/

  Metagraf
  http://w3.mecanica.upm.es/metapost/metagraf.php

  Ipe
  http://tclab.kaist.ac.kr/ipe/

  JpgfDraw
  http://theoval.cmp.uea.ac.uk/~nlct/jpgfdraw/index.html

  Mayura Draw
  http://www.mayura.com/

  Graphics Layout Engine
  http://glx.sourceforge.net/

  LaTeXPiX
  http://www.beurden.cjb.net/latexpix.htm

  TeXCAD
  http://homepage.sunrise.ch/mysunrise/gdm/texcad.htm

  TeXCad32
  http://www.gelbes-rechenbuch.de/Texcad32/Index_e.html

  ePiX
  http://mathcs.holycross.edu/~ahwang/current/ePiX.html

  OLETeX Utility
  http://oletex.sourceforge.net/

  pstoedit
  http://www.pstoedit.net/

-------------------------------
TpX 1.5 readme file
Generated 2008-12-07 15:14:54
