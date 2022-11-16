---
layout: post
title:  "Erstellen einer Webseite mit Jekyll und GitHub Pages"
date:   2022-11-16 16:30
tags: howto jekyll github-pages godaddy
description: Eine kurze Einführung darin, wie ich diese Webseite erstellt habe. 
---

In diesem Eintrag möchte ich beschreiben, wie ich diese Webseite technisch erstellt habe, und allen bei der Orientierung helfen, die selbst auch schon immer mal eine eigene Webseite starten wollten. Direkt vorweg: Ich bin kein Frontend-Profi (Bei Webseiten und Apps unterteilt man in der Regel in ein Frontend (die Benutzeroberfläche) und ein Backend (die Datenbank o.Ä., die im Hintergrund läuft)). Ein wichtige Motivation für diese Website war, dass ich mich *learning by doing* in das Thema einarbeiten wollte und will. Korrekturen und Ergänzungen sind daher wärmstens willkommen. 
    

## Schritt 1: Technologieauswahl

Bei der Technologieauswahl gibt es meiner Einschätzung nach 4 grobe Möglichkeiten, die auch die nachfolgenden Schritte beeinflussen bzw. zum Teil sogar überflüssig machen können. Absteigend sortiert nach Coding-Tauchtiefe/manueller Arbeit sehe ich folgende Möglichkeiten:

### Variante 1: “Das Rad neu erfinden”

