CREATE TABLE IF NOT EXISTS geos(
    id INTEGER AUTO_INCREMENT,
    lat DECIMAL NOT NULL,
    lng DECIMAL NOT NULL,

    CONSTRAINT pk_geos PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS addresses(
    id INTEGER AUTO_INCREMENT,
    street VARCHAR(30) NOT NULL,
    suite VARCHAR(15) NOT NULL,
    city VARCHAR(20) NOT NULL,
    zipcode VARCHAR(15) NOT NULL,
    geoId INTEGER NOT NULL,

    CONSTRAINT pk_addresses PRIMARY KEY (id),
    CONSTRAINT fk_addresses_geos FOREIGN KEY (geoId)
    REFERENCES geos(id)
);

CREATE TABLE IF NOT EXISTS companies(
    id INTEGER AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL,
    catchPhrase VARCHAR(255) NOT NULL,
    bs VARCHAR(100) NOT NULL,

    CONSTRAINT pk_companies PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS users(
    id INTEGER AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL,
    username VARCHAR(15) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(25) NOT NULL,
    website VARCHAR(255) NOT NULL,
    addressId INTEGER NOT NULL,
    companyId INTEGER NOT NULL,

    CONSTRAINT pk_users PRIMARY KEY (id),
    CONSTRAINT fk_users_addresses FOREIGN KEY (addressId)
    REFERENCES addresses(id),
    CONSTRAINT fk_users_companies FOREIGN KEY (companyId)
    REFERENCES companies(id)
);

CREATE TABLE IF NOT EXISTS posts(
    id INTEGER AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    body VARCHAR(255) NOT NUll,
    userId INTEGER NOT NULL,

    CONSTRAINT pk_posts PRIMARY KEY (id),
    CONSTRAINT fk_posts_users FOREIGN KEY (userId) 
    REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS comments(
    id INTEGER NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(255) NOT NULL,
    body VARCHAR(255) NOT NULL,
    postId INTEGER NOT NULL,

    CONSTRAINT pk_comments PRIMARY KEY (id),
    CONSTRAINT fk_comments_posts FOREIGN KEY (postId) REFERENCES posts(id)
);

CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER AUTO_INCREMENT,
    nombre VARCHAR(30) NOT NULL,
    usuario VARCHAR(15) NOT NULL,
    email VARCHAR(255) NOT NULL,
    contrasena_hash VARCHAR(255) NOT NULL,
    contrasena_salt VARCHAR(255) NOT NULL,

    CONSTRAINT pk_usuarios PRIMARY KEY (id)
);