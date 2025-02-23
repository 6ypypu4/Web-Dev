import { Component } from '@angular/core';
import { AppService } from './app.service';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterModule],
  templateUrl: `app.component.html`,
  styleUrl: `app.component.css`
})
export class AppComponent {
  categories: string[];

  constructor(private appService: AppService) {
    this.categories = this.appService.getCategories();
  }
}