Jede:r, der in der Schule mal Informatikunterricht besucht hat, hat vermutlich mal eine kleine Webseite in [HTML](https://www.w3schools.com/html/) gebaut. Meinem verwöhnten Generation Y-Eindruck nach wirkt es in vielen Bereichen wie ein zwar etwas mächtigeres, aber auch sehr viel umständlicheres [Markdown](https://de.wikipedia.org/wiki/Markdown). Mit [CSS](https://www.w3schools.com/Css/) kann man gebündelt Stil und Format bestimmter Bausteine festlegen, z.B. dass alle großen Überschriften immer Pink und rechtsbündig sind. Mit HTML und CSS kann man bereits recht viel anstellen, aber für Feinheiten wird man schnell zu [JavaScript](https://www.w3schools.com/js/DEFAULT.asp) greifen, mit dem man z.B. Knöpfe bauen kann, die einen wieder an den Anfang der Seite bringen

### Variante 2: “Ich kenne mich etwas aus und/oder habe zu viel Zeit”

In dieser Kategorie, in die ich mich selbst einordnen würde, verwendet man Website-Builder wie [Jekyll](https://jekyllrb.com/) oder [Hugo](https://gohugo.io/), die eine große Auswahl an vorgefertigten Themes und Funktionalitäten anbieten, die mit etwas Lese- und Schreibverständnis in HTML und CSS angepasst werden können. 

### Variante 3: “Gut & Günstig: Baukasten”

Günstig bezieht sich hierbei nicht unbedingt nur auf die monetären Kosten, sondern vor allem auf die Zeit. Allrounder wie [Wordpress](https://wordpress.com/), [Wix](https://de.wix.com/), [Squarespace](https://de.squarespace.com/), [Jimdo](https://www.jimdo.com/de/) oder [IONOS](https://www.ionos.de/), aber auch traditionelle Hosting-Anbieter wie [Strato](https://www.strato.de/) oder [GoDaddy](https://www.godaddy.com/) (siehe auch [Schritt 4](#schritt-4-hosting-und-domain)) bieten Webseite-Baukästen an und sind damit ein guter No Code-Kompromiss für alle, die zügig und/oder ohne viele Vorkenntnisse eine eigene Webseite bauen und hosten lassen wollen. In der Regel kann man aus verschiedenen Themes wählen und diese leicht anpassen. Wer keine White Label-Domain benötigt, kann oft kostenfrei eine \<frei wählbar\>.\<anbieter\>.com verwenden. 

### Variante 4: “Team Genügsam”

Für alle, die möglichst wenig Aufwand haben möchten und keinen Wert auf Personalisierung legen, sind vermutlich die gängigen Social Media- oder Blogging-Plattformen wie [Medium](https://medium.com/), [Twitter](https://twitter.com), [Instagram](https://www.instagram.com/) oder [LinkedIn](https://www.linkedin.com/) der beste Weg für einen eigenen Blog. Je nach Inhalt und Zielgruppe eignet sich mal die eine, mal die andere Plattform besser, aber im Grunde genommen benötigt man lediglich einen Account, um direkt loslegen zu können. Auch ist es hier möglicherweise am einfachsten, Interaktionen hervorzurufen und eine “Community” aufzubauen.

Im professionellen Umfeld finden all diese Varianten in der Regel keinen Einsatz, auch wenn sich ein Frontend-Entwickler natürlich trotzdem gut mit HTML, CSS und JavaScript auskennen muss. Dort wird mit mächtigeren Frameworks wie [Django](https://www.djangoproject.com/), [Ruby on Rails](https://rubyonrails.org/), [Vue.js](https://vuejs.org/guide/introduction.html), [React](https://reactjs.org/), oder [Angular](https://angular.io/) gearbeitet. Diese wären für eine erste kleine, eigene Webseite wie diese, die so einfach wie möglich sein soll, meinem Eindruck nach etwas Overkill. Vielleicht ja bei meinem nächsten Projekt…

## Schritt 2: Jekyll und alles drum herum

Für *leodreieck.de* habe ich mich für Variante 2 aus Schritt 1 und Jekyll entschieden. Für den Einstieg bin ich einfach dem offiziellen [Jekyll-Guide](https://jekyllrb.com/docs/step-by-step/10-deployment/) gefolgt. Darin wird das Minima-Theme anwendet, eine sehr reduzierte Formatvorlage. Dies war perfekt für mich, da ich so leicht Anpassungen durchführen konnte. Wer möchte, kann aber auch schon [vorgefertigte](https://jekyllrb.com/docs/themes/#overriding-theme-defaults) Themes verwenden. Meine Navigationsleiste habe ich nicht wie im Guide beschrieben, sondern wie in der [GitHub-Dokumentation](https://github.com/jekyll/minima#customize-navigation-links) vorgeschlagen umgesetzt, da mir dies weniger umständlich vorkam. Zuletzt folgte ich für die Verwendung von Tags und der Tag-Wolke im Feed [diesem](http://longqian.me/2017/02/09/github-jekyll-tag/) Blog-Eintrag. Als zusätzliche Orientierung half mir außerdem [dieser](https://www.aleksandrhovhannisyan.com/blog/getting-started-with-jekyll-and-github-pages/) Blog-Eintrag, der sehr ausführlich ist und einige beruhigende Screenshots enthält.

Als Editor verwende ich [Visual Studio Code](https://code.visualstudio.com/) (VSC), den aktuell wohl beliebtesten Editor. Für die Code-Versionierung in GitHub benötigt man außerdem [Git](https://git-scm.com/download/win). Für die Vorbereitung und Planung nutze ich außerdem das wunderbare [Notion](https://www.notion.so/product?fredir=1), mit dem ich quasi mein ganzes Leben plane und dokumentiere.

## Schritt 3: Rechtliches

Vorab ein Disclaimer: Ich bin kein Anwalt und kann unmöglich garantieren, dass das untenstehende ausreicht.

Wenn ich alles richtig verstanden habe, benötigt man bereits sehr schnell ein Impressum und eine Datenschutzerklärung für die eigene Webseite. Die einzige Ausnahme ist eigentlich eine Seite, die wirklich nur für Familie und Freunde gedacht ist (wie z.B. ein Schüleraustausch-Blog). Alles Kommerzielle oder Redaktionelle (auch von zweifelhafter journalistischer Qualität wie diese Seite) braucht ein Impressum und eine Datenschutzerklärung. Glücklicherweise gibt es Angebote wie [eRecht24](https://www.e-recht24.de/), die dabei unterstützen, diese Erklärungen zu erstellen.

Auch wenn es inzwischen manchmal so wirkt, zwingt einen dagegen niemand dazu, ein Cookie-Banner oder eine Aufforderung, Push-Benachrichtigungen zu aktivieren, einzurichten (sofern man keine Cookies platziert). Cookies sind kleine Informationsbrösel, die per se überhaupt nicht schlecht sein müssen und dem Server zB dabei helfen können, die Webseite an das Gerät (Handy oder Computer) anzupassen. Für solche funktionalen Cookies benötigt man meines Wissens nach keine Einwilligung der Besucher:innen. Hilfreiche Cookies, für die man aber bereits ein Banner benötigt, könnten zum Beispiel den Warenkorb auf einer Seite speichern oder die Stelle, auf der man zuletzt aufgehört hatte zu lesen. Analytics-Cookies sind wahrscheinlich der Grund für den allgemeinen Hass auf Cookies und können Google und Konsorten helfen, plattformübergreifend ein Klickprofil zu erstellen. Sie sind auch der Grund, wieso man die ganze Zeit Werbung von Webseiten bekommt, die man mal besucht hat. Private Browserfenster löschen übrigens neben dem Verlauf die Cookies, nachdem man sie geschlossen hat. 

<details>
<summary> <i> Fun Fact/Exkurs/gefährliches Halbwissen: Gutgläubiger Erklärungsansatz, wieso wir Werbung für Dinge sehen, über die wir nur offline gesprochen haben </i></summary>
<p></p>
<p>
Ihr kennt diesen besonders gruseligen Moment sicher auch: am einen Tag spricht man noch mit guten Freund:innen über einen Urlaub auf Bali (ohne ihn im Internet zu suchen!) und am nächsten Tag sieht man auf einmal Werbung für Flüge nach Bali. Das könnte ebenfalls mit den Cookies zusammenhängen. Anhand der Krümel, die wir mit unseren Klicks im Internet hinterlassen, werden “Profile” von uns angelegt (z.B.: Student, Single, keine Kinder, sportlich, …). Wenn jetzt eine Person mit einem sehr ähnlichen Profil (z.B.: gute Freund:innen) nach einem Urlaub in Bali suchen (weil sie zuvor mit ihrem guten Freund Leo darüber geredet haben und sich für einen Moment aus dem kühlen November wegträumen möchten), kann es für den Algorithmus Sinn ergeben, deren Klicks auch anderen ähnlichen Profilen (z.B.: mir!) vorzuschlagen. Ergänzt werden könnte das Ganze noch vom [Baader-Meinhoff-Phänomen](https://en.wikipedia.org/wiki/Frequency_illusion). Sehr gefährliches Halbwissen, aber ich finde, dass das gemäß [Ockhams Rasiermesser](https://de.wikipedia.org/wiki/Ockhams_Rasiermesser) eine ziemlich plausible Erklärung für das Phänomen ist. Exkurs Ende.
</p>
</details>
<p></p>

Da ich aktiv gar keine Cookies sammle und nur im Hintergrund die funktionalen Cookies zur korrekten Darstellung verwendet werden, kommt diese Seite also ohne das elendige Banner aus. 

<a name="schritt-4-hosting-und-domain">
## Schritt 4: Hosting und Domain

Damit eine Website im Internet erreichbar ist, muss sie auf einem Server gehostet werden, der, vereinfacht gesagt, den Anfragenden die Webseite zusendet und, falls vorhanden (z.B. in einem Online-Shop), die Datenbank verwaltet. 

Meine Webseite ist eine statische Website. Das bedeutet, dass bei der Benutzung keine großen Rechenoperationen auf dem Server ausführt werden. Das höchste der Gefühle ist ein Link auf eine andere Webseite. Da solche Webseiten wenig Speicher- und Rechenkapazitäten benötigen, gibt es für sie kostenlose Hosting-Angebote wie [Netlify](https://www.netlify.com/) oder [GitHub Pages](https://docs.github.com/en/pages). Ich nutze GitHub Pages, was wirklich sehr einfach und bequem ist.

Standardmäßig sind Webseiten, die mit GitHub Pages gehostet werden, unter der Domain *\<Nutzername\>.github.io* erreichbar. Wenn man eine eigene, raketencoole Domain wie [leodreieck.de](http://leodreieck.de) nutzen möchte, muss man diese über Domainanbieter wie GoDaddy, IONOS oder Strato reservieren. Auf den ersten (in meinem Fall: ungeschulten) Blick unterscheiden sich die Anbieter kaum; ich habe mich für GoDaddy entscheiden. Gegen eine kleine jährliche Gebühr verwaltet der Anbieter die DNS. Das bedeutet, dass er wie ein Wegweiser Leute, die die Domain eintippen auf den richtigen Server verweist. Um die persönliche Domain in GitHub zu hinterlegen, folgte ich [dieser](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site) Anleitung.