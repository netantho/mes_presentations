Création d'une charte graphique avec Bootstrap
==============================================

---

Boot quoi ?
===========

<img src="img/bootstrap_homepage.png" width=800 />

Des classes CSS pour faire une charte graphique pro

* Facilement
* Rapidement

---

Fonctionnalités
===============

<!--
<head>
<link type="text/css" rel="stylesheet" href="twitter-bootstrap-c52368d/bootstrap/css/bootstrap.min.css" />
<link type="text/css" rel="stylesheet" href="twitter-bootstrap-c52368d/bootstrap/css/bootstrap-responsive.min.css" />
</head>
-->

* Scaffolding : Outils pour réaliser un prototype de design
    * Grille : Découpage en colonnes tel un tableau <strike>Excel</strike> Libreoffice Calc
    * Responsive design : Interface adaptée à une TV, un PC, un smartphone, une tablette, ... Démo !
* CSS de base : Formulaires, tableaux, ...
* Composants : Boutons, onglets, listes, barres de navigation, ...
* Plugins javascript

---

Principes de base
=================

Installation
------------

* Télécharger bootstrap
* Dans le bloc délimité par la balise head, ajouter

        !html
        <link href="css/bootstrap.min.css" rel="stylesheet">

Utilisation
-----------

Associer les éléments HTML à des classes CSS prédéfinies dans bootstrap

Exemple :

    !html
    <span class="label label-success">Success</span>

<img src="img/success.png" />

---

Grille
======


* Grille de 12 colonnes
* Chaque zone est encore divisible en 12 colonnes

<img src="img/grille.png" />


---

Grille - Exemple d'utilisation
==============================

<img src="img/grille_demo.png" />

    !html
    <div class="container-fluid">
        <div class="row-fluid">
            <div class="span2">
                <!-- Barre latérale -->
            </div>
            <div class="span10">
                <!-- Corps -->
            </div>
        </div>
    </div>

---

Responsive Design
=================

Installation
------------

* Dans le bloc délimité par la balise head, ajouter

        !html
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="css/bootstrap-responsive.min.css" rel="stylesheet">

Utilisation
-----------

<img src="img/responsive_design.png" />

---

Au boulot !
===========
