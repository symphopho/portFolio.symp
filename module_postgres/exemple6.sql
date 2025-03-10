cd "C:\Program Files\PostgreSQL\17\bin"
./psql -U postgres


ALTER USER postgres WITH PASSWORD 'daria';

 -- listing des database 
 \l
-- création d'une database 
create database e_commerce;

\c e_commerce;
-- création de la table client 
CREATE TABLE client (
    id SERIAL NOT NULL PRIMARY KEY,
    nom VARCHAR(150) NOT NULL,
    prenom VARCHAR(150) NOT NULL,
    email VARCHAR(150)
);
INSERT INTO client (nom, prenom, email) VALUES
('Dupont', 'Jean', 'jean.dupont@email.com'),
('Martin', 'Sophie', 'sophie.martin@email.com'),
('Durand', 'Paul', 'paul.durand@email.com'),
('Lefevre', 'Emma', 'emma.lefevre@email.com'),
('Morel', 'Lucas', 'lucas.morel@email.com');
SELECT * FROM client;


--  création de la table commandes
CREATE TABLE commande (
    id SERIAL NOT NULL PRIMARY KEY,
    date_commande DATE NOT NULL,
    montant DECIMAL(10, 2) NOT NULL,
    client_id INTEGER REFERENCES client(id)
);
INSERT INTO commande (date_commande, montant, client_id) VALUES
('2024-02-01', 150.75, 1),
('2024-02-02', 299.99, 2),
('2024-02-03', 89.50, 3),
('2024-02-04', 450.20, 4),
('2024-02-05', 120.00, 5);
select * from commande;
CREATE TABLE produit (
    id SERIAL NOT NULL PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    prix DECIMAL(10, 2) NOT NULL
);
INSERT INTO produit (nom, prix) VALUES
('Ordinateur portable', 899.99),
('Smartphone', 499.50),
('Casque Bluetooth', 120.00),
('Souris sans fil', 29.99),
('Clavier mécanique', 75.90);
select * from produit;
CREATE TABLE commande_produit (
    commande_id INTEGER REFERENCES commande(id),
    produit_id INTEGER REFERENCES produit(id),
    PRIMARY KEY (commande_id, produit_id)
);
INSERT INTO commande_produit (commande_id, produit_id) VALUES
(1, 2),  -- Commande 1 contient le produit 2
(1, 4),  -- Commande 1 contient aussi le produit 4
(2, 1),  -- Commande 2 contient le produit 1
(3, 3),  -- Commande 3 contient le produit 3
(4, 5);  -- Commande 4 contient le produit 5
select * from commande_produit;




