import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { AuthService } from '../../services/auth';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, FormsModule], // <--- IMPORTANTE: Asegúrate de incluir estos dos aquí
  templateUrl: './login.html',
  styleUrl: './login.css'
})
export class LoginComponent {
  credentials = { correo: '', contrasena: '' };
  errorMessage = '';

  constructor(private authService: AuthService, private router: Router) {}

  onLogin() {
  this.authService.login(this.credentials).subscribe({
    next: (res: any) => {
      // Aquí redirigimos al usuario una vez que el login es exitoso
      // Guardamos el token y el rol en localStorage
        // Si el JSON de Django devuelve el rol como res.rol o res.usuario.rol:
      if (res.token) {
          localStorage.setItem('auth_token', res.token);
      }

      // Guardamos el rol (ajusta 'res.rol' según el atributo que mande el backend)
        const rolUsuario = res.rol || res.role || res.usuario?.rol || 'Cliente';
        localStorage.setItem('user_role', rolUsuario);
      // Puedes cambiar '/productos' por la ruta que prefieras en tu aplicación
      this.router.navigate(['/productos']); 
    },
    error: (err) => {
      console.error('Error detallado del login:', err); // <-- Añade esto
      this.errorMessage = 'Usuario o contraseña incorrectos.';
    }
  });
}
}