# Générateur de M et P pour la Méthode Somme Produit
Un programme python fait sans modules permetant de trouver m et p dans un trinome pour la [méthode Produit-Somme](https://fr.wikipedia.org/wiki/M%C3%A9thode_du_produit-somme)
## Installation
Utilisez la fonction MPS(ac, b), qui retournera [m, p].
## Pourquoi ne pas directement retourner l'expression factorisée ?
Je suis actuellement Lycéen et je comptes transférer ce programme sur ma calculatrice.
J'ai ici simplement automatisé la recherche de m et p pour passer l'étape du "faire joujour avec les facteurs" pusique je suis très mauvais en calculs mentaux et que ça ne demande pas vraiment de technique ou de méthode.
Néanmoins la factorisation est un procédé important à maitriser, faire un programme me donant l'expression factorisée serait de la triche et peu intéressant pour moi.
Si vous cherchez tout de même un script capable de factoriser vous trouverez chaussure à votre pied sur github ;)
## Tests
### Input
Je veux factoriser l'expression 9x^2-12x-45, j'entre donc [9*-45, -12].
### Output
On me retourne [15, -27], j'ai donc l'expression `9x^2-27x+15x-45` qui me donne `3x(3x-9)+5(3x-9)` que je remet en évidence `(3x+5)(3x-9)` que je peux réduire par `3(x-3)(3x+5)` et tada !
