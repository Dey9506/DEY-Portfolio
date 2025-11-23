import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PGI_PME.settings')
django.setup()

from core.models import *
from django.utils import timezone
from datetime import datetime, timedelta

def populate_database():
    print("Début du peuplement de la base de données...")
    
    # Nettoyer la base
    print("Nettoyage de la base...")
    Client.objects.all().delete()
    Fournisseur.objects.all().delete()
    Categorie.objects.all().delete()
    Produit.objects.all().delete()
    
    # Création des catégories
    print("Création des catégories...")
    categories = [
        {'nom': 'Électronique', 'description': 'Produits électroniques et high-tech'},
        {'nom': 'Vêtements', 'description': 'Vêtements et accessoires de mode'},
        {'nom': 'Maison', 'description': 'Articles pour la maison et décoration'},
        {'nom': 'Sport', 'description': 'Équipements et vêtements de sport'},
        {'nom': 'Livres', 'description': 'Livres et magazines'},
    ]
    
    for cat_data in categories:
        Categorie.objects.create(**cat_data)
    
    # Création des fournisseurs
    print("Création des fournisseurs...")
    fournisseurs = [
        {'nom': 'TechCorp', 'email': 'contact@techcorp.com', 'telephone': '01 23 45 67 89', 'adresse': '123 Rue de la Tech, 75001 Paris'},
        {'nom': 'FashionStyle', 'email': 'info@fashionstyle.com', 'telephone': '01 34 56 78 90', 'adresse': '456 Avenue de la Mode, 69001 Lyon'},
        {'nom': 'HomeDecor', 'email': 'contact@homedecor.com', 'telephone': '02 45 67 89 01', 'adresse': '789 Boulevard de la Maison, 31000 Toulouse'},
        {'nom': 'SportPlus', 'email': 'info@sportplus.com', 'telephone': '03 56 78 90 12', 'adresse': '321 Rue du Sport, 33000 Bordeaux'},
        {'nom': 'BookWorld', 'email': 'contact@bookworld.com', 'telephone': '04 67 89 01 23', 'adresse': '654 Avenue des Livres, 59000 Lille'},
    ]
    
    fournisseur_objects = {}
    for four_data in fournisseurs:
        obj = Fournisseur.objects.create(**four_data)
        fournisseur_objects[four_data['nom']] = obj
    
    # Création des produits
    print("Création des produits...")
    produits = [
        {'nom': 'Smartphone Galaxy X', 'description': 'Smartphone haut de gamme avec écran 6.7"', 'prix': 899.99, 'cout_achat': 550.00, 'stock': 50, 'stock_alerte': 10, 'fournisseur': fournisseur_objects['TechCorp'], 'categorie': Categorie.objects.get(nom='Électronique')},
        {'nom': 'Laptop Pro 15"', 'description': 'Ordinateur portable professionnel', 'prix': 1499.99, 'cout_achat': 900.00, 'stock': 25, 'stock_alerte': 5, 'fournisseur': fournisseur_objects['TechCorp'], 'categorie': Categorie.objects.get(nom='Électronique')},
        {'nom': 'T-shirt Casual', 'description': 'T-shirt en coton bio', 'prix': 29.99, 'cout_achat': 12.00, 'stock': 100, 'stock_alerte': 20, 'fournisseur': fournisseur_objects['FashionStyle'], 'categorie': Categorie.objects.get(nom='Vêtements')},
        {'nom': 'Jean Slim', 'description': 'Jean slim fit délavé', 'prix': 79.99, 'cout_achat': 35.00, 'stock': 75, 'stock_alerte': 15, 'fournisseur': fournisseur_objects['FashionStyle'], 'categorie': Categorie.objects.get(nom='Vêtements')},
        {'nom': 'Canapé 3 places', 'description': 'Canapé en tissu gris', 'prix': 699.99, 'cout_achat': 400.00, 'stock': 10, 'stock_alerte': 2, 'fournisseur': fournisseur_objects['HomeDecor'], 'categorie': Categorie.objects.get(nom='Maison')},
        {'nom': 'Table basse design', 'description': 'Table basse en bois et métal', 'prix': 199.99, 'cout_achat': 100.00, 'stock': 15, 'stock_alerte': 3, 'fournisseur': fournisseur_objects['HomeDecor'], 'categorie': Categorie.objects.get(nom='Maison')},
        {'nom': 'Vélo de course', 'description': 'Vélo de course carbone 21 vitesses', 'prix': 1299.99, 'cout_achat': 800.00, 'stock': 8, 'stock_alerte': 2, 'fournisseur': fournisseur_objects['SportPlus'], 'categorie': Categorie.objects.get(nom='Sport')},
        {'nom': 'Tapis de yoga', 'description': 'Tapis de yoga antidérapant', 'prix': 39.99, 'cout_achat': 15.00, 'stock': 50, 'stock_alerte': 10, 'fournisseur': fournisseur_objects['SportPlus'], 'categorie': Categorie.objects.get(nom='Sport')},
        {'nom': 'Roman best-seller', 'description': 'Dernier roman à succès', 'prix': 19.99, 'cout_achat': 8.00, 'stock': 200, 'stock_alerte': 30, 'fournisseur': fournisseur_objects['BookWorld'], 'categorie': Categorie.objects.get(nom='Livres')},
        {'nom': 'Guide de voyage', 'description': 'Guide complet pour voyageurs', 'prix': 24.99, 'cout_achat': 10.00, 'stock': 80, 'stock_alerte': 15, 'fournisseur': fournisseur_objects['BookWorld'], 'categorie': Categorie.objects.get(nom='Livres')},
    ]
    
    produit_objects = {}
    for prod_data in produits:
        obj = Produit.objects.create(**prod_data)
        produit_objects[prod_data['nom']] = obj
    
    # Création des clients
    print("Création des clients...")
    clients = [
        {'nom': 'Marie Dubois', 'email': 'marie.dubois@email.com', 'telephone': '06 12 34 56 78', 'adresse': '12 Rue de la Paix, 75002 Paris'},
        {'nom': 'Pierre Martin', 'email': 'pierre.martin@email.com', 'telephone': '06 23 45 67 89', 'adresse': '34 Avenue des Champs, 69002 Lyon'},
        {'nom': 'Sophie Bernard', 'email': 'sophie.bernard@email.com', 'telephone': '06 34 56 78 90', 'adresse': '56 Boulevard de la Liberté, 31002 Toulouse'},
        {'nom': 'Thomas Petit', 'email': 'thomas.petit@email.com', 'telephone': '06 45 67 89 01', 'adresse': '78 Rue du Commerce, 33002 Bordeaux'},
        {'nom': 'Julie Moreau', 'email': 'julie.moreau@email.com', 'telephone': '06 56 78 90 12', 'adresse': '90 Avenue Victor Hugo, 59002 Lille'},
    ]
    
    client_objects = {}
    for client_data in clients:
        obj = Client.objects.create(**client_data)
        client_objects[client_data['nom']] = obj
    
    # Création des commandes
    print("Création des commandes...")
    commandes = [
        {'client': client_objects['Marie Dubois'], 'statut': 'LIVREE'},
        {'client': client_objects['Pierre Martin'], 'statut': 'EXPEDIEE'},
        {'client': client_objects['Sophie Bernard'], 'statut': 'EN_PREPARATION'},
        {'client': client_objects['Thomas Petit'], 'statut': 'CONFIRMEE'},
        {'client': client_objects['Julie Moreau'], 'statut': 'BROUILLON'},
    ]
    
    commande_objects = []
    for i, cmd_data in enumerate(commandes):
        # Créer la commande avec une date différente pour chaque
        date_cmd = timezone.now() - timedelta(days=10-i*2)
        cmd = Commande.objects.create(
            client=cmd_data['client'],
            statut=cmd_data['statut'],
            date_commande=date_cmd
        )
        commande_objects.append(cmd)
    
    # Ajouter des lignes de commande
    print("Ajout des lignes de commande...")
    lignes_commandes = [
        # Commande 1 - Marie Dubois
        {'commande': commande_objects[0], 'produit': produit_objects['Smartphone Galaxy X'], 'quantite': 1, 'prix_unitaire': 899.99},
        {'commande': commande_objects[0], 'produit': produit_objects['T-shirt Casual'], 'quantite': 2, 'prix_unitaire': 29.99},
        
        # Commande 2 - Pierre Martin
        {'commande': commande_objects[1], 'produit': produit_objects['Laptop Pro 15"'], 'quantite': 1, 'prix_unitaire': 1499.99},
        {'commande': commande_objects[1], 'produit': produit_objects['Roman best-seller'], 'quantite': 3, 'prix_unitaire': 19.99},
        
        # Commande 3 - Sophie Bernard
        {'commande': commande_objects[2], 'produit': produit_objects['Canapé 3 places'], 'quantite': 1, 'prix_unitaire': 699.99},
        {'commande': commande_objects[2], 'produit': produit_objects['Table basse design'], 'quantite': 1, 'prix_unitaire': 199.99},
        
        # Commande 4 - Thomas Petit
        {'commande': commande_objects[3], 'produit': produit_objects['Vélo de course'], 'quantite': 1, 'prix_unitaire': 1299.99},
        {'commande': commande_objects[3], 'produit': produit_objects['Tapis de yoga'], 'quantite': 1, 'prix_unitaire': 39.99},
        
        # Commande 5 - Julie Moreau
        {'commande': commande_objects[4], 'produit': produit_objects['Jean Slim'], 'quantite': 2, 'prix_unitaire': 79.99},
        {'commande': commande_objects[4], 'produit': produit_objects['Guide de voyage'], 'quantite': 1, 'prix_unitaire': 24.99},
    ]
    
    for ligne_data in lignes_commandes:
        LigneCommande.objects.create(**ligne_data)
    
    # Création des factures pour les commandes livrées ou expédiées
    print("Création des factures...")
    for cmd in commande_objects:
        if cmd.statut in ['LIVREE', 'EXPEDIEE', 'EN_PREPARATION', 'CONFIRMEE']:
            Facture.objects.create(
                commande=cmd,
                montant_total=cmd.total,
                date_echeance=timezone.now() + timedelta(days=30)
            )
    
    # Marquer certaines factures comme réglées
    factures = Facture.objects.all()
    if factures.exists():
        factures[0].reglee = True
        factures[0].save()
        
        factures[1].reglee = True
        factures[1].save()
    
    # Création des employés
    print("Création des employés...")
    employes = [
        {'nom': 'Durand', 'prenom': 'Alice', 'email': 'alice.durand@entreprise.com', 'telephone': '01 11 22 33 44', 'poste': 'Responsable Commercial', 'date_embauche': '2020-01-15', 'salaire': 4500.00},
        {'nom': 'Lefebvre', 'prenom': 'Marc', 'email': 'marc.lefebvre@entreprise.com', 'telephone': '01 22 33 44 55', 'poste': 'Gestionnaire de Stock', 'date_embauche': '2021-03-20', 'salaire': 3200.00},
        {'nom': 'Morel', 'prenom': 'Sarah', 'email': 'sarah.morel@entreprise.com', 'telephone': '01 33 44 55 66', 'poste': 'Assistante Marketing', 'date_embauche': '2022-06-10', 'salaire': 2800.00},
    ]
    
    for emp_data in employes:
        Employe.objects.create(**emp_data)
    
    print("Peuplement de la base de données terminé avec succès!")

if __name__ == '__main__':
    populate_database()