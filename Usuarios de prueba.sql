-- Un usuario por rol para probar el RBAC. Contraseña de todos: Rentnow123
-- Ejecutar DESPUÉS de importar "Base de datos rentnow.sql".
-- Roles: 1 administrador, 2 arrendador, 3 arrendatario, 4 usuario
USE rentnow;
INSERT INTO usuarios (id_rol, nombre, correo, telefono, contrasena, tipo_documento, numero_documento, estado) VALUES
(1, 'Admin Prueba',        'admin@rentnow.com',        '3000000001', 'pbkdf2_sha256$1000000$Et5S7ufN6pOmESvG6Clkjy$BreqKwkmMK8DgfrYdFJ6DupwnVA3fEU7ypJthqhluEQ=', 'CC', '1000000001', 'activo'),
(2, 'Arrendador Prueba',   'arrendador@rentnow.com',   '3000000002', 'pbkdf2_sha256$1000000$Et5S7ufN6pOmESvG6Clkjy$BreqKwkmMK8DgfrYdFJ6DupwnVA3fEU7ypJthqhluEQ=', 'CC', '1000000002', 'activo'),
(3, 'Arrendatario Prueba', 'arrendatario@rentnow.com', '3000000003', 'pbkdf2_sha256$1000000$Et5S7ufN6pOmESvG6Clkjy$BreqKwkmMK8DgfrYdFJ6DupwnVA3fEU7ypJthqhluEQ=', 'CC', '1000000003', 'activo'),
(4, 'Usuario Prueba',      'usuario@rentnow.com',      '3000000004', 'pbkdf2_sha256$1000000$Et5S7ufN6pOmESvG6Clkjy$BreqKwkmMK8DgfrYdFJ6DupwnVA3fEU7ypJthqhluEQ=', 'CC', '1000000004', 'activo');
