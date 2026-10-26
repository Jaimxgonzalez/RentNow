import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';

interface Producto {
  id: number;
  nombre: string;
  categoria: string;
  precioDia: number;
  estado: 'Disponible' | 'Alquilado' | 'Mantenimiento';
  imagenUrl: string;
}

@Component({
  selector: 'app-mis-productos',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './mis-productos.html',
  styleUrl: './mis-productos.css'
})
export class MisProductosComponent implements OnInit {
  misProductos: Producto[] = [
    {
      id: 1,
      nombre: 'Cámara DSLR Canon EOS',
      categoria: 'Fotografía',
      precioDia: 45000,
      estado: 'Disponible',
      imagenUrl: 'https://via.placeholder.com/150'
    },
    {
      id: 2,
      nombre: 'Taladro Inalámbrico Dewalt',
      categoria: 'Herramientas',
      precioDia: 25000,
      estado: 'Alquilado',
      imagenUrl: 'https://via.placeholder.com/150'
    }
  ];

  ngOnInit(): void {
    // Aquí más adelante llamaremos a tu servicio backend para cargar la lista real desde Django
  }

  eliminarProducto(id: number): void {
    if (confirm('¿Estás seguro de que deseas eliminar esta publicación?')) {
      this.misProductos = this.misProductos.filter(p => p.id !== id);
    }
  }
}
