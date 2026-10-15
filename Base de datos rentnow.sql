CREATE DATABASE rentnow;
use rentnow;

-- =========================================================
-- 1. TABLA ROLES
-- =========================================================

CREATE TABLE roles (
    id_rol INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR(255),
    estado ENUM('activo', 'inactivo') NOT NULL DEFAULT 'activo',
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    fecha_eliminacion TIMESTAMP NULL DEFAULT NULL,

    PRIMARY KEY (id_rol),
    UNIQUE KEY uq_roles_nombre (nombre)
) ENGINE=InnoDB;


-- =========================================================
-- 2. TABLA USUARIOS
-- =========================================================

CREATE TABLE usuarios (
    id_usuario INT NOT NULL AUTO_INCREMENT,
    id_rol INT NOT NULL,
    nombre VARCHAR(150) NOT NULL,
    correo VARCHAR(150) NOT NULL,
    telefono VARCHAR(20),
    contrasena VARCHAR(255) NOT NULL,
    tipo_documento VARCHAR(30) NOT NULL,
    numero_documento VARCHAR(30) NOT NULL,
    estado ENUM('activo', 'inactivo') NOT NULL DEFAULT 'activo',
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    fecha_eliminacion TIMESTAMP NULL DEFAULT NULL,

    PRIMARY KEY (id_usuario),

    UNIQUE KEY uq_usuarios_correo (correo),
    UNIQUE KEY uq_usuarios_documento (numero_documento),

    KEY idx_usuarios_rol (id_rol),

    CONSTRAINT fk_usuarios_roles
        FOREIGN KEY (id_rol)
        REFERENCES roles(id_rol)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
) ENGINE=InnoDB;


-- =========================================================
-- 3. TABLA CATEGORIAS
-- =========================================================

CREATE TABLE categorias (
    id_categoria INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(255),
    estado ENUM('activo', 'inactivo') NOT NULL DEFAULT 'activo',
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    fecha_eliminacion TIMESTAMP NULL DEFAULT NULL,

    PRIMARY KEY (id_categoria),
    UNIQUE KEY uq_categorias_nombre (nombre)
) ENGINE=InnoDB;


-- =========================================================
-- 4. TABLA PUBLICACIONES
-- =========================================================

CREATE TABLE publicaciones (
    id_publicacion INT NOT NULL AUTO_INCREMENT,
    id_usuario INT NOT NULL,
    id_categoria INT NOT NULL,
    titulo VARCHAR(150) NOT NULL,
    descripcion TEXT NOT NULL,
    precio_alquiler DECIMAL(12,2) NOT NULL,
    ubicacion VARCHAR(255) NOT NULL,
    disponibilidad ENUM('disponible', 'ocupado')
        NOT NULL DEFAULT 'disponible',
    estado ENUM('activo', 'inactivo')
        NOT NULL DEFAULT 'activo',
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    fecha_eliminacion TIMESTAMP NULL DEFAULT NULL,

    PRIMARY KEY (id_publicacion),

    KEY idx_publicaciones_usuario (id_usuario),
    KEY idx_publicaciones_categoria (id_categoria),

    CONSTRAINT fk_publicaciones_usuarios
        FOREIGN KEY (id_usuario)
        REFERENCES usuarios(id_usuario)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,

    CONSTRAINT fk_publicaciones_categorias
        FOREIGN KEY (id_categoria)
        REFERENCES categorias(id_categoria)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,

    CONSTRAINT chk_publicaciones_precio
        CHECK (precio_alquiler >= 0)
) ENGINE=InnoDB;


-- =========================================================
-- 5. TABLA PRODUCTOS
-- =========================================================

CREATE TABLE productos (
    id_producto INT NOT NULL AUTO_INCREMENT,
    id_usuario INT NOT NULL,
    id_categoria INT NOT NULL,
    nombre VARCHAR(150) NOT NULL,
    descripcion TEXT,
    estado ENUM(
        'disponible',
        'alquilado',
        'mantenimiento',
        'inactivo'
    ) NOT NULL DEFAULT 'disponible',
    fecha_creacion DATETIME NOT NULL,
    fecha_actualizacion DATETIME NOT NULL,
    fecha_eliminacion DATETIME DEFAULT NULL,

    PRIMARY KEY (id_producto),

    KEY idx_productos_usuario (id_usuario),
    KEY idx_productos_categoria (id_categoria),

    CONSTRAINT fk_productos_usuario
        FOREIGN KEY (id_usuario)
        REFERENCES usuarios(id_usuario)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,

    CONSTRAINT fk_productos_categoria
        FOREIGN KEY (id_categoria)
        REFERENCES categorias(id_categoria)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
) ENGINE=InnoDB;


