## __Info-Projekt__

---

# Idee

Mathematische Schwingungen können nicht nur als Wellen (Abb.1, rechts), sondern auch als Einheitskreise (Abb.1, links) dargestellt werden:

![gif](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Sinus_und_Cosinus_am_Einheitskreis.gif/800px-Sinus_und_Cosinus_am_Einheitskreis.gif)
>Abb.1: Animation Einheitskreis

Wenn man nun mehrere Schwingungen addiert, kann man zur Visualisierung auch mehrere Einheitskreise "addieren", das heißt die 'Spitze' des einen Einheistkreises als Ausgangspunkt für den zweiten Einheistkreis nutzen:

![gif](https://upload.wikimedia.org/wikipedia/commons/b/bd/Fourier_series_square_wave_circles_animation.svg)
>Abb.2: Animation Addition Schwingungen

Lässt man das letzte Ende dieser addierten Kreise (Abb.2, roter Punkt) eine Linie zeichnen eribt sich ein 2-dimensionale Linie, die in sich geschlossen ist. Diese Formen sind unter anderem in der Astronomie als _Planetenschleifen_ bekannt und waren ein großer Kritikpunkt am geozentrischen Weltbild (Abb.3). Denn, um die Schleifen, die bestimmte Himmelsobjekte am Himmel machen mit dem geozentrischen Weltbild erklären zu können müssten diese Körper merkwürdige Laufbahnen haben (Abb.3, rechts). Genau diese entstehen durch dass addieren der Laufbahnen (d.h. Schwingungen) der Erde und des anderen Himmelskörpers.

![gif](https://upload.wikimedia.org/wikipedia/commons/e/ea/Apparent_retrograde_motion.gif)
>Abb.3: Animation Planetenschleifen geozentr. Weltbild

Wie in Abbildung 2 rechts zu sehen lassen sich durch Addition verschiedener Schwingungen bestimmte Funktionen annähern. Diese Annäherungen werden mit steigender Anzahl N der genutzten Schwingungen zunehmend auflösender.

Dieser Prozess lässt sich mathematisch anhand der _Fourier Analyse_ beschreiben. Diese kann genutzt werden, um Schwingungen in ihre Bestandteile (verschiedene sin und cos Funktionen) zu "zerlegen". In technischer Sprache wird also ein Signal in seine einzelnen Frerquenzen zerlegt

![Image](https://imgur.com/QEgyWxD.png)
>Abb.4: Zerlegung einer Schwingung in ihre Frequenzen. __Spalte 1__: kleinste Schwingung. __Spalte 2__: alle Schwingungen einzelnd dargestellt. __Spalte 3__: alle Schwingungen addiert dargestellt. __Spalte 4__: die "Frequenzen", die in der Schwingung aus Spalte 3 stecken (d.h die "Frequenzen" der Schwingungen aus Spalte 2).