import { Routes } from '@angular/router';
import { LoginComponent } from './components/login/login';
import { authGuard } from './guards/auth-guard';

export const routes: Routes = [
  // Ruta pública de inicio de sesión
  { path: 'login', component: LoginComponent },
  
  // Ejemplo de ruta protegida con tu authGuard:
  // { path: 'dashboard', component: DashboardComponent, canActivate: [authGuard] },

  // Redirección por defecto al login si no coincide ninguna ruta
  { path: '', redirectTo: 'login', pathMatch: 'full' },
  { path: '**', redirectTo: 'login' }
];