# DLR Corporate Design for Python

The specifications of the [DLR Corporate Design](https://intranet.dlr.de/Seiten/f1cee728-0e4b-41d3-a092-6ac48689d9fa/Inhalt/Richtlinien%20zur%20visuellen%20Gestaltung%20(CD-Handbuch).aspx?itemid=d21e9728-ce84-41b0-8eae-c922107e6b11&containerid=d755d16b-0e19-4ea3-9c18-3a3809b386cf&vTerms=InfoAndToolsNonTopic&termId=f1cee728-0e4b-41d3-a092-6ac48689d9fa) as default settings for Matplotlib and seaborn plots.
This includes especially the colors and font (Frutiger).
Comments and change requests are welcome.

![Example line plot](<./examples/lineplot.png>)*Example line plot with seaborn.lineplot()*

## Usage & Installation
The easiest way is to simply include dlr_style as a module. To do this, download [dlr_style.py](<dlr.style.py>) and place it either in the root directory or location of choice. 
```
import dlr_style
```
This can also happen with path specification
```
import sys
sys.path.append("../") #path to dlr_style.py
import dlr_style
```
Running [dlr_style.py](<dlr.style.py>) directly creates the example styles in the example subfolder.

For heatmaps or many plots it can be useful to limit oneself to a few colors but to have an arbitrary number (n_colors) of gradations. For this purpose a corresponding color palette can be created using:
```
dlr_style.get_blend_palette(n_colors=12))
```
![timeseries_facets plot](<./examples/timeseries_facets.png>)*Example line plot with a blend palette*



## Project status
Project currently maintained by Jan Wagner.

Institute of Aerodynamics and Flow Technology| Institut für Aerodynamik und Strömungstechnik \
Experimental Methods (AS-EXV) | Experimentelle Verfahren (AS-EXV) | \
Bunsenstr. 10 | 37073 Göttingen

M.Sc. Jan Wagner |Research assistant |Wissenschaftlicher Mitarbeiter
<!-- Third-party DLR contact info removed pre-publication; see docs/redaction-policy.md (R-AUDIT-08a). -->

