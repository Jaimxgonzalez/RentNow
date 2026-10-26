import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

interface Usuario {
  id: number;
  nombre: string;
  email: string;
  rol: 'Cliente' | 'Arrendador' | 'Admin';
  estado: 'Activo' | 'Inactivo';
}

interface Reporte {
  id: number;
  reportadoPor: string;
  motivo: string;
  estado: 'Pendiente' | 'Resuelto';
}

@Component({
  selector: 'app-admin-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './admin-dashboard.html',
  styleUrl: './admin-dashboard.css'
})
export class AdminDashboardComponent implements OnInit {
  pestanaActiva: 'usuarios' | 'reportes' = 'usuarios';

  usuarios: Usuario[] = [
    { id: 1, nombre: 'María Hernández', email: 'maria@example.com', rol: 'Arrendador', estado: 'Activo' },
    { id: 2, nombre: 'Carlos Gómez', email: 'carlos@example.com', rol: 'Cliente', estado: 'Activo' },
    { id: 3, nombre: 'Juan Pérez', email: 'juan@example.com', rol: 'Cliente', estado: 'Inactivo' }
  ];

  reportes: Reporte[] = [
    { id: 101, reportadoPor: 'Carlos Gómez', motivo: 'Producto entregado en mal estado', estado: 'Pendiente' },
    { id: 102, reportadoPor: 'María Hernández', motivo: 'Pago no reflejado en pasarela', estado: 'Resuelto' }
  ];

  ngOnInit(): void {}

  cambiarPestana(pestana: 'usuarios' | 'reportes'): void {
    this.pestanaActiva = pestana;
  }

  toggleEstadoUsuario(usuario: Usuario): void {
    usuario.estado = usuario.estado === 'Activo' ? 'Inactivo' : 'Activo';
  }

  resolverReporte(reporte: Reporte): void {
    reporte.estado = 'Resuelto';
  }
}