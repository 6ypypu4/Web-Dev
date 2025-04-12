import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Company } from '../interfaces/company';
import { Vacancy } from '../interfaces/vacancy';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  BASE_URL = 'http://127.0.0.1:8000/api';

  constructor(private client: HttpClient) { }

  getCompanies(): Observable<Company[]> {
    return this.client.get<Company[]>(`${this.BASE_URL}/companies/`);
  }

  getCompanyVacancies(id: number): Observable<Vacancy[]> {
    return this.client.get<Vacancy[]>(`${this.BASE_URL}/companies/${id}/vacancies/`);
  }
}
