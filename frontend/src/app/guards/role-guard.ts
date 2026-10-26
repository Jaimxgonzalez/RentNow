import { inject } from '@angular/core';
import { Router, CanActivateFn } from '@angular/router';

export const roleGuard: CanActivateFn = (route, state) => {
  const router = inject(Router);
  
  // Obtenemos el rol guardado en localStorage
  const userRole = localStorage.getItem('user_role');
  
  // Obtenemos los roles permitidos definidos en la ruta
  const allowedRoles = route.data['roles'] as Array<string>;

  // Validamos si el usuario tiene un rol y si está dentro de los permitidos
  if (userRole && allowedRoles && allowedRoles.includes(userRole)) {
    return true;
  }

  // Si no tiene acceso, lo redirigimos al login o productos
  console.warn('Acceso denegado: Rol insuficiente');
  router.navigate(['/login']);
  return false;
};