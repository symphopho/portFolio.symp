 -- listing des database 
 /l
-- création d'une database 
create database e_commerce;
-- création de la table commerce
CREATE TABLE commerces (
    id SERIAL PRIMARY KEY,   -- Clé primaire avec auto-incrémentation
    nom VARCHAR(50) NOT NULL, -- Nom du commerçant (obligatoire)
    prenom VARCHAR(50) NOT NULL -- Prénom du commerçant (obligatoire)
);

-- création de la table clients
\l
CREATE TABLE clients (
    id SERIAL PRIMARY KEY,         -- Clé primaire avec auto-incrémentation
    nom VARCHAR(100) NOT NULL,      -- Nom du client (obligatoire)
    prenom VARCHAR(100) NOT NULL,   -- Prénom du client (obligatoire)
    email VARCHAR(255) UNIQUE NOT NULL, -- Email unique et obligatoire
    telephone VARCHAR(20) UNIQUE,   -- Numéro de téléphone unique
    adresse TEXT,                   -- Adresse optionnelle
    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date de création par défaut
);
INSERT INTO clients (nom, prenom, email, telephone, adresse) VALUES
('Dupont', 'Jean', 'jean.dupont@email.com', '0601020304', '10 Rue de Paris, 75001 Paris'),
('Martin', 'Sophie', 'sophie.martin@email.com', '0612345678', '15 Avenue des Champs, 75008 Paris'),
('Lemoine', 'Paul', 'paul.lemoine@email.com', '0622334455', '5 Boulevard Haussmann, 75009 Paris'),
('Bernard', 'Claire', 'claire.bernard@email.com', '0633445566', '8 Rue Lafayette, 75010 Paris'),
('Morel', 'Lucas', 'lucas.morel@email.com', '0644556677', '12 Quai de Seine, 75019 Paris');
select * from clients;
INSERT INTO commerces (id, nom, prenom) VALUES
(1, 'Durand', 'Alice'),
(2, 'Lefevre', 'Thomas'),
(3, 'Moreau', 'Camille'),
(4, 'Dubois', 'Julien'),
(5, 'Lambert', 'Sophie');
select * from commerces;
-- création d'une table produits
CREATE TABLE produits (
    id SERIAL PRIMARY KEY,           -- ID auto-incrémenté
    nom VARCHAR(100) NOT NULL,        -- Nom du produit (obligatoire)
    description TEXT,                 -- Description optionnelle
    prix DECIMAL(10,2) NOT NULL,      -- Prix avec 2 décimales
    stock INT NOT NULL DEFAULT 0,     -- Quantité en stock (par défaut 0)
    date_ajout TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date d'ajout automatique
);
INSERT INTO produits (id, nom, description, prix, stock) VALUES
(1, 'Ordinateur portable', 'PC 15 pouces avec 16Go RAM et 512Go SSD', 899.99, 10),
(2, 'Smartphone', 'Téléphone 5G avec écran OLED', 699.99, 25),
(3, 'Casque Bluetooth', 'Casque sans fil avec réduction de bruit', 149.99, 50),
(4, 'Montre connectée', 'Montre avec capteurs de santé et GPS', 199.99, 30),
(5, 'Clavier mécanique', 'Clavier RGB avec switches rouges', 89.99, 40);
 
 SELECT * from produits;
 --création de la table catégories
 CREATE TABLE categories (
    id SERIAL PRIMARY KEY,               -- ID de la catégorie (auto-incrémenté)
    nom VARCHAR(100) NOT NULL,            -- Nom de la catégorie
    description TEXT                      -- Description de la catégorie
);
INSERT INTO categories (nom, description) VALUES
('Informatique', 'Tous les produits liés à l’informatique, tels que les ordinateurs et accessoires.'),
('Téléphonie', 'Produits et accessoires liés aux téléphones portables.'),
('Audio', 'Casques, écouteurs, haut-parleurs et autres accessoires audio.'),
('Montres connectées', 'Montres intelligentes avec des fonctionnalités de santé et de suivi.'),
('Claviers et Souris', 'Périphériques de saisie comme les claviers mécaniques et souris gamer.');
SELECT * from categories;
DROP TABLE commmerce;
--crétion de la table fournisseurs
CREATE TABLE fournisseurs (
    id SERIAL PRIMARY KEY,               -- ID du fournisseur (auto-incrémenté)
    nom VARCHAR(100) NOT NULL,            -- Nom du fournisseur
    contact VARCHAR(100),                 -- Contact du fournisseur
    adresse TEXT,                         -- Adresse du fournisseur
    telephone VARCHAR(20),                -- Numéro de téléphone
    email VARCHAR(255)                    -- Email du fournisseur
);
INSERT INTO fournisseurs (nom, contact, adresse, telephone, email) VALUES
('TechCorp', 'John Doe', '123 Rue de la Technologie, 75000 Paris', '0102030405', 'contact@techcorp.com'),
('SmartGadgets', 'Sarah Smith', '5 Boulevard des Innovations, 75008 Paris', '0105060708', 'info@smartgadgets.com'),
('AudioMasters', 'Paul Martin', '10 Rue du Son, 75011 Paris', '0112233445', 'contact@audiomasters.com'),
('MobileTech', 'Julie Lefevre', '20 Avenue des Téléphones, 75015 Paris', '0122334455', 'support@mobiletech.com'),
('GizmoWorld', 'Eric Lambert', '3 Place des Accessoires, 75018 Paris', '0133445566', 'contact@gizioworld.com');

\dt

INSERT INTO fournisseurs (nom, contact, adresse, telephone, email) VALUES
('TechCorp', 'John Doe', '123 Rue de la Technologie, 75000 Paris', '0102030405', 'contact@techcorp.com'),
('SmartGadgets', 'Sarah Smith', '5 Boulevard des Innovations, 75008 Paris', '0105060708', 'info@smartgadgets.com'),
('AudioMasters', 'Paul Martin', '10 Rue du Son, 75011 Paris', '0112233445', 'contact@audiomasters.com'),
('MobileTech', 'Julie Lefevre', '20 Avenue des Téléphones, 75015 Paris', '0122334455', 'support@mobiletech.com'),
('GizmoWorld', 'Eric Lambert', '3 Place des Accessoires, 75018 Paris', '0133445566', 'contact@gizioworld.com');
SELECT * FROM fournisseurs;
CREATE TABLE commandes (
    id SERIAL PRIMARY KEY,               -- ID de la commande (auto-incrémenté)
    date_commande TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date de la commande
    total DECIMAL(10,2) NOT NULL,         -- Montant total de la commande
    statut VARCHAR(50) DEFAULT 'En cours', -- Statut de la commande (par défaut 'En cours')
);
INSERT INTO commandes (total, statut) VALUES
(249.99, 'En cours'),
(499.50, 'Livrée'),
(120.00, 'Annulée'),
(189.75, 'En cours'),
(305.40, 'Livrée');
ALTER TABLE commandes ADD COLUMN client_id INTEGER;
ALTER TABLE commandes ADD COLUMN client_id INTEGER;

INSERT INTO commandes (client_id, total, statut) VALUES
(1, 249.99, 'En cours'),
(2, 499.50, 'Livrée'),
(3, 120.00, 'Annulée'),
(4, 189.75, 'En cours'),
(5, 305.40, 'Livrée');
select * FROM commandes;
SELECT c.id AS commande_id, c.date_commande, c.total, c.statut, cl.nom AS client_nom
FROM commandes c
JOIN clients cl ON c.client_id = cl.id;