-- =========================================================
-- 6. TABLA ALQUILERES
-- =========================================================

CREATE TABLE alquileres (
    id_alquiler INT NOT NULL AUTO_INCREMENT,
    id_publicacion INT NOT NULL,
    id_arrendatario INT NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    valor_total DECIMAL(12,2) NOT NULL,
    valor_garantia DECIMAL(12,2) DEFAULT 0.00,

    estado_alquiler ENUM(
        'pendiente',
        'confirmado',
        'activo',
        'finalizado',
        'cancelado'
    ) NOT NULL DEFAULT 'pendiente',

    estado ENUM('activo', 'inactivo')
        NOT NULL DEFAULT 'activo',

    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    fecha_eliminacion TIMESTAMP NULL DEFAULT NULL,

    PRIMARY KEY (id_alquiler),

    KEY idx_alquileres_publicacion (id_publicacion),
    KEY idx_alquileres_arrendatario (id_arrendatario),

    CONSTRAINT fk_alquileres_publicaciones
        FOREIGN KEY (id_publicacion)
        REFERENCES publicaciones(id_publicacion)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,

    CONSTRAINT fk_alquileres_arrendatarios
        FOREIGN KEY (id_arrendatario)
        REFERENCES usuarios(id_usuario)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,

    CONSTRAINT chk_alquileres_fechas
        CHECK (fecha_fin >= fecha_inicio),

    CONSTRAINT chk_alquileres_garantia
        CHECK (valor_garantia >= 0),

    CONSTRAINT chk_alquileres_valor
        CHECK (valor_total >= 0)
) ENGINE=InnoDB;


-- =========================================================
-- 7. TABLA IMAGENES_PUBLICACION
-- =========================================================

