-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 19 Sty 2022, 06:15
-- Wersja serwera: 10.4.21-MariaDB
-- Wersja PHP: 8.0.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `pixelshop`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add user', 6, 'add_user'),
(22, 'Can change user', 6, 'change_user'),
(23, 'Can delete user', 6, 'delete_user'),
(24, 'Can view user', 6, 'view_user'),
(25, 'Can add pixel art', 7, 'add_pixelart'),
(26, 'Can change pixel art', 7, 'change_pixelart'),
(27, 'Can delete pixel art', 7, 'delete_pixelart'),
(28, 'Can view pixel art', 7, 'view_pixelart'),
(29, 'Can add order', 8, 'add_order'),
(30, 'Can change order', 8, 'change_order'),
(31, 'Can delete order', 8, 'delete_order'),
(32, 'Can view order', 8, 'view_order');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(41, '2022-01-19 04:58:07.480906', '6', 'asda1 PLN11.00', 3, '', 7, 25),
(42, '2022-01-19 04:58:07.482898', '5', '12312 sadasd as $12,312,312.00', 3, '', 7, 25),
(43, '2022-01-19 04:58:07.483898', '4', 'dasdasd €12,312,312.00', 3, '', 7, 25),
(44, '2022-01-19 04:58:07.485898', '3', 'jlahdjksahjdka PLN1,231,231.00', 3, '', 7, 25),
(45, '2022-01-19 04:58:07.486913', '2', 'ajajaj12312 PLN12,340.00', 3, '', 7, 25),
(46, '2022-01-19 04:58:07.487934', '1', 'ajajaj PLN241.00', 3, '', 7, 25),
(47, '2022-01-19 05:03:38.888479', '7', 'Deep in mind cave $24.99', 1, '[{\"added\": {}}]', 7, 25),
(48, '2022-01-19 05:04:22.073885', '8', 'Diva €5.00', 1, '[{\"added\": {}}]', 7, 25),
(49, '2022-01-19 05:05:06.419608', '9', 'Fire in the forest PLN19.99', 1, '[{\"added\": {}}]', 7, 25),
(50, '2022-01-19 05:08:42.378996', '10', 'Inside the shop £74.99', 1, '[{\"added\": {}}]', 7, 25),
(51, '2022-01-19 05:10:22.253824', '11', 'Metro PLN119.99', 1, '[{\"added\": {}}]', 7, 25),
(52, '2022-01-19 05:11:01.059707', '12', 'Mountains PLN3.99', 1, '[{\"added\": {}}]', 7, 25);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(8, 'pixelshop', 'order'),
(7, 'pixelshop', 'pixelart'),
(6, 'pixelshop', 'user'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-11-28 14:31:02.298694'),
(2, 'contenttypes', '0002_remove_content_type_name', '2021-11-28 14:31:02.325493'),
(3, 'auth', '0001_initial', '2021-11-28 14:31:02.425666'),
(4, 'auth', '0002_alter_permission_name_max_length', '2021-11-28 14:31:02.445599'),
(5, 'auth', '0003_alter_user_email_max_length', '2021-11-28 14:31:02.450583'),
(6, 'auth', '0004_alter_user_username_opts', '2021-11-28 14:31:02.456562'),
(7, 'auth', '0005_alter_user_last_login_null', '2021-11-28 14:31:02.461546'),
(8, 'auth', '0006_require_contenttypes_0002', '2021-11-28 14:31:02.462542'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2021-11-28 14:31:02.468523'),
(10, 'auth', '0008_alter_user_username_max_length', '2021-11-28 14:31:02.473506'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2021-11-28 14:31:02.478489'),
(12, 'auth', '0010_alter_group_name_max_length', '2021-11-28 14:31:02.488463'),
(13, 'auth', '0011_update_proxy_permissions', '2021-11-28 14:31:02.493439'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2021-11-28 14:31:02.499419'),
(15, 'pixelshop', '0001_initial', '2021-11-28 14:31:02.660879'),
(16, 'admin', '0001_initial', '2021-11-28 14:31:02.709716'),
(17, 'admin', '0002_logentry_remove_auto_add', '2021-11-28 14:31:02.717690'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2021-11-28 14:31:02.727655'),
(19, 'sessions', '0001_initial', '2021-11-28 14:31:02.743602');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0jk0v5p9ei5rx4gze9xsq4qj9vdchcwv', '.eJxVjDsOwjAQBe_iGlm2s-sPJX3OYO3aCw6gRMqnQtwdIqWA9s3Me6lM29rytsich6rOyqE6_Y5M5SHjTuqdxtukyzSu88B6V_RBF91PVZ6Xw_07aLS0b41Mhn2CiLaLcC0SuVrw3pBzXTBSjVhOiMV1SJiK9wAW0YbAySQB9f4A7R425w:1nA2zG:TJ3hA9bFJqTj3ArE3Zis475qfJ5eQpcagfG7V1x6onQ', '2022-02-02 04:54:22.403949'),
('lllombyy9anq3yxelslxeiulndohv8d9', '.eJxVjEEOwiAQRe_C2hAGVIpL9z0DmWEGqRpISrsy3l2bdKHb_977LxVxXUpcu8xxYnVRoA6_G2F6SN0A37Hemk6tLvNEelP0TrseG8vzurt_BwV7-dZHx2B8yjZLkBSGYNLJcsYEGKxlsIZIwgDh7B27bIHFswHxQoIZSL0_9Lo4ug:1myCYL:lSOtUh5avYpWc-mdNRGU2X4b4-nqO0uEBybp_Hvkodc', '2021-12-31 12:41:37.566834'),
('o25sl6aa5ruenudm5svu0y7rqnxha847', '.eJxVjEEOwiAQRe_C2hAGVIpL9z0DmWEGqRpISrsy3l2bdKHb_977LxVxXUpcu8xxYnVRoA6_G2F6SN0A37Hemk6tLvNEelP0TrseG8vzurt_BwV7-dZHx2B8yjZLkBSGYNLJcsYEGKxlsIZIwgDh7B27bIHFswHxQoIZSL0_9Lo4ug:1mrOfx:xFdiQdRS8QdYumkx0TLVGOiQIAG8HQmVJTZ3D7i5HyQ', '2021-12-12 18:13:21.174671'),
('zauqi1gfirv74soxnne5fsjg9k9t5dbp', 'e30:1mzGwO:0NN0OK9xuoWiTKSe7bzLGBvtl8W6xWkr1xBPdljk_5I', '2022-01-03 11:34:52.289685');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `pixelshop_order`
--

CREATE TABLE `pixelshop_order` (
  `id` bigint(20) NOT NULL,
  `date_purchased` datetime(6) NOT NULL,
  `status` varchar(20) NOT NULL,
  `pixelart_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `pixelshop_pixelart`
--

CREATE TABLE `pixelshop_pixelart` (
  `id` bigint(20) NOT NULL,
  `title` varchar(50) NOT NULL,
  `desc` varchar(200) NOT NULL,
  `file` varchar(100) NOT NULL,
  `price_currency` varchar(3) NOT NULL,
  `price` decimal(14,2) NOT NULL,
  `certificate_id` varchar(128) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `pixelshop_pixelart`
--

INSERT INTO `pixelshop_pixelart` (`id`, `title`, `desc`, `file`, `price_currency`, `price`, `certificate_id`) VALUES
(7, 'Deep in mind cave', 'Obraz przedstawiający głęboką jaskinię umysłu.', 'static\\images\\deep_in_mind_cave.png', 'USD', '24.99', '44ac091082cc75607130a807c6fbed64328105c5e47f67bf41ac22b0d60163c9'),
(8, 'Diva', 'Pixelart przedstawiający Divę z gry Overwatch', 'static\\images\\diva_overwatch.png', 'EUR', '5.00', '44ac091082cc75607130a807c6fbed64328105c5e47f67bf41ac22b0d60163c9'),
(9, 'Fire in the forest', 'Obraz lasu w płomieniach', 'static\\images\\fire_in_forest.jpg', 'PLN', '19.99', '44ac091082cc75607130a807c6fbed64328105c5e47f67bf41ac22b0d60163c9'),
(10, 'Inside the shop', 'Pixelart przedstawiający wnętrze sklepiku na przedmieściach. Jego artystyczne podejście do tematu zostało docenione przez najsurowszych krytyków tego typu sztuki.', 'static\\images\\inside_the_shop.jpg', 'GBP', '74.99', '44ac091082cc75607130a807c6fbed64328105c5e47f67bf41ac22b0d60163c9'),
(11, 'Metro', 'Obraz przedstawiający artystyczny pogląd na komunikację miejską.', 'static\\images\\metro.jpg', 'PLN', '119.99', '44ac091082cc75607130a807c6fbed64328105c5e47f67bf41ac22b0d60163c9'),
(12, 'Mountains', 'Piękna kompozycja obrazu ujmująca wzniesienia górskie.', 'static\\images\\mountains.png', 'PLN', '3.99', '44ac091082cc75607130a807c6fbed64328105c5e47f67bf41ac22b0d60163c9');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `pixelshop_user`
--

CREATE TABLE `pixelshop_user` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `pixelshop_user`
--

INSERT INTO `pixelshop_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(23, 'pbkdf2_sha256$260000$6ZSTTg7yGvFbR9RAElsUaa$Xqw4S4YVcJx/kcG3qRBEQIbv8IqBXahIGwjXlxlXPBU=', NULL, 0, 'Ziomek123', 'Marek', 'Kowalski', 'user123@gmail.com', 0, 1, '2022-01-19 04:44:05.000000'),
(24, 'pbkdf2_sha256$260000$nhwzHArLjE3kikZsoXYru6$ekkjCrsQs94D1E503SKBuSL+xWXC/iFrgbmj1D9e3lI=', NULL, 0, 'pracusiek3371', 'Janush', 'Walczuk', 'pracownik123@gmail.com', 1, 1, '2022-01-19 04:51:27.000000'),
(25, 'pbkdf2_sha256$260000$vwBE1XqEJpYFoFoBRfvKUi$3+mufKAWZRA3lBLOrgaibQKLekykerQB3LsPEJeVvpM=', '2022-01-19 05:08:54.871606', 1, 'admin', 'Administrator', 'Tegopodworka', 'admin@pixelshop.com', 1, 1, '2022-01-19 04:53:00.000000');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `pixelshop_user_groups`
--

CREATE TABLE `pixelshop_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `pixelshop_user_user_permissions`
--

CREATE TABLE `pixelshop_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indeksy dla tabeli `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indeksy dla tabeli `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indeksy dla tabeli `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_pixelshop_user_id` (`user_id`);

--
-- Indeksy dla tabeli `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indeksy dla tabeli `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indeksy dla tabeli `pixelshop_order`
--
ALTER TABLE `pixelshop_order`
  ADD PRIMARY KEY (`id`),
  ADD KEY `pixelshop_order_pixelart_id_f4a2f1f7_fk_pixelshop_pixelart_id` (`pixelart_id`),
  ADD KEY `pixelshop_order_user_id_a9d15abf_fk_pixelshop_user_id` (`user_id`);

--
-- Indeksy dla tabeli `pixelshop_pixelart`
--
ALTER TABLE `pixelshop_pixelart`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `pixelshop_user`
--
ALTER TABLE `pixelshop_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indeksy dla tabeli `pixelshop_user_groups`
--
ALTER TABLE `pixelshop_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `pixelshop_user_groups_user_id_group_id_d17f6f0e_uniq` (`user_id`,`group_id`),
  ADD KEY `pixelshop_user_groups_group_id_03e79ec7_fk_auth_group_id` (`group_id`);

--
-- Indeksy dla tabeli `pixelshop_user_user_permissions`
--
ALTER TABLE `pixelshop_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `pixelshop_user_user_perm_user_id_permission_id_39c23ae2_uniq` (`user_id`,`permission_id`),
  ADD KEY `pixelshop_user_user__permission_id_0fe388c5_fk_auth_perm` (`permission_id`);

--
-- AUTO_INCREMENT dla zrzuconych tabel
--

--
-- AUTO_INCREMENT dla tabeli `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT dla tabeli `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT dla tabeli `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT dla tabeli `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT dla tabeli `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT dla tabeli `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT dla tabeli `pixelshop_order`
--
ALTER TABLE `pixelshop_order`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT dla tabeli `pixelshop_pixelart`
--
ALTER TABLE `pixelshop_pixelart`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT dla tabeli `pixelshop_user`
--
ALTER TABLE `pixelshop_user`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT dla tabeli `pixelshop_user_groups`
--
ALTER TABLE `pixelshop_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT dla tabeli `pixelshop_user_user_permissions`
--
ALTER TABLE `pixelshop_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Ograniczenia dla zrzutów tabel
--

--
-- Ograniczenia dla tabeli `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Ograniczenia dla tabeli `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Ograniczenia dla tabeli `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_pixelshop_user_id` FOREIGN KEY (`user_id`) REFERENCES `pixelshop_user` (`id`);

--
-- Ograniczenia dla tabeli `pixelshop_order`
--
ALTER TABLE `pixelshop_order`
  ADD CONSTRAINT `pixelshop_order_pixelart_id_f4a2f1f7_fk_pixelshop_pixelart_id` FOREIGN KEY (`pixelart_id`) REFERENCES `pixelshop_pixelart` (`id`),
  ADD CONSTRAINT `pixelshop_order_user_id_a9d15abf_fk_pixelshop_user_id` FOREIGN KEY (`user_id`) REFERENCES `pixelshop_user` (`id`);

--
-- Ograniczenia dla tabeli `pixelshop_user_groups`
--
ALTER TABLE `pixelshop_user_groups`
  ADD CONSTRAINT `pixelshop_user_groups_group_id_03e79ec7_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `pixelshop_user_groups_user_id_c61e77cb_fk_pixelshop_user_id` FOREIGN KEY (`user_id`) REFERENCES `pixelshop_user` (`id`);

--
-- Ograniczenia dla tabeli `pixelshop_user_user_permissions`
--
ALTER TABLE `pixelshop_user_user_permissions`
  ADD CONSTRAINT `pixelshop_user_user__permission_id_0fe388c5_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `pixelshop_user_user__user_id_579012fa_fk_pixelshop` FOREIGN KEY (`user_id`) REFERENCES `pixelshop_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
