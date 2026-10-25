import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  // URL base de tu API de Django (puerto 8000)
  private apiUrl = 'http://localhost:8000/api'; 

  constructor(private http: HttpClient) {}

  // Método para iniciar sesión
  login(credentials: { username: string; password: string }): Observable<any> {
    return this.http.post(`${this.apiUrl}/login/`, credentials);
  }

  // Guardar el token en el almacenamiento local
  saveToken(token: string): void {
    localStorage.setItem('auth_token', token);
  }

  // Obtener el token guardado
  getToken(): string | null {
    return localStorage.getItem('auth_token');
  }

  // Verificar si el usuario está autenticado
  isAuthenticated(): boolean {
    return !!this.getToken();
  }

  // Cerrar sesión
  logout(): void {
    localStorage.removeItem('auth_token');
  }
}