# __Info-Projekt__

# Idee

## Hintergrund

Schwingungen können nicht nur als Wellen (Abb.1, rechts), sondern auch als Einheitskreise (Abb.1, links) dargestellt werden:

![gif](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Sinus_und_Cosinus_am_Einheitskreis.gif/800px-Sinus_und_Cosinus_am_Einheitskreis.gif)
>Abb.1: Animation Einheitskreis

Wenn man nun mehrere Schwingungen addiert, kann man zur Visualisierung auch mehrere Einheitskreise "addieren", das heißt die 'Spitze' des einen Einheistkreises als Ausgangspunkt für den zweiten Einheistkreis nutzen:

![gif](https://upload.wikimedia.org/wikipedia/commons/b/bd/Fourier_series_square_wave_circles_animation.svg)
>Abb.2: Animation Addition Schwingungen

Lässt man das letzte Ende dieser addierten Kreise (Abb.2, roter Punkt) eine Linie zeichnen eribt sich ein 2-dimensionale Linie, die in sich geschlossen ist. Diese Formen sind unter anderem in der Astronomie als _Planetenschleifen_ bekannt und waren ein großer Kritikpunkt am geozentrischen Weltbild (Abb.3). Denn, um die Schleifen, die bestimmte Himmelsobjekte am Himmel machen mit dem geozentrischen Weltbild erklären zu können müssten diese Körper merkwürdige Laufbahnen haben (Abb.3, rechts). Genau diese entstehen durch dass addieren der Laufbahnen (d.h. Schwingungen) der Erde und des anderen Himmelskörpers.

![gif](https://upload.wikimedia.org/wikipedia/commons/e/ea/Apparent_retrograde_motion.gif)
>Abb.3: Animation Planetenschleifen geozentr. Weltbild

Wie in Abbildung 2 rechts zu sehen lassen sich durch Addition verschiedener Schwingungen bestimmte Funktionen annähern. Diese Annäherungen werden mit steigender Anzahl N der genutzten Schwingungen zunehmend höher auflösend.

Dieser Prozess lässt sich mathematisch anhand der _Fourier Analyse_ beschreiben. Diese kann genutzt werden, um Schwingungen in ihre Bestandteile (verschiedene sin und cos Funktionen) zu "zerlegen". In technischer Sprache wird also ein Signal in seine einzelnen Frerquenzen zerlegt

![Image](https://imgur.com/QEgyWxD.png)
>Abb.4: Zerlegung einer Schwingung in ihre Frequenzen. __Spalte 1__: kleinste Schwingung. __Spalte 2__: alle Schwingungen einzelnd dargestellt. __Spalte 3__: alle Schwingungen addiert dargestellt. __Spalte 4__: die "Frequenzen", die in der Schwingung aus Spalte 3 stecken (d.h die "Frequenzen" der Schwingungen aus Spalte 2).

Diese Schwingung muss nicht im Format einer Schwingung im karthesischen Koordinatensystem bereit gestellt werden, sondern kann auch eine durch addierte Einheitskreise zustande gekommene Linie sein.

## Plan

Der Plan ist diese mathemtaische Theorie zu nutzen, um eine beliebige Vektorgraphik mithilfe von addierten Einheitskreisen graphisch an zu nähern. Folgende Eigenschaften soll das Programm also haben:

- Ein Interface, in dem eine svg Datei hochgeladen werden kann
- Die Möglichkeit die Auflösung, anhand der Anzahl an genutzten Einheitskreise, zu ändern

# Umsetzung

Aus den Voraussetzungen ergeben sich folgender grober Ablauf im Programm fast direkt:

- Die svg Datei muss in __eine__ zusammenhängende Linie umgewandelt werden
  - dies kann dadurch passieren, dass sie zuerst in eine Reihe an karthesische Koordinaten umgewandelt wird
  - und dann mit eine _Bezier Kurve_ angenähert wird
- Die daraus resultierende zusammenhängende Linie muss mithilfe der _Fourier Analyse_ in einzelne Schwingungen zerlegt werden
- Die Schwingungen müssen als addierte Einheitskreise gerendert werden
- Am Ende der Kreise muss eine Linie gezeichnet werden
