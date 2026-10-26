import { Routes } from '@angular/router';
import { LoginComponent } from './components/login/login';
import { ProductosComponent } from './components/productos/productos';
import { MisProductosComponent } from './components/mis-productos/mis-productos';
import { AdminDashboardComponent } from './components/admin-dashboard/admin-dashboard';
import { roleGuard } from './guards/role-guard';

export const routes: Routes = [
  // Ruta raíz que redirige al login
  { path: '', redirectTo: 'login', pathMatch: 'full' },
  
  // Ruta de inicio de sesión
  { path: 'login', component: LoginComponent },

  // Catálogo general
  { 
    path: 'productos', 
    component: ProductosComponent, 
    canActivate: [roleGuard], 
    data: { roles: ['Cliente', 'Usuario', 'Arrendatario', 'Arrendador', 'Admin', 'Administrador'] } 
  },

  // Vista exclusiva de Arrendadores
  { 
    path: 'mis-productos', 
    component: MisProductosComponent,
    canActivate: [roleGuard],
    data: { roles: ['Arrendador', 'Admin', 'Administrador'] }
  },

  // Panel de control exclusivo de Administradores
  { 
    path: 'admin-dashboard', 
    component: AdminDashboardComponent,
    canActivate: [roleGuard],
    data: { roles: ['Admin', 'Administrador'] }
  },

  // Comodín para rutas no encontradas
  { path: '**', redirectTo: 'login' }
];