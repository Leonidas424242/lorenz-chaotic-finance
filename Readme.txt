Pour exécuter ce code, il vous faut les modules suivants :
- numpy
- scipy 
- matplotlib

Si ces modules ne sont pas installés, utilisez la commande suivante : 

pip install numpy scipy matplotlib





But du programme modele_mod.py :

 - Etudier un système d'équations différentielles en variant 3 paramètres rho, sigma, beta.

 - Ce programme a pour objectif de résoudre un système de trois équations différentielles 
   non linéaires dépendant des paramètres rho, sigma et beta. Ces équations modélisent 
   3 dynamiques économiques, à savoir les taux d'intérêt, les stocks et les investissements. 

 - Le programme analyse et calcule aussi les points d'équilibre et leur nature à nouveau
   en fonction de rho, sigma et beta :

      (a) Calcul des points d'équilibre
      (b) Calcul des valeurs propres de la Jacobienne

 Paramètres du programme modele_mod.py : 

  - ρ rho nombre de Rayleigh 
  - σ sigma nombre de Prandtl
  - β beta paramètre sans dimension

Fonctions utilisées dans le programme modele_mod.py: 

 (i) lorenz(t,variables) :
        Définit les 3 équations différentielles
 (ii) résolution() :
        Résout les équations par la méthode RK45, le tout sur un intervalle de temps donné.
 (iii) calcul_eq(sigma, rho, beta) :
        Calcul les points d'équilibres (x_eq,y_eq,z_eq) du système.
 (iv) jacobienne(x, y, z, sigma, rho, beta) :
        Renvoie la matrice Jacobienne du système mesuré au 
        point d'équilibre (x_eq,y_eq,z_eq).
 (v) stabilité(equilibre, sigma, rho, beta) :
        Analyse la stabililté des points d'équilibres.




But du programme finite_differences.py : 

- Définir le système de Lorenz à partir de trois paramètres : ρ (rho), σ (sigma), et β (beta).

- Résoudre le système à l’aide de la méthode de Runge-Kutta d’ordre 4 (RK4).

- Tracer les trajectoires dans les plans (x,y)(x,y), (y,z)(y,z), et (x,z)(x,z).

Paramètres du programme finite_differences.py : 

  - ρ rho nombre de Rayleigh 
  - σ sigma nombre de Prandtl
  - β beta paramètre sans dimension
  - Conditions initiales : Les valeurs initiales des variables x, y, et z.
  - Intervalle de temps : Défini par le temps initial t_0, le temps final t_f, et le pas de temps Δt.

Fonctions utilisées dans le programme finite_differences.py : 

(i) lorenz_deriv(t, xyz, sigma, rho, beta) :
	Calcule les dérivées des variables du système de Lorenz.
(ii) rk4(f, t, xyz, dt, **kwargs) :
	Implémente la méthode de Runge-Kutta pour l’intégration 
	des équations différentielles.
(iii) rk4_lorenz(xyz0, t0, tf, dt, sigma, rho, beta) : 
	Simule le système complet sur un intervalle de temps donné.




But du programme CI-difference.py :

- Résoudre le système de Lorenz à l’aide de la méthode de Runge-Kutta d’ordre 4 (RK4)

- Tracer et comparer les trajectoires issues de deux conditions initiales voisines dans différents plans : (x,y), (y,z), et (z,x).

Paramètres du programme CI-difference.py : 

  - ρ rho nombre de Rayleigh 
  - σ sigma nombre de Prandtl
  - β beta paramètre sans dimension
  - Conditions initiales : Les valeurs initiales proches : (x_0, y_0, z0)=(1.0, 1.0, 1.0) et
	(x_0, y_0, z0)=(1.01, 1.0, 1.0)
  - Intervalle de temps : Défini par le temps initial t_0, le temps final t_f, et le pas de temps Δt.

Fonctions utilisées dans le programme CI-difference.py :

(i) lorenz(t, Y, sigma, rho, beta) :
	Définit le système de Lorenz et calcule les dérivées des variables.
(ii) rk4(f, t0, y0, t_end, h, **kwargs) :
	Implémente la méthode de Runge-Kutta 4ème ordre pour résoudre les équations 			différentielles.
(iii) main() : 
	Simule deux trajectoires proches et produit des visualisations graphiques pour comparer 	leur comportement.
