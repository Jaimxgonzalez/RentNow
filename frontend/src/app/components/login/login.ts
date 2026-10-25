import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './login.html',
  styleUrls: ['./login.css']
})
export class LoginComponent {
  credentials = {
    username: '',
    password: ''
  };
  errorMessage = '';

  constructor(private authService: AuthService, private router: Router) {}

  onLogin(): void {
    this.authService.login(this.credentials).subscribe({
      next: (response) => {
        // Guarda el token devuelto por la API de Django
        const token = response.token || response.access;
        if (token) {
          this.authService.saveToken(token);
          // Redirige a la página principal tras un inicio de sesión exitoso
          this.router.navigate(['/']);
        }
      },
      error: (err) => {
        console.error('Error de autenticación', err);
        this.errorMessage = 'Usuario o contraseña incorrectos.';
      }
    });
  }
}