CREATE TABLE imagenes_publicacion (
    id_imagen INT NOT NULL AUTO_INCREMENT,
    id_publicacion INT NOT NULL,
    url_imagen VARCHAR(500) NOT NULL,
    es_principal TINYINT(1) NOT NULL DEFAULT 0,
    estado ENUM('activo', 'inactivo')
        NOT NULL DEFAULT 'activo',
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    fecha_eliminacion TIMESTAMP NULL DEFAULT NULL,

    PRIMARY KEY (id_imagen),

    KEY idx_imagenes_publicacion (id_publicacion),

    CONSTRAINT fk_imagenes_publicacion
        FOREIGN KEY (id_publicacion)
        REFERENCES publicaciones(id_publicacion)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB;


-- =========================================================
-- 8. TABLA PAGOS
-- =========================================================

CREATE TABLE pagos (
    id_pago INT NOT NULL AUTO_INCREMENT,
    id_alquiler INT NOT NULL,
    id_usuario INT NOT NULL,
    monto DECIMAL(12,2) NOT NULL,

    metodo_pago ENUM(
        'efectivo',
        'tarjeta',
        'transferencia',
        'pse',
        'otro'
    ) NOT NULL,

    referencia_transaccion VARCHAR(100),

    estado_pago ENUM(
        'pendiente',
        'aprobado',
        'rechazado',
        'reembolsado'
    ) NOT NULL DEFAULT 'pendiente',

    fecha_pago DATETIME DEFAULT NULL,

    estado ENUM('activo', 'inactivo')
        NOT NULL DEFAULT 'activo',

    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    fecha_eliminacion TIMESTAMP NULL DEFAULT NULL,

    PRIMARY KEY (id_pago),

    UNIQUE KEY uq_pagos_referencia (referencia_transaccion),

    KEY idx_pagos_alquiler (id_alquiler),
    KEY idx_pagos_usuario (id_usuario),

    CONSTRAINT fk_pagos_alquileres
        FOREIGN KEY (id_alquiler)
        REFERENCES alquileres(id_alquiler)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,

    CONSTRAINT fk_pagos_usuarios
        FOREIGN KEY (id_usuario)
        REFERENCES usuarios(id_usuario)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,

    CONSTRAINT chk_pagos_monto
        CHECK (monto > 0)
) ENGINE=InnoDB;


-- =========================================================
-- 9. TABLA ENTREGAS
-- =========================================================

CREATE TABLE entregas (
    id_entrega INT NOT NULL AUTO_INCREMENT,
    id_alquiler INT NOT NULL,
    fecha_entrega DATETIME DEFAULT NULL,
    fecha_devolucion DATETIME DEFAULT NULL,
    direccion_entrega VARCHAR(255) NOT NULL,

    estado_entrega ENUM(
        'pendiente',
        'en_camino',
        'entregado',
        'devuelto',
        'cancelado'
    ) NOT NULL DEFAULT 'pendiente',

    condicion_entrega VARCHAR(255),
    condicion_devolucion VARCHAR(255),

    estado ENUM('activo', 'inactivo')
        NOT NULL DEFAULT 'activo',

    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    fecha_eliminacion TIMESTAMP NULL DEFAULT NULL,

    PRIMARY KEY (id_entrega),

    KEY idx_entregas_alquiler (id_alquiler),

    CONSTRAINT fk_entregas_alquileres
        FOREIGN KEY (id_alquiler)
        REFERENCES alquileres(id_alquiler)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
) ENGINE=InnoDB;


-- =========================================================
-- 10. TABLA RESENAS
-- =========================================================

CREATE TABLE resenas (
    id_resena INT NOT NULL AUTO_INCREMENT,
    id_alquiler INT NOT NULL,
    id_usuario INT NOT NULL,
    calificacion INT NOT NULL,
    comentario TEXT,

    estado ENUM('activo', 'inactivo')
        NOT NULL DEFAULT 'activo',

    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    fecha_eliminacion TIMESTAMP NULL DEFAULT NULL,

    PRIMARY KEY (id_resena),

    UNIQUE KEY uq_resena_alquiler_usuario
        (id_alquiler, id_usuario),

    KEY idx_resenas_usuario (id_usuario),

    CONSTRAINT fk_resenas_alquileres
        FOREIGN KEY (id_alquiler)
        REFERENCES alquileres(id_alquiler)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,

    CONSTRAINT fk_resenas_usuarios
        FOREIGN KEY (id_usuario)
        REFERENCES usuarios(id_usuario)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,

    CONSTRAINT chk_resenas_calificacion
        CHECK (calificacion BETWEEN 1 AND 5)
) ENGINE=InnoDB;


-- =========================================================
-- 11. TABLA REPORTES
-- =========================================================

CREATE TABLE reportes (
    id_reporte INT NOT NULL AUTO_INCREMENT,
    id_reportante INT NOT NULL,
    id_usuario_reportado INT DEFAULT NULL,
    id_publicacion INT DEFAULT NULL,
    motivo VARCHAR(150) NOT NULL,
    descripcion TEXT NOT NULL,

    estado_reporte ENUM(
        'pendiente',
        'en_revision',
        'resuelto',
        'rechazado'
    ) NOT NULL DEFAULT 'pendiente',

    estado ENUM('activo', 'inactivo')
        NOT NULL DEFAULT 'activo',

    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    fecha_eliminacion TIMESTAMP NULL DEFAULT NULL,

    PRIMARY KEY (id_reporte),

    KEY idx_reportes_reportante (id_reportante),
    KEY idx_reportes_usuario_reportado (id_usuario_reportado),
    KEY idx_reportes_publicacion (id_publicacion),

    CONSTRAINT fk_reportes_reportante
        FOREIGN KEY (id_reportante)
        REFERENCES usuarios(id_usuario)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,

    CONSTRAINT fk_reportes_usuario_reportado
        FOREIGN KEY (id_usuario_reportado)
        REFERENCES usuarios(id_usuario)
        ON DELETE SET NULL
        ON UPDATE CASCADE,

    CONSTRAINT fk_reportes_publicaciones
        FOREIGN KEY (id_publicacion)
        REFERENCES publicaciones(id_publicacion)
        ON DELETE SET NULL
        ON UPDATE CASCADE
) ENGINE=InnoDB;


-- =========================================================
-- 12. DATOS INICIALES DE ROLES
-- =========================================================

INSERT INTO roles (nombre, descripcion)
VALUES
('administrador', 'Gestiona y administra toda la plataforma'),
('arrendador', 'Publica productos para alquilar'),
('arrendatario', 'Realiza alquileres de productos'),
('usuario', 'Usuario general de la plataforma');


-- =========================================================
-- VERIFICACIÓN
-- =========================================================

SHOW TABLES;
