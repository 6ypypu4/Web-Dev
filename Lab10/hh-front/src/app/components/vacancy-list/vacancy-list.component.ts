import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/services/api.service';
import { Company } from 'src/app/interfaces/company';
import { Vacancy } from 'src/app/interfaces/vacancy';

@Component({
  selector: 'app-company-list',
  templateUrl: './company-list.component.html'
})
export class CompanyListComponent implements OnInit {
  companies: Company[] = [];
  vacancies: Vacancy[] = [];
  selectedCompanyId: number | null = null;

  constructor(private api: ApiService) {}

  ngOnInit(): void {
    this.api.getCompanies().subscribe(data => {
      this.companies = data;
    });
  }

  showVacancies(id: number): void {
    this.selectedCompanyId = id;
    this.api.getCompanyVacancies(id).subscribe(data => {
      this.vacancies = data;
    });
  }
}
