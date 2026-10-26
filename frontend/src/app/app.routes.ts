import { Routes } from '@angular/router';
import { LoginComponent } from './components/login/login';
import { ProductosComponent } from './components/productos/productos';
import { roleGuard } from './guards/role-guard';

export const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { 
    path: 'productos', 
    component: ProductosComponent,
    canActivate: [roleGuard],
    data: { roles: ['Cliente', 'Admin', 'Arrendador'] } 
  },
  { path: '', redirectTo: 'login', pathMatch: 'full' },
  { path: '**', redirectTo: 'login' }
];