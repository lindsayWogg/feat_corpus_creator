-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost
-- Généré le : jeu. 23 fév. 2023 à 06:21
-- Version du serveur : 10.4.24-MariaDB
-- Version de PHP : 8.0.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `taln`
--

-- --------------------------------------------------------

--
-- Structure de la table `corpus`
--

CREATE TABLE `corpus` (
  `id` int(11) NOT NULL,
  `titre` varchar(100) NOT NULL,
  `filename` varchar(100) NOT NULL,
  `path` varchar(500) NOT NULL,
  `categorie` varchar(50) DEFAULT NULL,
  `status` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `corpus`
--

INSERT INTO `corpus` (`id`, `titre`, `filename`, `path`, `categorie`, `status`) VALUES
(13, 'fihibohana', 'corpus_1.txt', '/home/lindsay/Documents/Projets/Mémoire/Création_de_corpus/31-08-2022/corpora/corpus_1.txt', NULL, 0),
(14, 'fitsapàna', 'corpus_2.txt', '/home/lindsay/Documents/Projets/Mémoire/Création_de_corpus/31-08-2022/corpora/corpus_2.txt', NULL, 0),
(15, 'test', 'corpus_3.txt', '/home/lindsay/Documents/Projets/Mémoire/Création_de_corpus/31-08-2022/corpora/corpus_3.txt', NULL, 0),
(18, 'andrana', 'corpus_6.txt', '/home/lindsay/Documents/Projets/Mémoire/Création_de_corpus/31-08-2022/corpora/corpus_6.txt', NULL, 0),
(22, 'Fianarana', 'corpus_5.txt', '/home/lindsay/Documents/Projets/Mémoire/Création_de_corpus/31-08-2022/corpora/corpus_5.txt', 'Fianarana', 1),
(23, 'essai', 'corpus_6.txt', '/home/lindsay/Documents/Projets/Mémoire/Création_de_corpus/31-08-2022/corpora/corpus_6.txt', NULL, 0);

-- --------------------------------------------------------

--
-- Structure de la table `mpampiasa`
--

CREATE TABLE `mpampiasa` (
  `id` int(11) NOT NULL,
  `anarana` varchar(25) NOT NULL,
  `fanampiny` varchar(25) NOT NULL,
  `solon_anarana` varchar(25) NOT NULL,
  `teny_miafina` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `mpampiasa`
--

INSERT INTO `mpampiasa` (`id`, `anarana`, `fanampiny`, `solon_anarana`, `teny_miafina`) VALUES
(4, 'Andriamanantena', 'Lindsay Wogg', 'Lindsay', 'wogg'),
(5, 'Nivo', 'Randriambololona', 'nivo', '0000');

-- --------------------------------------------------------

--
-- Structure de la table `teny`
--

CREATE TABLE `teny` (
  `id` int(11) NOT NULL,
  `teny` varchar(50) NOT NULL,
  `sokajy` varchar(50) DEFAULT NULL,
  `voasokajy` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `teny`
--

INSERT INTO `teny` (`id`, `teny`, `sokajy`, `voasokajy`) VALUES
(2687, 'Anisan', '0', 0),
(2688, 'ireo', '0', 0),
(2689, 'nisedra', '0', 0),
(2690, 'olana', '0', 0),
(2691, 'manokana', '0', 0),
(2692, 'koa', '0', 0),
(2693, 'aho', '0', 0),
(2694, 'tamin', '0', 0),
(2695, 'Ny', 'Mpampitohy', 1),
(2696, 'voalohandohan', '0', 0),
(2697, 'fihibohana', '0', 0),
(2699, 'famakiana', '0', 0),
(2700, 'lahatsoratra', 'Mpanoritra', 1),
(2701, 'tato', '0', 0),
(2702, 'amin', '0', 0),
(2703, 'blaogy', '0', 0),
(2704, 'no', 'Mpampitohy fehezan-teny', 1),
(2705, 'anisany', '0', 0),
(2706, 'nanampy', '0', 0),
(2707, 'ahy', '0', 0),
(2708, 'Mety', '0', 0),
(2709, 'misy', '0', 0),
(2710, 'tahaka', '0', 0),
(2711, 'any', '0', 0),
(2712, 'ho', 'Mpamaritra', 1),
(2713, 'mila', '0', 0),
(2714, 'fanohanana', '0', 0),
(2715, 'sy', '0', 0),
(2716, 'fankaherezana', '0', 0),
(2717, 'Izany', '0', 0),
(2718, 'nahatapakevitra', '0', 0),
(2719, 'hamoaka', '0', 0),
(2720, 'ity', 'Mpanoritra', 1),
(2721, 'boky', '0', 0),
(2722, 'izao', '0', 0),
(2723, 'fotoana', '0', 0),
(2724, 'Tsy', '0', 0),
(2725, 'izay', '0', 0),
(2726, 'ihany', '0', 0),
(2727, 'anefa', 'Mpampiankin-teny', 1),
(2728, 'fa', '0', 0),
(2729, 'toetsaina', '0', 0),
(2730, 'mpandresy', '0', 0),
(2731, 'fijery', '0', 0),
(2732, 'miabo', '0', 0),
(2733, 'mihitsy', '0', 0),
(2734, 'tiana', '0', 0),
(2735, 'avchitra', '0', 0),
(2736, 'ao', '0', 0),
(2737, 'anatin', 'Mpanoritra', 1),
(2738, 'Maro', '0', 0),
(2739, 'hafatra', '0', 0),
(2740, 'an', '0', 0),
(2741, 'mikasa', '0', 0),
(2742, 'hanangana', '0', 0),
(2743, 'orinasa', '0', 0),
(2744, 'na', '0', 0),
(2745, 'tetikasa', '0', 0),
(2746, 'maniry', '0', 0),
(2747, 'hanatanteraka', '0', 0),
(2748, 'nofinofy', '0', 0),
(2749, 'ary', '0', 0),
(2750, 'olona', '0', 0),
(2751, 'hivelatra', '0', 0),
(2752, 'hijoro', '0', 0),
(2753, 'hahomby', '0', 0),
(2754, 'hiaina', '0', 0),
(2755, 'malalaka', '0', 0),
(2756, 'Fanaonny', '0', 0),
(2757, 'Blaogin', '0', 0),
(2758, 'i', '0', 0),
(2759, 'Voniary', '0', 0),
(2760, 'hatrany', '0', 0),
(2761, 'manolotra', '0', 0),
(2762, 'voambolantsehatra', '0', 0),
(2764, 'latsadanja', '0', 0),
(2766, 'indray', '0', 0),
(2767, 'mitoraka', '0', 0),
(2768, 'satria', '0', 0),
(2769, 'mba', '0', 0),
(2770, 'hanampy', '0', 0),
(2771, 'rehetra', '0', 0),
(2772, 'dia', 'Mpampitohy', 1),
(2773, 'nasiana', '0', 0),
(2774, 'voambolana', '0', 0),
(2775, 'momba', '0', 0),
(2776, 'fampivelarana', '0', 0),
(2777, 'mahaolona', '0', 0),
(2778, 'dikanteny', '0', 0),
(2779, 'malagasy', '0', 0),
(2780, 'frantsay', '0', 0),
(2781, 'frandohanny', '0', 0),
(2782, 'Indro', '0', 0),
(2783, 'hevitr', '0', 0),
(2784, 'Nivo', '0', 0),
(2785, 'Lalandy', '0', 0),
(2786, 'mpandrindra', '0', 0),
(2787, 'pejy', '0', 0),
(2788, 'Natioraly', '0', 0),
(2789, 'Happy', '0', 0),
(2790, 'mivoy', '0', 0),
(2791, 'isambatar', '0', 0),
(2792, 'alalan', '0', 0),
(2793, 'fankafizana', '0', 0),
(2794, 'volo', '0', 0),
(2795, 'natoraly', '0', 0),
(2796, 'sadly', '0', 0),
(2797, 'mpampianatra', '0', 0),
(2798, 'Yoga', '0', 0),
(2800, 'aad', '0', 0),
(2801, 'santinuent', '0', 0),
(2802, 'utiliser', '0', 0),
(2803, 'ce', '0', 0),
(2804, 'si', '0', 0),
(2805, 'Cook', '0', 0),
(2806, 'es', '0', 0),
(2807, 'voir', '0', 0),
(2808, 'Paliticse', '0', 0),
(2809, 'r', '0', 0),
(2810, 'eccepter', '0', 0),
(2811, 'leurut', '0', 0),
(2812, 'satior', '0', 0),
(2813, 'x', '0', 0),
(2814, 'cockies', '0', 0),
(2815, 'Ask', '0', 0),
(2816, 'questions', '0', 0),
(2817, 'Seay', '0', 0),
(2818, 'Fermer', '0', 0),
(2819, 'et', '0', 0),
(2820, 'accepter', '0', 0),
(2824, 'natokana', 'Mpampiankin-teny', 1),
(2825, 'hoanny', '0', 0),
(2826, 'fitsapna', '0', 0),
(2829, 'hatao', 'Tenim-piontanana', 1),
(2830, 'fitsapana', 'Mpamaritra', 1),
(2831, 'hoan', '0', 0),
(2838, 'hanaovana', 'Mpampiankin-teny', 1),
(2975, 'fianarana', 'Anarana', 1),
(2977, 'lova', 'Anarana', 1),
(2978, 'tsara', 'Mpanoritra', 1),
(2979, 'indrindra', 'Mpampiankin-teny', 1),
(2980, 'Miezaha', 'Matoanteny', 1),
(2981, 'mafy', 'Matoanteny', 1),
(2982, 'dieny', 'Mpampiankin-teny', 1),
(2983, 'mbola', 'Mpampiankin-teny', 1),
(2984, 'afaka', 'Tenim-piontanana', 1),
(2985, 'ianao', 'Mpisolo', 1),
(2986, 'hanomananao', 'Matoanteny', 1),
(2988, 'hoavinao', 'Mpamaritra', 1);

-- --------------------------------------------------------

--
-- Structure de la table `tmp_corpus`
--

CREATE TABLE `tmp_corpus` (
  `id` int(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `tmp_corpus`
--

INSERT INTO `tmp_corpus` (`id`) VALUES
(1);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `corpus`
--
ALTER TABLE `corpus`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `mpampiasa`
--
ALTER TABLE `mpampiasa`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `teny`
--
ALTER TABLE `teny`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `teny` (`teny`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `corpus`
--
ALTER TABLE `corpus`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT pour la table `mpampiasa`
--
ALTER TABLE `mpampiasa`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT pour la table `teny`
--
ALTER TABLE `teny`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3170;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
