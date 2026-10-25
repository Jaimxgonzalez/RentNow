import { inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';
import { AuthService } from '../services/auth'; // <--- Cambiado aquí

export const authGuard: CanActivateFn = (route, state) => {
  const authService = inject(AuthService);
  const router = inject(Router);

  // Verificamos si el usuario está autenticado
  if (authService.isAuthenticated()) {
    return true; // Permite el acceso a la ruta
  } else {
    // Si no está autenticado, redirige al inicio
    router.navigate(['/']);
    return false;
  }
};