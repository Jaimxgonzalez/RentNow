import { Routes } from '@angular/router';
import { LoginComponent } from './components/login/login';
import { ProductosComponent } from './components/productos/productos';
import { authGuard } from './guards/auth-guard';

export const routes: Routes = [
  // Ruta pública de inicio de sesión
  { path: 'login', component: LoginComponent },
  
  // ¡Agrega la ruta de productos aquí!
{ path: 'productos', component: ProductosComponent },
  
  // Redirección por defecto al login
  { path: '', redirectTo: 'login', pathMatch: 'full' },
  { path: '**', redirectTo: 'login' }
];