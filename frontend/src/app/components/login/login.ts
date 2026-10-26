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
      // Puedes cambiar '/productos' por la ruta que prefieras en tu aplicación
      this.router.navigate(['/productos']); 
    },
    error: (err) => {
      this.errorMessage = 'Usuario o contraseña incorrectos.';
    }
  });
}
}